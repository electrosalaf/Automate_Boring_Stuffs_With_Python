while True:
    print('Enter your age: ')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')

spam = '''Dear Mum,
How have you been? I am fine.
There is a container in the fridge that is labelled 'Milk Experiment'

Please do not drink it.
Sincerely,
Ibrahim'''
spam.split('\n')  # will return a split list anywhere it comes across a new line
print(spam)