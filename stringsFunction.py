#endswith()- returns true if the string ends with the specified value
a = "Hello Patna"
# print(a, a.endswith("Patna"))
# print(a, a.endswith("p"))
#startswith()- returns true if the string starts with the specified value
# print(a, a.startswith("H"))
# print(a, a.startswith("h"))

#swapcase()- returns a copy of the string with uppercase characters converted to lowercase and vice versa
#print(a, a.swapcase())

#strip()- returns a copy of the string with the leading and trailing characters removed
# b = "    Hello World    "
# print(b, b.strip())
# c = "  ******  Hello World  .......  "
# print(c, c.strip(" *, "))

#split()- returns a list where the string has been split at each separator
# print(a, a.split())
# print(a, a.split(" "))

# b = "#abcd#efgh#ijlk#mnop"
# print(b, b.split("#"))

#ljust()- returns a left justified version of the string
# print(a, a.ljust(20))
# print(a, a.ljust(20, "*"))
# x = a.ljust(20, "*")
# print(x,  "is my favourite city")

#rjust()- returns a right justified version of the string
#print(a, a.rjust(20)) #20 is left space
#print(a, a.rjust(20, "*"))

#replace()- returns a string where a specified value is replaced with a specified value
#print(a, a.replace("Patna", "Bihar"))

#rindex()- returns the index number of the last occurrence of the specified value
#print(a, a.rindex("P"))

#rfind()- returns the index number of the last occurrence of the specified value
print(a, a.rfind("t"))
print(a, a.find("na", 6, 15))