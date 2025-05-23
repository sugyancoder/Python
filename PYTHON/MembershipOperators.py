# Membership operators = used to test whether a value or variable is found in a sequence

# EXAMPLE 1
word = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter in word:
   print(f"There is a {letter}")
else:
   print(f"{letter} was not found")

# EXAMPLE 2
students = {"Sugyan", "Patrick", "Sandy"}

student = input("Enter the name of a student: ")

if student in students:
   print(f"{student} is in this class")
else:
   print(f"{student} is NOT in this class")

# EXAMPLE 3
grades = {
   "Sandy": 'A',
   "Squidward": 'B',
   "Sugyan": 'A',
   "Patrick": 'D'
}

student = input("Enter the name of a student: ")

if student in grades:
   print(f"{student}'s grade is {grades[student]}.")
else:
   print(f"{student} is not in the dictionary")

# EXAMPLE 4
email = "sugyancoder@gmail.com"

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")