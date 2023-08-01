import time

debug_mode = False


def set_debug_mode(value):
    global debug_mode
    debug_mode = value


def print_tcp_properties(ip, rs):
    if ip in rs:
        mac_address = rs[ip]['addresses']['mac']
        vendor = rs[ip]['vendor'][mac_address]
        print(f"    MAC Address: {mac_address}, Vendor: {vendor}")
        print()
        tcp_properties = rs[ip]['tcp']
        for port, port_info in tcp_properties.items():
            print(f"Port: {port}")
            print(f"  Name: {port_info['name']}")
            print(f"  Product: {port_info['product']}")
            print()


def print_banner():
    banner = r"""
      :::::::::  :::::::::: :::    :::  ::::::::  :::    :::  ::::::::   :::::::: 
     :+:    :+: :+:        :+:   :+:  :+:    :+: :+:   :+:  :+:    :+: :+:    :+: 
    +:+    +:+ +:+        +:+  +:+         +:+  +:+  +:+         +:+         +:+  
   +#++:++#+  :#::+::#   +#++:++        +#+    +#++:++        +#+        +#++:    
  +#+    +#+ +#+        +#+  +#+     +#+      +#+  +#+     +#+             +#+    
 #+#    #+# #+#        #+#   #+#   #+#       #+#   #+#   #+#       #+#    #+#     
#########  ###        ###    ### ########## ###    ### ##########  ########       
    """
    print(banner)


def print_scanning_dots():
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\n")


def print_debug(message):
    if debug_mode:
        print(f"[DEBUG]{message}\n")
