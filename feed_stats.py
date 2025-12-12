import json

with open("unified_feeds.json", "r") as f:
    data = json.load(f)

print("Feed Statistics Summary")
print("=======================")

total = 0

for feed, indicators in data.items():
    count = len(indicators)
    total += count
    print(f"{feed}: {count} indicators")

print("=======================")
print(f"Total Indicators Collected: {total}")
