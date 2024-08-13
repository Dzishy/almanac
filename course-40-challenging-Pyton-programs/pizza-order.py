import inquirer

small= 8
medium = 10
large = 12

thin = 0
thick = 2

cheese = 1
pepperoni = 1.5
mushrooms = 1
olives = 1

size = ["small","medium","large"]
dough = ["thin", "thick"]

print ("Welcome to our pizzeria!")
questions = [
    inquirer.List (name="size",message="choose the size", choices=size),
    inquirer.List (name="dough",message="choose the dough", choices=dough)
    ]
answers = inquirer.prompt (questions)
userInput = input("print the ingredients of your choice (cheese, perreroni, mushrooms, olives) \n")
print ((f"you chose: {answers["size"]} pizza with "), userInput, " on ", (f"{answers["dough"]} dough"))
print (f'you chose: {answers['size']} pizza with {userInput} on {answers['dough']} dough')

totalCost = 0

if answers["size"] == "small":
    totalCost +=  small
elif answers["size"] == "medium":
    totalCost += medium
elif answers["size"] == "large":
    totalCost += large

if answers["dough"] == "thin":
    totalCost += thin
elif answers["dough"] == "thick":
    totalCost += thick

if userInput == "cheese":
    totalCost += cheese
elif userInput == "pepperoni":
    totalCost += pepperoni
elif userInput == "olives":
    totalCost += olives
elif userInput == "mushrooms":
    totalCost += mushrooms

print ("Total cost: $",totalCost)