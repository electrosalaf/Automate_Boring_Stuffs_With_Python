import sys

while True:
    print('Enter exit to exit from the program.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed', response, 'as your response.')