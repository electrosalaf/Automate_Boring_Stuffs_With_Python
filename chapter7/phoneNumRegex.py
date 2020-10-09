import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 234-906-020-6819')

areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

# Next line of code contains the group() method which returns actual matched text from the string.
#  calling method group on variable mo to return the match