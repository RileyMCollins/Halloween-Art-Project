#-----import statements-----
import turtle as trtl
import random as rand
t = trtl.Turtle()
t.shapesize(5)
t.fillcolor("white")
xpos = 0
ypos = 0
t.penup()
wn = trtl.Screen()
wn.bgpic("universe.gif")
wn.addshape("ezgif.com-gif-maker.gif")
t.shape("ezgif.com-gif-maker.gif")





def change_pos():
  t.forward(100)
  num1 = rand.randint(1, 360)
  t.left(num1)

def click(x, y):
  change_pos()



if t.onclick(click):
  change_pos()




wn.mainloop()