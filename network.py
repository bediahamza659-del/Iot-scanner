import socket
import ipaddress
import subprocess
import platform
import re
import signal
import sys

# Variable globale pour gérer l'arrêt
stop_flag = False

def signal_handler(sig, frame):
    global stop_flag
    stop_flag = True
    print("\n✓ Arrêt du programme...")
    sys.exit(0)

# Configure le signal handler au démarrage
signal.signal(signal.SIGINT, signal_handler)


def get_local_network():
    """Retourne le réseau local avec un masque approprié."""
    
    ip = get_active_ip()
    if ip and not ip.startswith("127."):
        netmask = get_netmask_for_ip(ip)
        if netmask:
            try:
                network = ipaddress.ip_network(f"{ip}/{netmask}", strict=False)
                return str(network)
            except:
                pass
        
        try:
            network = ipaddress.ip_network(f"{ip}/24", strict=False)
            return str(network)
        except:
            pass
    
    return None


def get_active_ip():
    """Obtient l'IP active."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(2)  # TIMEOUT !
        sock.connect(("8.8.8.8", 80))
        ip = sock.getsockname()[0]
        sock.close()
        return ip
    except:
        pass
    
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        if not ip.startswith("127."):
            return ip
    except:
        pass
    
    return None


def get_netmask_for_ip(ip):
    """Récupère le masque de sous-réseau réel."""
    system = platform.system()
    
    if system == "Windows":
        return get_netmask_windows(ip)
    elif system in ["Linux", "Darwin"]:
        return get_netmask_unix(ip)
    
    return None


def get_netmask_windows(ip):
    """Récupère le netmask sous Windows avec TIMEOUT"""
    try:
        output = subprocess.check_output(
            ["ipconfig", "/all"],
            text=True,
            stderr=subprocess.DEVNULL,
            timeout=5  # TIMEOUT !!
        )
        
        lines = output.split("\n")
        for i, line in enumerate(lines):
            if ip in line:
                for j in range(i, min(i+5, len(lines))):
                    if "Subnet Mask" in lines[j] or "Masque de sous-réseau" in lines[j]:
                        match = re.search(r"(\d+\.\d+\.\d+\.\d+)", lines[j])
                        if match:
                            return match.group(1)
        return None
    except subprocess.TimeoutExpired:
        print("⚠️ Timeout ipconfig")
        return None
    except:
        return None


def get_netmask_unix(ip):
    """Récupère le netmask sous Linux/macOS avec TIMEOUT"""
    try:
        output = subprocess.check_output(
            ["ip", "addr", "show"],
            text=True,
            stderr=subprocess.DEVNULL,
            timeout=5  # TIMEOUT !!
        )
        
        lines = output.split("\n")
        for i, line in enumerate(lines):
            if ip in line:
                match = re.search(rf"{re.escape(ip)}/(\d+)", line)
                if match:
                    cidr = match.group(1)
                    return int(cidr)
        return None
    except subprocess.TimeoutExpired:
        print("⚠️ Timeout ip addr")
        pass
    except:
        pass
    
    # Fallback macOS
    try:
        output = subprocess.check_output(
            ["ifconfig"],
            text=True,
            stderr=subprocess.DEVNULL,
            timeout=5  # TIMEOUT !!
        )
        
        lines = output.split("\n")
        for i, line in enumerate(lines):
            if ip in line:
                for j in range(max(0, i-2), min(i+3, len(lines))):
                    if "netmask" in lines[j]:
                        match = re.search(r"0x([0-9a-f]+)", lines[j])
                        if match:
                            hex_mask = match.group(1)
                            return hex_to_cidr(hex_mask)
        return None
    except subprocess.TimeoutExpired:
        print("⚠️ Timeout ifconfig")
        return None
    except:
        return None


def hex_to_cidr(hex_mask):
    """Convertit un masque en hex en CIDR"""
    try:
        int_mask = int(hex_mask, 16)
        return bin(int_mask).count('1')
    except:
        return None


# Test
if __name__ == "__main__":
    print("Récupération du réseau local...")
    network = get_local_network()
    print(f"✓ Network: {network}")
    print(f"✓ Active IP: {get_active_ip()}")
    print("\nAppuyez sur Ctrl+C pour arrêter")
