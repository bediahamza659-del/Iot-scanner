def detect_device(mac, ports):
    ports = ports if ports else []
    mac = mac.lower() if mac else ""

    # Camera
    if 554 in ports:
        return "📷 Camera"

    # Console (PlayStation / Xbox)
    if 3074 in ports:
        return "🎮 Gaming Console"

    # Smart TV
    if 8008 in ports or 8009 in ports:
        return "📺 Smart TV"

    #  Router
    if 1900 in ports:
        return "📡 Router / Gateway"

    # IoT (MQTT, capteurs)
    if 1883 in ports:
        return "📡 IoT Sensor"

    #  PC
    if 22 in ports or 3389 in ports or 135 in ports:
        return "💻 PC"

    #  Téléphone (approximation)
    if len(ports) <= 1:
        return "📱 Smartphone"

    # fallback IoT générique
    return "📡 Connected Device"