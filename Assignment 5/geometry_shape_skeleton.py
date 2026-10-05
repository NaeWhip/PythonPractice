# Imports the module of turtle to draw shapes
import turtle

# Global constants for the menu choices
SQUARE = 1
CIRCLE = 2
TRIANGLE = 3
QUIT = 4

# Main function to call functions to draw the requestedshapes until user chooses to quit
def main():
    choice = 0

    while choice != QUIT:
        display_menu()
        choice = int(input('Enter your choice: '))

        if choice == SQUARE:
            x = int(input('Enter the starting X coordinate: '))
            y = int(input('Enter the starting Y coordinate: '))
            side = int(input('Enter the length of a side: '))
            color = input('Enter the fill color: ')
            square(x, y, side, color)

        elif choice == CIRCLE:
            x = int(input('Enter the starting X coordinate: '))
            y = int(input('Enter the starting Y coordinate: '))
            radius = int(input('Enter the radius: '))
            color = input('Enter the fill color: ')
            circle(x, y, radius, color)

        elif choice == TRIANGLE:
            x = int(input('Enter the starting X coordinate: '))
            y = int(input('Enter the starting Y coordinate: '))
            side = int(input('Enter the length of a side: '))
            color = input('Enter the fill color: ')
            equilateral_triangle(x, y, side, color)

        elif choice == QUIT:
            print("Exiting the program...")
        else:
            print("Error: invalid selection.")
            
    turtle.done()




# Displays the menu of shapes to draw
def display_menu():
    print()
    print("Shape Menu")
    print("1) Draw a Square")
    print("2) Draw a Circle")
    print("3) Draw an Equilateral Triangle")
    print("4) Quit")

#TODO: copy the code from lecture5 slide# 69
# Coordinates the start of shapes and draws
def square(x, y, side, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    for count in range(4):
        turtle.forward(side)
        turtle.left(90)
    turtle.end_fill()
   

def equilateral_triangle(x, y, side, color):
# Draw a triangle starting coordinate at x,y
    turtle.penup()              
    turtle.goto(x, y)           
    turtle.fillcolor(color)     
    turtle.pendown()            
    turtle.begin_fill()         
    for count in range(3):      
        turtle.forward(side)
        turtle.left(120)
    turtle.end_fill()

#TODO: copy lecture slide 71 code
# Draw a circle starting coordinate at x,y
def circle(x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

if __name__ == "__main__":
    main()