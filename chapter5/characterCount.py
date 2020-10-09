message = 'It was a raining day in September, and the clocks were stricken thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)
