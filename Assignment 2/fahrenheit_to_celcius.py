#prompts the user for a temperature in Fahrenheit
fahrenheit = float(input("Please enter a degree in fahrenheit: "));

#performs the conversion to Celsius
celsius = (fahrenheit - 32) * 5/9;

#generates output of temperature conversion
print(f'{fahrenheit: .1f} degrees fahrenheit is {celsius: .2f} degrees celsius');

