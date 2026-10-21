
def log_analyse(data):
    for line in data:
        line = data.strip()
        for parts in line:
            parts = line.split()
            if "from" in parts:
                from_index = parts.index("from")
                ip_address = parts[from_index + 1]
                print(ip_address)

def main():
    log_file = "auth_test.txt"
    try:

     with open(log_file,"r")as file:
        data_logs = file.read()
        log_analyse(data_logs)
    except FileNotFoundError:
        print(f"File {log_file} not Found")
    return data_logs

if __name__ == "__main__":
    main()