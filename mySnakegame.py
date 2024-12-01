import turtle
import time
import random

delay = 0.1


# score
score = 0
high_score = 0

# screen
wn = turtle.Screen()
wn.title("Snake game by Students")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0) # Turns off the screen updates

# head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0,0)
head.direction = "stop"


# food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red") 
food.penup()
food.goto(0,100)

segments = []

# score writer
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0  Hight Score: 0", align = "center", font=("Courier", 24, "normal"))


# Funktions
def go_up():
	if head.direction != "down": 
		head.direction = "up"

def go_down():
	if head.direction != "up":
		head.direction = "down"

def go_left():
	if head.direction != "right":
		head.direction = "left"

def go_right():
	if head.direction != "left":
		head.direction = "right"

def move():
	if head.direction == "up":
		y = head.ycor()
		head.sety(y + 20)

	if head.direction == "down":
		y = head.ycor()
		head.sety(y - 20)

	if head.direction == "left":
		x = head.xcor()
		head.setx(x - 20)

	if head.direction == "right":
		x = head.xcor()
		head.setx(x + 20)

# Keys connections
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")


# Main game loop
while True:
	wn.update()

	# check collision with border

	if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
		time.sleep(1)
		head.goto(0,0)
		head.direction = "stop"


	# Checking collision with food
	if head.distance(food) < 20:
		# Moving food to random postion
		x = random.randint(-290,290)
		y = random.randint(-290,290)
		food.goto(x,y)

		# Adding/Increasing Length of Snake
		new_segment = turtle.Turtle()
		new_segment.speed(0)
		new_segment.shape("square")
		new_segment.color("pink")
		new_segment.penup()
		segments.append(new_segment)

		# Adding score
		score +=1

		if score > high_score:
			high_score = score
		pen.clear()
		pen.write("Score: {}  Hight Score: {}".format(score,high_score), align = "center", font=("Courier", 24, "normal"))

		

	# moving end segment first in reverse

	for index in range(len(segments)-1, 0, -1):
		x = segments[index -1].xcor()
		y = segments[index -1].ycor()
		segments[index].goto (x,y)


	# Move segment 0 to where the head is 
	if len(segments) > 0:
		x = head.xcor()
		y = head.ycor()
		segments[0].goto(x,y)



	move()


	# Check for head collision with body segments
	for segment in segments:
		if segment.distance(head) < 20:
			time.sleep(1)
			head.goto(0,0)
			head.direction = "stop"
			
			
			# Hiding segments
			for segment in segments:
				segment.goto(1000, 1000)

			# Clearing segments list
			segments.clear()

			# Resting score
			score = 0
			
			# Updating score
			pen.clear()
			pen.write("Score: {}  Hight Score: {}".format(score,high_score), align = "center", font=("Courier", 24, "normal"))


	time.sleep(delay)
wn.mainloop()

