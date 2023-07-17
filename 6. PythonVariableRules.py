import keyword

# keyword.kwlist will return all the keywords for the present
# python version
keywordList = keyword.kwlist
print(keywordList)

# keyword.iskeyword() checks if the argument passed in it as a string
# is a keyword or not. It will return boolean value.
print(keyword.iskeyword("notry"))
