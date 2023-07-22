# if we don't assign the below string to a variable, then it will be
# considered as a multiline comment.
"""
This is a
multiline comment
"""

# if we assign the below string to a variable, then it will be
# considered as a multiline string and we will be able to print it.
text = """
This is a 
multiline string.
"""

print(text)
