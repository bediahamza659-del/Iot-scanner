from flask import Flask, render_template, jsonify
from network import get_local_network
from scanner import scan_network, scan_ports
from analyzer import detect_device
from security import calculate_risk

app = Flask(__name__)

def perform_scan():
    network = get_local_network()
    devices = scan_network(network)

    results = []

    for d in devices:
        ip = d.get("ip")
        mac = d.get("mac")

        ports = scan_ports(ip)
        device_type = detect_device(mac, ports)
        risk = calculate_risk(ports)

        results.append({
            "ip": ip,
            "type": device_type,
            "ports": ports,
            "risk": risk
        })

    return results


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/scan")
def scan():
    return jsonify(perform_scan())


if __name__ == "__main__":
    
    app.run(host="127.0.0.1", port=5000, debug=True)