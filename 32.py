import json

data = {
    "name": "Aditya",
    "age": 21,
    "skills": ["Python", "JavaScript", "HTML"],
    "is_student": True,
    "address": {
        "city": "Mumbai",
        "pincode": 400001
    }
}

json_str = json.dumps(data, indent=4)
print("JSON String:")
print(json_str)

print()

parsed_data = json.loads(json_str)
print("Name:", parsed_data["name"])
print("City:", parsed_data["address"]["city"])
print("First Skill:", parsed_data["skills"][0])

print()

with open("student.json", "w") as f:
    json.dump(data, f, indent=4)
print("Data written to student.json")

with open("student.json", "r") as f:
    loaded = json.load(f)
print("Read from student.json:")
print("Name:", loaded["name"])
print("Skills count:", len(loaded["skills"]))

import os
os.remove("student.json")
print("student.json cleaned up")
