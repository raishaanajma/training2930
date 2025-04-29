import json

with open("json-python.json", "r") as file:
    data = json.load(file)

print(data)