def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1

print('Enter a number: ')
userEntry = int(input())
newEntry = collatz(userEntry)
print(collatz(userEntry))
while collatz(newEntry) > 1:
    print(collatz(newEntry))


