
print ('Welcome to the Shipping Accounts Program')

users = ['DianaS', 'AlexR', 'Emim', 'dio']
username = input ('Enter your username: ')
price1 = 5.10
price2 = 5.00
price3 = 4.95
price4 = 4.80

if username in users:
    print ('Welcome back to your account.')
    print ('\nCurrent shipment prices are as follows:')
    print (f'Shipping orders 0 to 99:\t${price1} each')
    print (f'Shipping orders 100 to 499:\t${price2} each')
    print (f'Shipping orders 500 to 999:\t${price3} each')
    print (f'Shipping orders over 1000:\t${price4} each')
    numItems = int(input ('\nHow many items would you like to ship: '))
    if numItems < 100:
        price = price1
    elif numItems < 500:
        price = price2
    elif numItems < 1000:
        price = price3
    else:
        price = price4
    result = round (numItems*price, 2)
    print (f'To ship {numItems} it will cost you {result} at {price} per item.')
    answer = input ('Would you like to place this order (y/n): ').lower()
    if answer == 'y':
        print (f'Okay. Shipping your {numItems} items.')
    else:
        print ('Okay, no order is being placed this time.')
else:
    print('Sorry, you do not have an account with us. Goodbye.')


