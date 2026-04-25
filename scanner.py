import nmap

nm = nmap.PortScanner()

def scan_network(network):
    devices = []

    try:
        nm.scan(hosts=network, arguments="-sn")
    except:
        return devices

    for host in nm.all_hosts():
        mac = None

        if "addresses" in nm[host]:
            mac = nm[host]["addresses"].get("mac")

        devices.append({
            "ip": host,
            "mac": mac
        })

    return devices


def scan_ports(ip):
    try:
        nm.scan(ip, arguments="-sS -T4")

        if ip not in nm.all_hosts():
            return []

        if "tcp" not in nm[ip]:
            return []

        return list(nm[ip]["tcp"].keys())

    except:
        return []