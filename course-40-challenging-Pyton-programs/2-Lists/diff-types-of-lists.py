print('\tSummary table')


numStrings = ['15', '100', '55', '45']
numInts = [15, 100, 55, 45]
numFloats = [2.2, 45.666, 6.0, 0.234564]
numLists = [[1,2,3], [4,5,6], [7,8,9]]

print (f'\nThe variable numStrings is a {type(numStrings)}.')
print (f'It contains the elements: {numStrings}')
print (f'The element {numStrings[0]} is a {type(numStrings[0])}.')

print (f'\nThe variable numInts is a {type(numInts)}.')
print (f'It contains the elements: {numInts}')
print (f'The element {numInts[0]} is a {type(numInts[0])}.')

print (f'\nThe variable numFloats is a {type(numFloats)}.')
print (f'It contains the elements: {numFloats}')
print (f'The element {numFloats[0]} is a {type(numFloats[0])}.')

print (f'\nThe variable numLists is a {type(numLists)}.')
print (f'It contains the elements: {numLists}')
print (f'The element {numLists[0]} is a {type(numLists[0])}.')

print('\nNow sorting numStrings and numInts...')
print(f'Sorted numStrings: {sorted(numStrings)}')
print(f'Sorted numInts: {sorted(numInts)}')

print('\nStrings are sorted alphabetically while strings are sorted numerically!')