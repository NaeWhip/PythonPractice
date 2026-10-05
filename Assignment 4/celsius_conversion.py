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
            
    
        
