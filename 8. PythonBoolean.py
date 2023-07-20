x = 5
y = 10

print(bool(x < y))
# print(x < y) will also print True

x = 5
y = 10

# it will print True. Because x has a non-zero value.
print(bool(x))

x = 0
y = 10

# it will print False. Because x has a value which is zero.
print(bool(x))

name = ""

# it will print False. Because name is an empty string.
print(bool(name))

name = "hridoy"

# it will print True. Because name is a non-empty string.
print(bool(name))
