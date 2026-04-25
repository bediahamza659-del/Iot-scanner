import socket

def get_local_network():
    ip = socket.gethostbyname(socket.gethostname())
    parts = ip.split(".")
    return f"{parts[0]}.{parts[1]}.{parts[2]}.0/24"