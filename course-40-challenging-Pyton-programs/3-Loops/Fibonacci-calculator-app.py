

print ('Welcome to the Fibonacci Calculator App')

digits = int (input ('How many of the Fibonacci sequence would you like to compute: '))

sequence = [1,1]
for i in range (digits-2):
    f = sequence[i] + sequence[i+1]
    sequence.append(f)

print (f'The first {digits} numbers of the Fibonacci sequence are:')
for f in sequence:
    print (f)

golden = []
for i in range (digits-1): # -1 потому что в последнем проходе не будет i+1
    ratio = sequence[i+1]/sequence[i]
    golden.append(ratio)

print ('\nThe corresponding Golden Ratio values are: ')
for r in golden:
    print (r)