ABSOLUTE_ZERO_CELSIUS = -273.15


#prompts user to enter a celsius degree
weather_input = int(input("Enter a celsius degree: "))

#Prints the loop from users input
while weather_input < -273:

    #Prints the error message and prompts user again
    print("Error. Please enter a positive number.")
    weather_input = int(input("Enter a celsius degree: "))

    #Prints the table headings
    print()
    print('Celsius\t\tFahrenheit')
    print('-----------------------------')

#Prints the fahrenheit from users input
for celsius in range(0, weather_input + 1):
     fahrenheit = (celsius * 1.8) + 32
     print(f'{celsius}\t\t{fahrenheit: .1f}')
            


# ------ Instructors solution -------
# while True:
#      celsius = int(celsius_input := input("Enter a celsius degree: "))
#      if celsius >= ABSOLUTE_ZERO_CELSIUS:
#          break
#      print(f"Invalid input. Temperature cannot be below absolute zero ({ABSOLUTE_ZERO_CELSIUS} C).")

#      print(f'{"Celsius":>8}\t\t{"Fahrenheit":>8}')
#      print("-----------------------------")

#      if celsius >= 0:
#           for degree in range(0, celsius + 1):
#                fahrenheit = (degree * 1.8) + 32
#                print(f'{degree:>8}\t\t{fahrenheit:>8.2f}')

#      else: 
#           for degree in range(0, celsius - 1, -1):
#                 fahrenheit = (degree * 1.8) + 32
#                 print(f'{degree:>8}\t\t{fahrenheit:>8.2f}')
        
