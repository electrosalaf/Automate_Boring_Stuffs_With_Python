import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return  'Ask again later'
    elif answerNumber == 6:
        return  'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

r = random.randint(1,9)  # evaluates to a random number between 1 to 9 (including) and store the value in r
fortune = getAnswer(r)  # get answer function is called with argument r, moves to the top and value r stored in parameter answerNumber
print(fortune)

print(getAnswer(random.randint(1, 9)))  # alternative way
print('Hello ', end='')
print('World ', end='')
print('Wide ', end='')
print('Web')  # print function will merge the next line to it.

print('Dog', 'Cat', 'Mice')
print('Dog', 'Cat', 'Mice', sep=',')