def main():
    log_file = "auth_test.txt"
    try:

     with open(log_file,"r")as file:
        data_logs = file.read()
        print (data_logs)
    except FileNotFoundError:
        print(f"File {log_file} not Found")

if __name__ == "__main__":
    main()