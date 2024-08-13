
# my way

print('welcome to our mph to mps converter app.')

mph = float(input ('what is your speed in mph?\n'))
mps = mph*0.44704

print(f"Your speed in mps is: {mps:.2f}")



# course way

print('welcome to our mph to mps converter app.')

mph = float(input ('what is your speed in mph?\n'))
mps = round(mph*0.44704, 2)

print(f"Your speed in mps is: {mps}")
round