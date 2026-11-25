import json

users = [
    {"id": 101, "username": "aditya", "active": True, "score": 92.5},
    {"id": 102, "username": "rohan", "active": False, "score": 75.0},
    {"id": 103, "username": "priya", "active": True, "score": 88.0}
]

encoded = json.dumps(users, indent=2)
print("Encoded JSON:")
print(encoded)

print()

decoded = json.loads(encoded)
active_users = [u["username"] for u in decoded if u["active"]]
print("Active users:", active_users)

top_scorer = max(decoded, key=lambda u: u["score"])
print("Top scorer:", top_scorer["username"], "with", top_scorer["score"])

with open("users_cache.json", "w") as f:
    json.dump(decoded, f)

with open("users_cache.json", "r") as f:
    recovered = json.load(f)
print("Cached entries count:", len(recovered))

import os
os.remove("users_cache.json")
print("Cache file removed")
