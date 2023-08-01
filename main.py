from network_scanner import get_local_ip, scan_local_network, remove_last_octet
from print_utils import print_banner, print_scanning_dots

if __name__ == "__main__":
    print_banner()
    local_ip = get_local_ip()
    if local_ip:
        print(f"LOCAL_IP: {local_ip}\n")

        ip_range = remove_last_octet(local_ip)
        start, end = 1, 254
        print(f"SCANNING {ip_range}.{start} -> {ip_range}.{end}:\n")
        print_scanning_dots()
        hosts = scan_local_network(local_ip)

        for i, (ip, name) in enumerate(hosts, 0):
            print(f"IP: {ip} - [{name}][{i}]")

    else:
        print(f"ERROR: CANT_GET_LOCAL_IP")

    print(f"\n")
