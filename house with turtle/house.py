from turtle import*



#properties
speed(4)
width(7)


#square house
forward(150)
left(90)
forward(200)
left(90)
forward(300)
left(90)
forward(200)
left(90)
forward(150)

#triangle roof
color("red")
begin_fill()
penup()
goto(152, 200)
pendown()
left(135)
forward(210)

left(90)
forward(213)
left(135)
forward(295)

#door
color("brown")
begin_fill()
penup()
goto(30, 0)
pendown()
left(90)
forward(75)
left(90)
forward(50)
left(90)
forward(75)
left(90)
forward(50)
end_fill()

#window 1
color("blue")
penup()
goto(130, 100)
pendown()
left(180)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
penup()
goto(130,125)
pendown()
right(90)
forward(50)
#window 2
penup()
goto(105, 150)
pendown()
left(90)
forward(50)
penup()
goto(-70,100)
pendown()
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)

penup()
goto(-70,125)
pendown()
right(90)
forward(50)
penup()
goto(-95,150)
pendown()
left(90)
forward(50)
#door handle
color("yellow")
penup()
goto(30,35)
pendown()
left(90)

exitonclick()