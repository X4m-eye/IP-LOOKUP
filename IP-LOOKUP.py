#!/usr/bin/env python3

import requests
import time



#   Information About This Tool

#   Author          :           X4m-Eye
#   Tool's Name     :           IP-LOOKUP
#   Description     :           IP-Lookup is a tool that can be used to retrieve information about an IP address.
#   Warning         :           I created this tool solely for educational purposes. This means I do not take any responsibility for your actions.




def autor_tool():
    print("\n\n\n\n\n")
    print("""
_____       _____      ____      ____                ______       ______                                      ____________       ____           ____       ____________
\    \     /    /     |    |    |    |              /      \     /      \                                    |            |     |    |         |    |     |            |
 \    \   /    /      |    |    |    |             /        \   /        \                                   |     _______|     |    |         |    |     |     _______|
  \    \_/    /       |    |    |    |            /    /\    \_/    /\    \             _______________      |    |              \    \ ______ /    /     |    |
   \         /        |    |____|    |           /    /  \         /  \    \           |               |     |    |_______        \                /      |    |_______
    |       |         |              |          /    /    \       /    \    \          |_______________|     |            |        \____      ____/       |            |
    |       |         |_________     |         /    /      \_____/      \    \                               |     _______|             |    |            |     _______|
   /    _    \                  |    |        /    /                     \    \                              |    |                     |    |            |    |
  /    / \    \                 |    |       /    /                       \    \                             |    |_______              |    |            |    |_______
 /    /   \    \                |    |      /    /                         \    \                            |            |             |    |            |            |
/____/     \____\               |____|     /____/                           \____\                           |____________|             |____|	     	  |____________|
""")

def tool_logo():
    print("\n\n\n\n\n")
    print("""
 _____       _________                               ____                  ________             ________          ____    _____      ____      ____       _________
|     |     |         \                             |    |                /        \           /        \        |    |  /    /     |    |    |    |     |         \    
|     |     |   ____   \                            |    |               /   ____   \         /   ____   \       |    | /    /      |    |    |    |     |   ____   \   
|     |     |  (    )   |                           |    |              /   /    \   \       /   /    \   \      |    |/    /       |    |    |    |     |  (    )   |
|     |     |  (____)   |      _______________      |    |             |   /      \   |     |   /      \   |     |         /        |    |    |    |     |  (____)   |
|     |     |          /      |               |     |    |             |  |        |  |     |  |        |  |     |        /         |    |    |    |     |          /
|     |     |    _____/       |_______________|     |    |             |  |        |  |     |  |        |  |     |        \         |    |    |    |     |    _____/
|     |     |    |                                  |    |             |   \      /   |     |   \      /   |     |         \        |    |____|    |     |    |
|     |     |    |                                  |    |_______       \   \____/   /       \   \____/   /      |    |\    \       |              |     |    |
|     |     |    |                                  |            |       \          /         \          /       |    | \    \       \            /      |    |
|_____|     |____|                                  |____________|        \________/           \________/        |____|  \____\       \__________/       |____|
""")

def get_location(ip_address):
    try:
        response = requests.get(f'https://ipinfo.io/{ip_address}/json')
        data = response.json()
        return data
    except requests.RequestException as e:
        print("Fehler beim Abrufen der Lokalisierung:", e)
        return None

def main():
    
    autor_tool()
    
    time.sleep(1)
    
    tool_logo()
    
    ip_address = input("Enter the IP address you want to check: ")
    
    location_data = get_location(ip_address)
    if location_data:
        print("Geographical data for IP address:", ip_address)
        print(f"Country: {location_data.get('country', 'N/A')}")
        print(f"Region: {location_data.get('region', 'N/A')}")
        print(f"City: {location_data.get('city', 'N/A')}")
        print(f"Postal Code: {location_data.get('postal', 'N/A')}")
        print(f"Coordinates: {location_data.get('loc', 'N/A')}")
    else:
        print("Localization information could not be retrieved.")

if __name__ == "__main__":
    main()
