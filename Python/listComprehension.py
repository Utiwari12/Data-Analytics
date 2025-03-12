l1 = [30, 40, 50, 60]

l2 = []

for i in l1:
    # if i > 42:
    #    l2.append(i)
    l2.append(i)
    
#print(l2)
print(l1, "\n", l2)

l3 = []
l3 = [i for i in l1]  #Comprehension method
print(l3)
l3 = [i for i in l1 if i>43]
print(l3)
    