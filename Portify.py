import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(target_ip, port):
    """Scans a single port and returns the port number if open."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"[+] Port {port}: OPEN")
            return port
    return None

def main():
    target_ip = input("Enter Target IP: ").strip()
    start_port = int(input("Start Port: "))
    end_port = int(input("End Port: "))
    threads = int(input("Number of Threads (e.g. 50): "))

    print(f"\n[!] Fast-scanning {target_ip} with {threads} threads...\n")
    open_ports = []

    # ThreadPoolExecutor handles thread creation and memory clean-up
    with ThreadPoolExecutor(max_workers=threads) as executor:
        results = [
            executor.submit(scan_port, target_ip, port)
            for port in range(start_port, end_port + 1)
        ]
        
        for future in results:
            res = future.result()
            if res:
                open_ports.append(res)

    print(f"\n Complete. Open Ports: {sorted(open_ports)}")

if __name__ == "__main__":
    main()