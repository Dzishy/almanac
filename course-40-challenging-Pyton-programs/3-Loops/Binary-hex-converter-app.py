
print ('Welcome to Binary / Hexadecimal Converter App')
maxNumber = int(input ('Compute binary and hexadecimal values up to the following decimal number: '))

decimal = list(range(1, maxNumber+1))
binary = []
hexadec = []

for i in range (1, maxNumber+1):
    binary.append(bin(i))
    hexadec.append(hex(i))
print ('Generating lists...Complete!\nUsing slices we will now show a portion of each list.')
start = int(input ('What decimal number would you like to start at: '))
stop = int(input ('What decimal number would you like to stop at: '))
print (decimal, binary, hexadec)

print (f'\nDecimal values from {start} to {stop}:')
for num in decimal[start-1:stop]:
    print(num)
print (f'\nBinary values from {start} to {stop}:')
for num in binary[start-1:stop]:
    print(num)
print (f'\nHexadecimal values from {start} to {stop}:')
for num in hexadec[start-1:stop]:
    print(num)

input (f'\nPress Enter to see all values from {start} to {stop}.')
print ('Decimal----Binary----Hexadecimal')
print ('........................................................................')
for valDec, valBin, valHex in zip(decimal[start-1:stop], binary[start-1:stop], hexadec[start-1:stop]):
    print (f'{valDec}----{valBin}----{valHex}')
    