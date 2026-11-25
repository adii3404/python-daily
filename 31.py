import re

log = "2026-11-25 10:45:00 [ERROR] Connection lost from IP 192.168.1.45 on port 8080"

ip_match = re.search(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", log)
if ip_match:
    print("Found IP address:", ip_match.group())

timestamp = re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", log)
if timestamp:
    print("Timestamp:", timestamp.group())

level = re.search(r"\[([A-Z]+)\]", log)
if level:
    print("Log Level:", level.group(1))

print()

raw_string = "Hello    World!   Python   is  super    clean."
normalized = re.sub(r"\s+", " ", raw_string)
print("Normalized text:", normalized)

print()

hashtags = "#python #learning_daily #code2026 #student"
tags = re.findall(r"#\w+", hashtags)
print("Extracted tags:", tags)
