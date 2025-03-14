a = ["tata", "maruti", "toyota", "honda"]

#to create a copy of list
b = []
print(b)
b = a.copy()
print(b)
#to access an element
print(a.index("toyota"))
#to extend the list
c = ["patna", "ranchi"]
a.extend(c)
print(a)
#to reverse the list
a.reverse()
print(a)
#to sort the list
a.sort()  #sort() means arrange alphabetical orders
print(a)

d = [1, 12, 3, 9, 8, 6, 7, 11, 2]
d.sort()
print(d)

#to clear all the data from the list
a.clear()
print(a)