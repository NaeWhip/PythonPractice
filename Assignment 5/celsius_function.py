#Global constants of temperature
FAHRENHEIT_TYPE = "F"
CELSIUS_TYPE = "C"
ABSOLUTE_ZERO_F = -459.67
ABSOLUTE_ZERO_CELSIUS = -273.15

# Main function that calls the functions and displays the conversion
def main():
    temperature_type = get_temperature_type()
    temperature = get_temperature(temperature_type)
    display_conversion(temperature_type, temperature)

# Prompts the user to enter the temperature type until a valid value is received.
def get_temperature_type():
    while True:
        temperature_type = str(input("Enter the type of temperature (F for Fahrenheit, C for Celsius): "))
        if temperature_type == CELSIUS_TYPE:
            return CELSIUS_TYPE

        if temperature_type == FAHRENHEIT_TYPE:
            return FAHRENHEIT_TYPE
        
        else:
            print("Invalid temperature type. Please enter 'F' for Fahrenheit or 'C' for Celsius.")
       

# Prompts the user to convert the temperature.
def get_temperature(temperature_type):
    while True:
        temperature = float(input("Enter the temperature you want to convert: "))
        if temperature_type == CELSIUS_TYPE:
            if temperature < ABSOLUTE_ZERO_CELSIUS:
                print(f"Invalid temperature. Please enter a temperature above absolute zero ({ABSOLUTE_ZERO_CELSIUS: .2f}).")
                continue
        elif temperature_type == FAHRENHEIT_TYPE:
            if temperature < ABSOLUTE_ZERO_F:
                print(f"Invalid temperature. Please enter a temperature above absolute zero ({ABSOLUTE_ZERO_F: .2f}).")
                continue
        break
    return temperature

# Performs the temperature conversion.
def display_conversion(temperature_type, temperature):
    if temperature_type == CELSIUS_TYPE:
        fahrenheit = (temperature * 9/5) + 32
        print(f"The temperature in Fahrenheit is {fahrenheit:.2f}°F")
    elif temperature_type == FAHRENHEIT_TYPE:
        celsius = (temperature - 32) * 5/9
        print(f"The temperature in Celsius is {celsius:.2f}°C")

# Calls main function to run the program.
if __name__ == "__main__":
    main()