import socket

def get_user_input():
    print("=== Target & Port Configuration ===")
    
    # 1. IP Address Input (Validation as String)
    while True:
        target_ip = input("Enter Target IP Address (e.g., 127.0.0.1): ").strip()
        try:
            socket.inet_aton(target_ip)  # Validates IPv4 structure
            break
        except socket.error:
            print("Invalid IP Address format. Try again.\n")

    # 2. Port Range Input
    while True:
        try:
            s_port = int(input("Enter Starting Port (1-65535): "))
            e_port = int(input("Enter Ending Port (1-65535): "))
            
            if 1 <= s_port <= e_port <= 65535:
                return target_ip, s_port, e_port
            print("Ports must be between 1 and 65535, and End Port >= Start Port.\n")
        except ValueError:
            print("Please enter valid integer numbers only.\n")


def port_scanner(target_ip, s_port, e_port):
    print(f"\nScanning target {target_ip} from port {s_port} to {e_port}...\n")
    open_ports = []

    for port in range(s_port, e_port + 1):
        # Using context manager for automatic socket cleanup
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.2)
            result = s.connect_ex((target_ip, port))
            if result == 0:
                print(f"[+] Port {port}: OPEN")
                open_ports.append(port)

    return open_ports


def main():
    target_ip, s_port, e_port = get_user_input()
    open_ports = port_scanner(target_ip, s_port, e_port)
    print(f"\nScan complete. Found {len(open_ports)} open port(s): {open_ports}")


if __name__ == "__main__":
    main()