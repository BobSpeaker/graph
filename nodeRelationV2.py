import turtle
import nodeRelationGUIV2 #Requiers the turtle library.

#Initialize.
    #Retrieve data.
    #Prepare GUI.
my_ts = turtle.Screen() #Screen with canvas to draw on and recieve events from.
my_turtle = turtle
gui = nodeRelationGUIV2.NRGui(my_ts, my_turtle) #Our own GUI.
gui.draw() #First drawing.

#Eventloop.

my_turtle.mainloop()
my_turtle.done()

#Shutdown.
    #Save data.
