#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold


#Name
#Mohammad Qaddoura
#Date
#12/18/19


#### INSTRUCTIONS ####
#Create an etch a sketch turtle game                                                             DONEDONEDONE                              
#The turtle should move with the arrow keys (up, down, left and right), and draw                 DONEDONEDONE
#Space should clear the screen                                                                   DONEDONEDONE
#o and p should make the pen size bigger and smaller                                             DONEDONEDONE
#u should pick the pen up or put the pen down                                                    DONEDONEDONE
#All code must be commented                                                                      DONEDONEDONE
#BONUS
#Add a feature to change colors                                                                  DONEDONEDONE

#import required libraries
import turtle as trtl

#create turtle and game outline
etch_me = trtl.Turtle()
etch_me.pensize(3)

#inform the user on commands
etch_me.penup()
etch_me.goto(-400, 20)
etch_me.write("use arrow keys to move")
etch_me.goto(-400,0)
etch_me.write("press b for blue")
etch_me.goto(-400,-20)
etch_me.write("press r for red")
etch_me.goto(-400,-40)
etch_me.write("u toggles the marking on or off")
etch_me.goto(-400,-60)
etch_me.write("o to enlarge line size")
etch_me.goto(-400,-80)
etch_me.write("p to decrease line size")
etch_me.goto(-400,-100)
etch_me.write("space to clear the board")

etch_me.goto(0,0)
etch_me.pendown()
#movement functions
def Up():                   #turtle goes up
   etch_me.setheading(90)
   etch_me.forward(10)
    
def Down():                  #turtle goes down
   etch_me.setheading(270)
   etch_me.forward(10)
 
 
def Left():                 #turtle goes left
   etch_me.setheading(180)
   etch_me.forward(10)

 
def Right():                #turtle goes right
   etch_me.setheading(0)
   etch_me.forward(10)

#color/drawing functions
def clear_screen(): #clears the screen
    etch_me.clear()

clicked = 0
def toggle_pen():               #toggles the drawer to continue or stop marking where it goes
    global clicked
    if clicked is 0:
        etch_me.penup()
        clicked = (clicked + 1)
    elif clicked is 1:
        etch_me.pendown()
        clicked = (clicked - 1)

def enlarge_pensize():          #increases pensize
    etch_me.pensize(5)
    
def decrease_pensize():         #decreases pensize
    etch_me.pensize(1)

def color_change_blue():        #turns the pen blue
    etch_me.pencolor("blue")

def color_change_red():         #turns the pen red
    etch_me.pencolor("red")
#create screen
wn = trtl.Screen()

#bind to keypresses
wn.onkeypress(color_change_blue, "b")
wn.onkeypress(color_change_red, "r")
wn.onkeypress(enlarge_pensize, "o")
wn.onkeypress(decrease_pensize, "p")
wn.onkeypress(toggle_pen, "u")
wn.onkeypress(clear_screen, "space")
wn.onkeypress(Up, "Up")
wn.onkeypress(Down, "Down")
wn.onkeypress(Left, "Left")
wn.onkeypress(Right, "Right")

#listen
wn.listen()

#mainloop
wn.mainloop()