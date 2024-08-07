import requests

def getuid(username: str):
    url = 'https://users.roblox.com/v1/usernames/users'
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'usernames': [username]
    }
    
    print("[+] Fetching user ID...")
    response = requests.post(url, headers=headers, json=data)
    
    if response.ok:
        user_data = response.json()
        if user_data['data']:
            print("[+] User ID fetched!")
            return user_data['data'][0]['id']
        else:
            print("[-] User not found")
            return None
    else:
        print(f"[-] Failed to fetch user ID. Code {response.status_code}")
        return None