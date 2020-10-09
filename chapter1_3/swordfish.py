while True:
    print('Who are you?')
    name = input()
    if name != 'Ibrahim':
        continue
    print('Hello, Ibrahim. What is your password?  hint(It is a fish)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
