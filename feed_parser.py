import requests
import json

# Simple OSINT Feed URLs (example)
feeds = {
    "CIRCL": "https://iplists.firehol.org/files/firehol_level1.netset",
    "Botvrij": "https://rules.emergingthreats.net/blockrules/emerging-drop.suricata.rules"
}

parsed_data = {}

for name, url in feeds.items():
    print(f"[+] Fetching feed: {name}")
    response = requests.get(url)
    data = response.text.splitlines()
    parsed_data[name] = data[:20]  # sample first 20 entries

# Save unified output
with open("unified_feeds.json", "w") as out:
    json.dump(parsed_data, out, indent=4)

print("[+] Feeds parsed and saved to unified_feeds.json")
