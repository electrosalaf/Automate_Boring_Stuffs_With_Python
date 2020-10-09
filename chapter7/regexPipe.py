import re

'''Matching Multiple Groups with the Pipe
This will return either Batman or Tina Fey and the first occurrence in the matching text will be returned as the matching object'''
heroRegex = re.compile(r'Batman|Tina Fey.')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())  # returns Batman the first occurrence

mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())  # returns Tina Fey the first occurence

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))


# the following lines does optional matching
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

'''letting the regex look for  phone numbers that  do or do not have area code by making the area code optional
the '#' actually matches nothing or one of the group preceeding this question mark '''

phoneNumbRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d\d')
mo1 = phoneNumbRegex.search('My phone number is 234-602-06819')
print(mo1.group())

mo2 = phoneNumbRegex.search('My phone number is 602-06819')
print(mo2.group())

'''Matching zero or more with asterisk'''

batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventure of Batwoman')
print(mo2.group())

mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())

'''Matching one or more with plus '+' '''
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())

'''mo3 = batRegex.search('The Adventures of Batman')
print(mo3.group())
The above statement will not match because atleast one word of wo must be in our definition'''

'''Matching Specific Repetitions with Curly Brackets'''
haRegex = re.compile(r'(Ha){0,3}')  # specifying the bounds
mo1 = haRegex.search('HaHaHa')
print(mo1.group())

'''Writing somethng like what am about to write below will not work, this should give an attribute error since Ha is to be matched atleast trice'''
mo2 = haRegex.search('Ha')
print(mo2.group())

'''Greedy and  NonGreedy Match'''
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

nonGreedyHaRegex = re.compile(r'(Ha){3,5}?')  # following the curly bracket with a question mark does the nongreedy match
mo2 = nonGreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())

# Never forget that the question mark in regular expression could mean a nongreedy match or an optional matchd

'''The findall() method do not just return the first match text but returns a list of every string that matches our definition'''

phoneNumbRegex = re.compile(r'\D\d\d\d-\d\d\d-\d\d\d\d\d') # has no groups
mo1 = phoneNumbRegex.search('Cell:+234-602-06819  Work: +234-178-59562')
print(mo1.group())

mo2 = phoneNumbRegex.findall('Cell:+234-602-06819  Work: +234-178-59562')
print(mo2)  # As long as there are no groups in the regular expression

phoneNumbRegex = re.compile(r'(\D\d\d\d)-(\d\d\d)-(\d\d\d\d\d)')  # has groups
mo3 = phoneNumbRegex.findall('Cell:+234-602-06819  Work: +234-178-59562')  #returns list of tuples
print(mo3)

# Character Classes
xmasRegex = re.compile(r'\d+\s\w+')
''' The findall() method returns all matching strings of the regex pattern in a list.'''
mo1 = xmasRegex.findall('12 drummer, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(mo1)

# Making Your Own Character Classes
vowelRegex = re.compile(r'[aeiouAEIOU]')  # defining your own characters using square brackets
mo1 = vowelRegex.findall('Robocop eats baby food. BABY FOOD.')  # will match any vowel both upper case and lower case
print(mo1)

consonantRegex = re.compile(r'[^aeiouAEIOU]')  # Placing ^ will make a negative character class
mo2 = consonantRegex.findall('Robocop eats baby food. BABY FOOD')  # matching every character that is not a vowel
print(mo2)

#The Caret and Dollar Sign Character
beginsWithHello = re.compile(r'^Hello')
mo1 = beginsWithHello.search('Hello World!')
print(mo1)
mo2 = beginsWithHello.search('He said hello.')
print(mo2)  # the text does not begin with a Hello, so it returns none

endsWithHello = re.compile(r'\d$')  # matches string that ends with numeric character 0-9
mo1 = endsWithHello.search('My age is 23')
print(mo1)
mo2 = endsWithHello.search('My age is twenty three')
print(mo2)  # since the string is not ending with a number it returns none

wholeStringIsNum = re.compile(r'^\d+$')
mo1 = wholeStringIsNum.search('1234567890')
print(mo1)

mo2 = wholeStringIsNum.search('1234xyz567890')
print(mo2)

# The Wildcard Character
'''The  wildcard character will match any character except for a newline and note that it will only match one character'''
atRegex = re.compile(r'.at')
mo1 = atRegex.findall('The cat in the hat sat on the flat mat')
print(mo1)

# Matching Everything with Dot-Star
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')  # note that dot-star is greedy, will always want to match as much as possible
mo = nameRegex.search('First Name: Ibrahim Last Name: Lawal')
print(mo.group(1))
print(mo.group(2))
print(mo.group())

# For the nongreedy mode:
nonGreedyRegex = re.compile(r'<.*?>')
mo = nonGreedyRegex.search('<To serve man> for dinner.>')  # matches the shortest possible strings
print(mo.group())

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')  # matches the longest possible strings
print(mo.group())

# Making Newlines with the Dot Character
'''The dot-star will match everything except newline. By passing re.DOTALL to the re.compile you match everything including newline too'''
noNewLineRegex = re.compile(r'.*')
nonGreedyHaRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()

newLineRegex = re.compile('.*', re.DOTALL)
newLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()

# case insensitive matching, regular expresssions matches texts with the case specified
regex1 = re.compile('ROBOCOP')
regex2 = re.compile('robocop')
regex3 = re.compile('ROBOcop')

# to make it case insensitive you can pass in re.IGNORE or re.I as second arguement to the re.compile

robocop = re.compile(r'robocop')
robocop.search('RoboCop is part man, part machine')