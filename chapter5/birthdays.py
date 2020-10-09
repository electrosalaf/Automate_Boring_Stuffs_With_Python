birthdays = {'Ibrahim': 'Mar 27, 1996', 'Aliyy': 'Mar 30, 1999', 'Sherif': 'Jan 06, 2001'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name], 'is the birthday of', name)
        # If the name is in the dictionary, you access the associated value using square brackets
    else:
        print('I do not have information for ', name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated')
# note that all the data you updated is deleted when the program terminates 