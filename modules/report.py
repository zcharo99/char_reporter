import requests

def reportuser(reportid: int, userid: str, cookie: str):
    url = 'https://report.roblox.com/v2/report'
    headers = {
        'Cookie': f'.ROBLOSECURITY={cookie}',
        'Content-Type': 'application/json'
    }
    data = {
        'UserID': userid,
        'Category': reportid,
        'Comment': 'Bullying and harassment'
    }
    print('[+] Sending report...')
    response = requests.post(url, headers=headers, json=data)

    if response.ok:
        print("[+] User reported successfully!")
    else:
        print(f"[-] Failed to report user. Code {response.status_code}")
        print(f"[-] Response: {response.text}")
