myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet named', name)
else:
    print(name, 'is my pet.')
cat = ['fat', 'black', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]
# Or
size, color, disposition = cat  #  The number of variables and the length of the list must be exactly equal to avoid ValueError

