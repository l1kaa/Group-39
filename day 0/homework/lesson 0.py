from turtle import *


#painting a house
#step 1:building the walls of the house
speed(30)
width(7)
color("black")
begin_fill()
forward(200) 
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()
#end of building the walls of the house
#step2: drawing a door
 
forward(70)
color("purple")
begin_fill()
left(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)
end_fill()
#end of drawing the door
#step 3: drawing a rooftop
penup()
goto(200,200)
pendown()
color("purple")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
left(120)
forward(200)
end_fill()
#end of drawing the rooftop
#step 5: drawing the windows
penup()
goto(170,170)
pendown()

color("yellow")
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)

penup()
goto(150,170)
pendown()

right(90)
forward(40)

penup()
goto(170,150)
pendown()

right(90)
forward(40)

penup()
goto(30,170)
pendown()

left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)

penup()
goto(50,170)
pendown()

left(90)
forward(40)

penup()
goto(30,150)
pendown()

left(90)
forward(40)

#end of drawing a house:)


exitonclick()