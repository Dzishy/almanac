print ('Welcome to the Basketball Roster Program!')

players = []

pointGuard = input ('Who is your point quard?').title()
players.append(pointGuard)
shootGuart = input ('Who is your shooting quard?').title()
players.append(shootGuart)
smallForw = input ('Who is your small forward?').title()
players.append(smallForw)
powForw = input ('Who is your power forward?').title()
players.append(powForw)
center = input ('Who is your center?').title()
players.append(center)

print (players)

print (f'\tYour starting {len(players)} for the upcoming bascetball season')
print (f'\t\tPoint Guard: \t{players[0]}')
print (f'\t\tShoot Guard: \t{players[1]}')
print (f'\t\tSmall Forward: \t{players[2]}')
print (f'\t\tPower Forward: \t{players[3]}')
print (f'\t\tCenter: \t{players[4]}')

p2 = players.pop(2)
print (f'\nOh no, {p2} is injured\nYour roster has only {len(players)} players.')
change = input (f"Who will take {p2}'s spot?").title()
players.insert(2,change)

print (f'\tYour starting {len(players)} for the upcoming bascetball season')
print (f'\t\tPoint Guard: \t{players[0]}')
print (f'\t\tShoot Guard: \t{players[1]}')
print (f'\t\tSmall Forward: \t{players[2]}')
print (f'\t\tPower Forward: \t{players[3]}')
print (f'\t\tCenter: \t{players[4]}')

print (f'\nGood luck {change}! You will do great!')
print (f'Your roster has  {len(players)} players.')