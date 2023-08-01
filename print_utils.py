import time


def print_tcp_properties(ip, rs):
    if ip in rs:
        tcp_properties = rs[ip]['tcp']
        for port, port_info in tcp_properties.items():
            print(f"Port: {port}")
            # print(f"  State: {port_info['state']}")
            # print(f"  Reason: {port_info['reason']}")
            print(f"  Name: {port_info['name']}")
            print(f"  Product: {port_info['product']}")
            # print(f"  Version: {port_info['version']}")
            # print(f"  Extra Info: {port_info['extrainfo']}")
            # print(f"  Conf: {port_info['conf']}")
            # print(f"  CPE: {port_info['cpe']}")
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
