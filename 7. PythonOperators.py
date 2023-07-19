# Identity operator
# Identity operator is used for checking if the objects are
# similar or not. It will not compare the elements, only the objects
# which is actually the address in the memory. If two objects are in
# same address in the memory, then they are identical objects.

a = ["raihanul", 31]
b = ["raihanul", 31]

# it will return false, because a and b are two lists that are in
# different addresses in the memory. It will not compare the elements
# in the list
print(a is b)

# it will return true, because a and b are two lists that are in
# different addresses in the memory. It will not compare the elements
# in the list
print (a is not b)

# it will return true, because the "==" operator is used for comparing
# elements in the list. It checks the elements on both the list are equal.
# That's why it return true
print(a == b)


# =======================================================================================================

# Bitwise operators

# 0 - 00
# 1 - 01
# 2 - 10
# 3 - 11

x = 0
y = 1

# Bitwise AND
# 0 0
# 0 1
# -------
# 0 0 ---> 0
# it will print 0
print(x & y)

x = 1
y = 3

# 0 1
# 1 1
# -------
# 0 1 ---> 1
# it will print 1
print(x & y)

# Bitwise OR

x = 1
y = 3

# 0 1
# 1 1
# -------
# 1 1 ---> 3
# it will print 3
print(x | y)
