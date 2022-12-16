# Methods: Are fuctions that "Live" on objects.
# thing.method()
# Methods automatically have access to the objects
# they are called on.

first_name = "Andrew"
last_name = "Albrecht"
full_name = first_name + " " + last_name
print(full_name)

# String Methods:
# lower() - lowercases all of the string:
print(full_name.lower())

msg = "heLLo wOrld"
# capitalize() - capatalizes the First letter only:
print(msg.capitalize())
# upper() - uppercases all of the string:
print(msg.upper())

# 'msg' string is unchanged*
print(msg)

# Best Python Documentation source for the language.
# "The Python Standard Library" link below*
# docs.python.org/3/library

# str.strip():
"-----Hello ----".strip("-") # 'Hello'

# str.replace(old, new, [count])
# 'old' and 'new' are required*
races = "3Kilometers 5Kilometers 10Kilometers 20Kilometers"
print(races)
# 'races' is unchanges from .replace(), so we save it 
# to a new variable to change and call it*
abr_races = races.replace("Kilometers", "Km")
print(abr_races)

# Chaining String Methods:
email = "TODD@FranklinVenture.com  "
clean_email = email.strip().lower()
print(clean_email)

# Press Release Exercise*
press_release = """

Doody Calls, a nationwide leader in dog poop removal 
services, is growing its footprint in the pooper scooper
industry with the opening of an office in Orlando, Florida.
Doody Calls currently cleans up dog poop in over 57 
territories across 23 states and has been named the 
number-one dog poop removal franchise in the United
States by Entrpreneur Magazine's annual Franchise 500 
list.

"""

# Remove the leading and trailing white space (new 
# lines) from press_release.
press_release = press_release.strip()

# Replace the phrase "dog poop" with "pet waste"
# from press release. 
press_release = press_release.replace("dog poop", "pet waste")
press_release = press_release.replace("number-one", "#1")

# We changed our company name! Replace the phrase 
# "Doody Calls" with "DoodyCalls" (no space between the words) 
press_release = press_release.replace("Doody Calls", "DoodyCalls")

# Make the entire press release uppercase.
press_release = press_release.upper()

# Print out the updated press release with all of the
# above changes.
print(press_release)