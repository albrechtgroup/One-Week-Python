# Conditionals:
# age = input("How old are you? ")
# age = int(age)

# if age >= 21: 
#     print("Welcome, Come on in.")
# else:
#     print("Get Out of here, before I call the Police!")
# print("AFTER the 'if' statement")

# My Bartender Code:
age = input("Hello, How old are you? ")
age = int(age)

if age > 18 and age < 21:
    print("Im sorry, you must be 21 to enter.")
elif age >= 21 and age < 65:
    print("Welcome! Come on in!")
elif age >= 65:
    print("Welcome. You get a Senior Discount today!!!")
else:
    print("Get the HELL out of here before I call your Parents!!!")
    print("Go*^ Da^% Kids!!!")
print("************************")
print("AFTER the 'if' statement")
