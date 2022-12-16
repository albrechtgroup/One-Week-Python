# Strings wrapped in quotes, same as JS:
color = "purple"

url = "www.reddit.com/r/formula1/"

# In Python, we can change types of variables:
age = 42
age = "forty-three"

# String Operator: 
# Concatination - Combine two strings
first_name = "Andrew"
last_name = "Albrecht"

full_name = first_name + " " + last_name 
# Print:
print(full_name)  # Andrew Albrecht

# Multiplication - Multiply a string by a Number
'ho' * 3 # 'hohoho'

# In Python, strings are 0 Based like JS! Yayyy
msg = "I <3 Cats"
 
msg[0] # 'I'
msg[5] # 'C"
msg[2] # '<'
msg[-1] # 's'

# None - Is a special value that denotes a lack of 
# value. Not the same as zero or an empty string.
# Python's version of 'null'
user = None

# String Slices:
msg[2:4] # '<3'

# txt = "Hello WORLD ! " * 33
# print(txt)

# Escape Characters:
# Newline - \n        # Tab - \t
# Double Quote - \"   # Single Quote - \'   
# Backlash - \\

# Strings and Functions:

# Arguments = Fancy word for inputs

# the Len() function - will return the lenth of whatever
# item we pass to it. Excluding numbers.
word = "Chicken"
len(word) # 7

# the input() function - will prompt a user to enter 
# some input, converts it into a string, then returns it.
age = input("How old are you?")

first_name = input("What is your first name?")
last_name = input("What is your last name?")
 
full_name = first_name + " " + last_name
print("Hi there " + full_name)

# Type Casting:

# Age Calculator: 
age = input("How old are you in years?")
days = float(age) * 365
print(days)

# 'F' Strings - are an easy way to generate strings
# that contain interpolated expressions. Any code 
# between Curly braces {} will be evaluated and then
# the result will be turned into a string and inserted
# into the overall string.
f"there are {24*60*60} seconds in a day."
# "there are 86400 seconds in a day."
print(f"You are {days} days old!!")

# Shopping Cart Exercise:
print("WELCOME TO THE USELESS STORE")
print("*" * 23)
item = input("What item are you purchasing? ")
price = float(input(f"What is the price of {item}? "))
quantity = float(input(f"How many {item} are you buying? "))
print(f"Added {quantity} {item}(s) to shopping cart.")
print(f"Subtotal is: ${price * quantity}")

