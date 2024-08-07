from modules.menu import *
from modules.report import *
from modules.getuid import *
import modules.config
import platform
import os
import sys

menuchoices = ["Report User", "Generate Config", "Set Interval", "Exit"]

def clearscreen():
    if platform.system == "Windows":
        os.system('cls')
    else:
        os.system('clear')

print("[+] Parsing config and getting values...")

if not os.path.exists('config.rep') or os.path.getsize('config.rep') == 0:
    default_data = """\
Interval: 5;
ReportID: 5;
Cookie: "Unknown"
"""
    with open('config.rep', 'w') as file:
        file.write(default_data)

parsed_config = modules.config.parse_config('config.rep')

report_interval = modules.config.getvaluekey(parsed_config, 'Interval')
report_id = modules.config.getvaluekey(parsed_config, 'ReportID')

clearscreen()

title("normal")
choices("square_brackets", menuchoices)
choice = input("[+] Enter choice: ")
if choice == "1":
    print("wip")
elif choice == "4":
    print("[+] Bye!")
    sys.exit(1)