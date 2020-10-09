spam = 43
spam = spam + 1  # return 44

#  This augmented assignment
spam = 42
spam += 1
spam = 'Hello'
spam += 'World' # will return hello world.


# calling a method
spam = ['hello', 'hi', 'howdy', 'hyper']
spam.index('hyper')

spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
spam.index('Pooka')  # since we have repetition, it returns the first appearance, returns 1

#Adding value to list with append and insert methods
spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
spam.append('Big Nose')  # adds argument to the end of the list

spam = ['Cat', 'Dog', 'Hen']
spam.insert(2, 'Cow')  # insert cow at index 2

spam.remove('Dog')  # applicable when you know value to remove
del spam[2]  # applicable when you know the index

# sorting a list can be done with method sort()
spam = ['Cat', 'Dog', 'Hen']
spam.sort()  # arrange list elements alphabetically
spam = [1, -0.34, 9, 0, 86, 0.34]
spam.sort()  # arrange in increasing order

# you can also sort the list in reverse order by passing the word True to keyword reverse
spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort(reverse=True)

# python sort uppercase before sorting lower case
spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort()

# if you want python to sort alphabetically irrespective uppercase, do this
spam = ['a', 'A', 'z', 'Z']
spam.sort(key=str.lower) # treat all item in the list as if they were lower case
spam