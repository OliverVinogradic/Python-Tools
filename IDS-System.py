import time

access_log = "/var/log/httpd/access_log"


def transform_logs(temp_result_list):
     all_dics = []

     for row in temp_result_list:
    
        ipadress = row[0]
        date = row[1]
        http_m = row[2]
        s_code = row[3]

        temp_dict = {
            "IP_Adress": ipadress,
            "Date & Time": date,
            "HTTP Methode & Path": http_m,
            "Status Code": s_code
        }
    
        all_dics.append(temp_dict)
     return all_dics

def extract_logs():
    temp_result_list = []
    with open(access_log,"r") as file:
        for line in file:
            cleaned_line = line.strip()

            if not cleaned_line:
               continue
            data = cleaned_line.split(" - ")

            temp_result_list.append(data)
            
    return temp_result_list


def analyse_logs(data_dictonary):
    for data in data_dictonary:
        status_code = int(data.get("Status Code"))
        if status_code == 401 or status_code == 403:
            intruder_ip = data.get("IP_Adress")
            date = data.get("Date & Time")
            print(f"[!]{intruder_ip} logged in {date} at {status_code}")
        else:
            print("[+] No errors !")

        
    
        

def main():
    low_res = extract_logs()
    mid_res = transform_logs(low_res)
    end_res = analyse_logs(mid_res)


if __name__ == "__main__":
    main()