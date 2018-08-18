import turtle


def draw_square(a):
 	for i in range (0,4):
 		a.forward(100)
 		a.right(90)

def draw():
	window  =  turtle.Screen()
	window.bgcolor("red")

	a  = turtle.Turtle()
	a.shape("turtle")
	a.color("yellow")
	a.speed(10)
	for i in range(1,37):
		draw_square(a)
		a.right(10)
	window.exitonclick()

draw()



