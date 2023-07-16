x = 42
# id is the identifier of the object that is passed as argument
# basically it returns the address of the argument from the memory
print(id(x))

y = 42
print(id(y))

# if many variable possess the same integer value, then
# their identifier should also be the same. Because they all
# are pointing to the same integer object in the memory

x = 600
print(id(x))

y = 900
print(id(y))

# the values are different, so the identifiers or the addresses in the memory
# are also different.
