#1. Convert the folowing dictionary into JSON format
import json
student_data = { "name": "John", "age": 30, "city": "New York" }
data = json.dumps(student_data)
print(data, type(data))
#2. Convert the following list into JSON format
# a = ["apple", "banana", "cherry"]
# b = json.dumps(a)
# print(b, type(b))
#3. Convert the following tuple into JSON format
# c = ("apple", "banana", "cherry")
# d = json.dumps(c)
# print(d, type(d))

#4. access the value of key "name" from the following JSON string
# e = '{"name": "John", "age": 30, "city": "New York"}'
# f = json.loads(e)
# print(f["name"], type(f["name"]))

#5. Pretty print the following JSON string
# g = '{"name": "John", "age": 30, "city": "New York"}'
# h = json.loads(g)
# print(json.dumps(h, indent=4, separators=(",", " = "))) #indent is used for spacing

#6.sort the following JSON keys and write it to a file
# i = '{"name": "John", "age": 30, "city": "New York"}'
# j = json.loads(i)
# print(json.dumps(j, sort_keys=True, indent=4))

#7. Access the nested key "address" from the following JSON string
k = """{
    "student": {
        "grade": {
            "name": "David",
            "address": {
                "street": "123 Main St",
                "city": "New York",
                "state": "NY"
            }
        }
    }
    }"""
    
data = json.loads(k)
print(data["student"]["grade"]["address"])