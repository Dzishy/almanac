print('Welcome to Favourite Teachers Program!')

favTeachers = []

favTeachers.append(input('\nWho is your first favourite teacher: ').title())
favTeachers.append(input('Who is your second favourite teacher: ').title())
favTeachers.append(input('Who is your third favourite teacher: ').title())
favTeachers.append(input('Who is your forth favourite teacher: ').title())

print (f'\nYour favourite teachers ranked are: {favTeachers}')
print (f'Your favourite teachers alphabetically are: {sorted(favTeachers)}')
print (f'Your favourite teachers in reverse alphabetical order are: {sorted(favTeachers, reverse=True)}')

print (f'\nYour top two teachers are: {favTeachers[0]} and {favTeachers[1]}.')
print (f'Your next two favourite teachers are: {favTeachers[2]} and {favTeachers[3]}.')
print (f'Your last favourite teacher is: {favTeachers[-1]}.')
print (f'You have a total of {len(favTeachers)} favourite teachers.')

print (f'\nOoops, {favTeachers[0]} is no longer your favourite teacher.',end=" ")
favTeachers.insert(0, input ('Who is your new favourite teacher:').title())

print (f'\nYour favourite teachers ranked are: {favTeachers}')
print (f'Your favourite teachers alphabetically are: {sorted(favTeachers)}')
print (f'Your favourite teachers in reverse alphabetical order are: {sorted(favTeachers, reverse=True)}')

print (f'\nYour top two teachers are: {favTeachers[0]} and {favTeachers[1]}.')
print (f'Your next two favourite teachers are: {favTeachers[2]} and {favTeachers[3]}.')
print (f'Your last favourite teacher is: {favTeachers[-1]}.')
print (f'You have a total of {len(favTeachers)} favourite teachers.')

print (f"\nYou've decided you no longer like a teacher.",end=" ")
favTeachers.remove (input ('Which teacher would you like to remove from the list:').title())

print (f'\nYour favourite teachers ranked are: {favTeachers}')
print (f'Your favourite teachers alphabetically are: {sorted(favTeachers)}')
print (f'Your favourite teachers in reverse alphabetical order are: {sorted(favTeachers, reverse=True)}')

print (f'\nYour top two teachers are: {favTeachers[0]} and {favTeachers[1]}.')
print (f'Your next two favourite teachers are: {favTeachers[2]} and {favTeachers[3]}.')
print (f'Your last favourite teacher is: {favTeachers[-1]}.')
print (f'You have a total of {len(favTeachers)} favourite teachers.')