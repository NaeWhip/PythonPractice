import turtle

#constants of both length and color of diamond
SIDE_LENGTH = 100
color = 'blue'

#setup of the turtle window
turtle.setup(500,600)

#setup  of the turtle 
turtle.hideturtle()
turtle.fillcolor(color)

#drawing of left-side of diamond   
turtle.begin_fill()
turtle.penup()
turtle.goto(SIDE_LENGTH, 0)
turtle.pendown() 
turtle.goto(0,SIDE_LENGTH)
turtle.goto(-SIDE_LENGTH,0)
turtle.goto(0,-SIDE_LENGTH)
turtle.goto(SIDE_LENGTH,0)
turtle.pendown()
turtle.end_fill()

#sets up for right-side diamond
turtle.penup()
turtle.goto(SIDE_LENGTH,0)
turtle.pendown()

#drawing of right-side diamond
turtle.begin_fill()
turtle.goto(200,SIDE_LENGTH)
turtle.goto(300,0)
turtle.goto(200,-SIDE_LENGTH)
turtle.goto(SIDE_LENGTH,0)
turtle.end_fill()

#outputs the drawing of turtle
turtle.done()
