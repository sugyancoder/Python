#type casting = The process of converting a value of one data type to another
#(string, integer, float, boolean)
#Explicit vs Implicit

name = "Sugyan Lama"
age = 16
student = True

print(type(name))
print(type(age))
print(type(student)) 

age = float(age)
print(age)

student = str(student)
print(student)

name = bool(name)
print(name)