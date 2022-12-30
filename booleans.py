# Booleans and Comparisons: True or False Only
isLoggedIn = True

# Comparison Operators:
# == Equal to
13 == 3 # False
13 == 13 # True

# != Not equal to
13 != 3 # True
13 != 13 # False

# Truthy and Falsey:
# Falsey = 'False', 0.0, 0, None, range(0), Empty 
# anything: Empty String, Empty Data Structures [],
# {}, (), set()

# Truthy = Everthing Else!

# The 'in' Operator: Gives us a True or False value.
# Looks to see if an item is a member of a sequence.
'a' in 'cat' # True
'A' in 'hat' # False

# ord() - Lists the order of the value in the Unicode
# 'code point' (list).
print(ord('a')) # 97
print(ord('$')) # 36



# "Dollar Tree"
print("*********************")
i = 1
while i <= 13:
    print(i * '$')
    i = i + 1
