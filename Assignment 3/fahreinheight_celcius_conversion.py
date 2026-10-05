#Named Constants for Fahrenheit and Celsius
FAHRENHEIT_TYPE = "F"
CELSIUS_TYPE = "C"

#prompts the user for temperature and type
weather_num = float(input("Enter the temperature you want to convert: "))

weather_type = str(input("Enter the type of temperature (F for Fahrenheit, C for Celsius): "))

#performs conversion to celsius and generates output
if weather_type == FAHRENHEIT_TYPE:
    if weather_num > -459.67:
        celsius = (weather_num - 32) * 5/9
        print(f'The temperature in Celsius is: {celsius: .2f}')
    else:
        print('Invalid temperature. Please enter a temperature above absolute zero.') 

#performs conversion to fahrenheit and generates output
elif weather_type == CELSIUS_TYPE:
      if weather_num > -273.15:
             fahrenheit = (weather_num * 1.8) + 32
             print(f'The temperature in Fahrenheit is: {fahrenheit: .2f}')
      else:
             print('Invalid temperature. Please enter a temperature above absolute zero.') 

#prompts user for invalid type 
else: print("Invalid temperature type. Please enter 'F' for Fahrenheit or 'C' for Celsius.") 
