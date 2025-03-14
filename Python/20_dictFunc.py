students = {
    "name": "John",
    "age": 16,
    "class": "10th",
    "roll_no": 20,
    "city": "Patna",
    "gender": "male"
}

# Functions are
#get() - returns the value of the specified key
#print(students.get("name"))

#items() - returns a list containing a tuple for each key value pair
#print(students.items())

#keys() - returns a list containing the dictionary's keys
#print(students.keys())

#values() - returns a list of all the values in the dictionary
#print(students.values())


#copy() - returns a copy of the dictionary
#print(students.copy())

#setdefault() - returns the value of the specified key. If the key does not exist: insert the key, with the specified value
#print(students.setdefault("name"))
# x = students.setdefault("roll_no", 22,)
# print(x)

#update() - updates the dictionary with the specified key-value pairs
#print(students.update({"name1": "Mohan"}))

#pop() - removes the element with the specified key
#print(students.pop("name"))

#popitem() - removes the last inserted key-value pair
#print(students.popitem())

#clear() - removes all the elements from the dictionary
#print(students.clear())
print(students)
