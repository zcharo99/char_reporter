from modules.menu import *
from modules.report import *
from modules.getuid import *
import modules.config
import platform
import os
import json
import time

menuchoices = ["Report User", "Set Interval", "Set report type", "Set cookie", "Exit"]

def clearscreen():
    if platform.system == "Windows":
        os.system('cls')
    else:
        os.system('clear')

print("[+] Starting...")

if not os.path.exists('config.json') or os.path.getsize('config.json') == 0:
    default_data = {
        'interval': 5,
        'reportID': 5,
        'cookie': 'unknown'
    }
    with open('config.json', 'w') as file:
        json.dump(default_data, file, indent=4)

parsed_config = modules.config.parse('config.json')

report_interval = modules.config.getvaluekey(parsed_config, 'interval')
report_id = modules.config.getvaluekey(parsed_config, 'reportID')
cookie = modules.config.getvaluekey(parsed_config, 'cookie')

clearscreen()

title("normal")
choices("square_brackets", menuchoices)
while True:
    choice = input("[+] Enter choice: ")
    if choice == "1":
        if cookie == "unknown":
            print("[-] Please set a cookie first")
        else:
            clearscreen()
            title('normal')
            username = input("[+] Username to report: ")
            try:
                userid = getuid(username)
            except Exception as e:
                print(f"[-] Error: {e}")
            times = input("[+] Number of reports: ")
            print("[+] Starting in 3")
            time.sleep(1)
            print("[+] Starting in 2")
            time.sleep(1)
            print("[+] Starting in 1")
            time.sleep(1)
            clearscreen()
            title("normal")
            url = 'https://report.roblox.com/v2/report'
            headers = {
                'Cookie': f'.ROBLOSECURITY={cookie}',
                'Content-Type': 'application/json'
            }
            data = {
                'UserID': userid,
                'Category': report_id,
                'Comment': 'Bullying and harassment'
            }
            response = requests.post(url, headers=headers, json=data)
            
            attempts = 0
            successful_attempts = 0
            failed_attempts = 0

            for _ in range(times):
                attempts = attempts + 1
                if response.ok:
                    successful_attempts = successful_attempts + 1
                    print(f"[+] User {username} reported ({attempts}/{times})")
                else:
                    print(f"[-] Failed to report {username}. Code {response.status_code} ({attempts}/{times})")
                    print(f"(Response: {response.text} on report {attempts})")
                time.sleep(report_interval)

            clearscreen()
            title('normal')
            print("[+] Log:")
            print(f"[+] Successful attempts: {successful_attempts}")
            print(f"[-] Failed attempts:     {failed_attempts}")
    elif choice == "2":
        clearscreen()
        title('normal')
        interval_set = False
        new_report_interval = input("[+] Enter new report interval (in seconds): ")
        try:
            float(new_report_interval)
            print("[+] Creating new dictionary...")
            try:
                config_dict = modules.config.update('config.json', 'interval', new_report_interval)
                parsed_config = modules.config.parse('config.json')
                clearscreen()
                title("normal")
            except Exception as e:
                clearscreen()
                title("normal")
                print(f"[-] Exception occurred while changing interval: {e}")
                choices("square_brackets", menuchoices)
        except ValueError:
            print('[-] Invalid interval')
    elif choice == "5":
        print("\n[+] Bye!")
        break