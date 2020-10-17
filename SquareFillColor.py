import turtle

def drawPolygon(myturtle, sides, size=100):
  count = 1
  while count <= sides:
    bob.forward(size)
    bob.right(360/sides)
    count = count + 1

bob = turtle.Turtle()
bob.up()
bob.goto(0,0)
bob.down()
drawPolygon(bob, 4)
bob.up()
bob.goto(50,-50)
bob.down()
#bob.color("red")
bob.begin_fill()
drawPolygon(bob, 4, 50)
bob.end_fill()
