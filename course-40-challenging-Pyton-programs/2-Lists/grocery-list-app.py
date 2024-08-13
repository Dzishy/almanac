from datetime import datetime

now = datetime.now()
formatedDayTime = now.strftime('%d/%m %H:%M')

print ('Welcome to the Grocery List App')
print(f'Current date and time: {formatedDayTime}')

groceryList = ['Meat','Cheese']

print (f'You currently have {groceryList[0]} and {groceryList[1]} in your list')

for i in range(3):
    item = (input ('Type of food to add to grocery list:')).title()
    groceryList.append (item)

print (f'\nHere is your grocery list:\n{groceryList}')
groceryList.sort()
print (f'Here is your grocery list sorted: \n{groceryList}')

for i in range(3):
    print (f'\nCurrent grocery list: {len(groceryList)} items\n{groceryList}')
    purchase = (input('What did you just buy:')).title()
    print (f'Removing {purchase} from the list...')
    groceryList.remove(purchase)

ramainingItem = groceryList.pop()
print (f'\nSorry, the store is out of {ramainingItem}')
newItem = (input('What would you like instead?')).title()
groceryList.insert(0,newItem)
print(f'\nHere is what remains in your grocery list: {groceryList}')