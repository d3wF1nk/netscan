from network_scanner import get_local_ip, scan_local_network, remove_last_octet, run_nmap_scan
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

        decimal_value = input("\n[insert decimal value] or (press Enter to scan all devices): ")
        if decimal_value:
            try:
                device_number = int(decimal_value)
                if 0 <= device_number < len(hosts):
                    ip, name = hosts[device_number]
                    print(f"Scanning selected device: IP: {ip} - Name: {name}")
                    run_nmap_scan(ip)
                else:
                    print("Invalid device number.")
            except ValueError:
                print("Invalid input.")
        else:
            print("Scanning all devices...")
    else:
        print(f"ERROR: CANT_GET_LOCAL_IP")
    print(f"\n")
