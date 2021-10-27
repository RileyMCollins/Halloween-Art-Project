
import turtle
t = turtle.Turtle()
wn = turtle.Screen()
t.turtlesize(5)

wn.mainloop()

def run():
  t.penup()
  t.forward(100)


def click(x,y):
  run()

if t.onclick(click):
  run()

wn.mainloop()