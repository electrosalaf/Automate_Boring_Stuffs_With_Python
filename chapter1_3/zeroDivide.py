def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(10))
print(spam(0))
print(spam(1))

'''def spam(divideBy):
    return 42 / divideBy

try:
    print(spam(2))
    print(spam(10))
    print(spam(0))
    print(spam(1))  will not run, once the program into exception, it does not return to back to the clause to try it

except ZeroDivisionError:
    print('Error: Invalid argument')'''
