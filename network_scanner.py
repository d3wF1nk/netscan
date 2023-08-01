import socket

def remove_last_octet(ip_address):
    parts = ip_address.split(".")
    ip_range = ".".join(parts[:-1])
    return ip_range

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except socket.error as e:
        print(f"ERROR: {e}")
        return None

def scan_local_network(ip_address):
    ip_range = remove_last_octet(ip_address)
    nstart, nend = 1, 254    
    active_hosts = []

    for host in range(nstart, nend):
        target_ip = ip_range + "." + str(host)
        try:
            hostname = socket.gethostbyaddr(target_ip)
            active_hosts.append((target_ip, hostname[0]))
        except socket.error as e:
            pass

    return active_hosts