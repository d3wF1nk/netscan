import time

from network_scanner import get_local_ip, scan_local_network, remove_last_octet, run_nmap_scan
from print_utils import print_banner, print_scanning_dots, print_tcp_properties, print_debug, set_debug_mode
import argparse

debug_mode = False


def main():
    local_ip = get_local_ip()
    if local_ip:
        print(f"LOCAL_IP: {local_ip}\n")
        ip_range = remove_last_octet(local_ip)
        start, end = 1, 254
        if debug_mode:
            start, end = 100, 105
        print(f"SCANNING {ip_range}.{start} -> {ip_range}.{end}:\n")
        print_scanning_dots()
        hosts = scan_local_network(local_ip, start, end)
        for i, (ip, name) in enumerate(hosts, 0):
            print(f"IP: {ip} - [{name}][{i}]")
        decimal_value = input("\n[insert decimal value] or (press Enter to scan all devices): ")
        if decimal_value:
            try:
                device_number = int(decimal_value)
                if 0 <= device_number < len(hosts):
                    ip, name = hosts[device_number]
                    print(f"\nScanning selected device: IP: {ip} - Name: {name}")
                    rs = run_nmap_scan(ip)
                    print_tcp_properties(ip, rs)
                else:
                    print("Invalid device number.")
            except ValueError:
                print("Invalid input.")
        else:
            print("Scanning all devices...")
            print_scanning_dots()
            for i, (ip, name) in enumerate(hosts, 0):
                print(f"Scanning device: IP: {ip} - Name: {name}")
                rs = run_nmap_scan(ip)
                print_tcp_properties(ip, rs)
                time.sleep(1)
    else:
        print(f"ERROR: CANT_GET_LOCAL_IP")


def enable_debug_mode():
    global debug_mode
    debug_mode = True
    set_debug_mode(debug_mode)
    print_debug("debug_mode.enabled")


def evaluate_args():
    parser = argparse.ArgumentParser(description="BFK-NTScan")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    args = parser.parse_args()
    if args.debug:
        enable_debug_mode()


if __name__ == "__main__":
    print_banner()
    evaluate_args()
    main()
    print(f"\n")
