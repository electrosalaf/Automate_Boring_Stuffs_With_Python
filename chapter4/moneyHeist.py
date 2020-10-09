heistMen = ['Professor', 'Helsinki', 'Oslo', 'Rio', 'Palermo', 'Nairobi', 'Tokyo', 'Denver', 'Berlin', 'Moscow']
print('Have You Watched Money Heist?  ', end='')
print('If yes,then state the name of any gang member that robbed the Royal Mint in Spain.')
name = input()
if name not in heistMen:
    print('You probably did not watch the movies coz', name, 'is not a robber ')
elif name == 'Professor':
    print('Though, Professor is a cast but was not in the mint ')
else:
    print(name, ' is a cast in money heist')