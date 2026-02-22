import json
x = '{"name":"Zareh", "Age": "12", "City": "Boca"}'
#Json
y = json.loads(x)
# # Converts Json to dictionary
# print(y["Age"])

x = {
    "Name":"Zareh",
    "Age" : "12",
    "City": "Boca"
}
y = json.dumps(x)
# print(y)