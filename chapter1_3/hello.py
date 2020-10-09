# This program says hello and asks users for my name

print('Hello World')

print('What is your name?')  # ask for user's name
myName = input()

print('It is good to meet you,', myName)

#Return the length (the number of items) of an object. The argument may be a sequence 
# (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set)
print('The length of your name is:', len(myName))


print('What is your age?')   # ask for user's age
myAge = input()


print('You will be ' + str(int(myAge) + 1) + ' next year!')
