student_data = {
    "name": "John",
    "age": 15,
    "class": "10th",
    "city": "Patna",
    "gender": "male"
}

# print(student_data)
# print("name:", student_data["name"])

#Iteration in dictionary
for key in student_data:
    #print(key, ":", student_data[key]) #get ket and value both
    #print(key, ":", student_data.get(key))
    #print(key)  #get key only
    print(student_data[key]) # value only