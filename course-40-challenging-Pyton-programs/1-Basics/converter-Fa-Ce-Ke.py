print('welcome to our mph to mps converter app.')



farenheit = float(input ('what is the temperature in Farenheit?\n'))
celsius = (farenheit-32)/1.8
kelvin = (farenheit+459.67)/1.8

print(f"Temperature in Farenheit is: {farenheit:.4f}\nTemperature in Celcius is: {celsius:.4f}\nTemperature in Kelvin is: {kelvin:.4f}")