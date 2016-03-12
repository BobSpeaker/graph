#GUI for NodeRelation.
import turtle
from gui_data_model import *  #Abstraction of the visual GUI. Storring locations of GUI elements.

class NRGui():

    #"a tmp model of the graph representing its appearence. It knows where screen items are."
    _gui_dm = gui_dm()
    _graph = "A reference to the actual data model (graph). "
    _pen_color = "#000000"
    _fill_color = "#8888ff" 

    def __init__(self,TurtleScreen, inTurtle):
        #Constructor.
        self._my_turtle = inTurtle
        self._my_turtle_screen = TurtleScreen
        #Bind events.
        self._my_turtle_screen.onclick(self.recieve_click_left,1)  #Left
        self._my_turtle_screen.onclick(self.recieve_click_right,2)  #Right
        self._my_turtle.onclick(self.new_node)
        self._my_turtle.pu()
        
        return(None)

    def draw(self):
        #Draws the gui using the provided turtle. _my_turtle.
        return()
    
    def new_node(self, x, y):
        #Add new node. Contract: Add node to gui and Callback to add node in datamodel.

        
        #Move turtle to the clicked position.
        self._my_turtle.setpos(x,y)

        #Request text input:
        txt = self._my_turtle.textinput("Node input", "Node text:")

        self._my_turtle.color(self._pen_color,self._fill_color)

        self._my_turtle.begin_fill()
        
        self._my_turtle.setpos(x-20,y+10)

        self._my_turtle.pd()
        self._my_turtle.setpos(x+100,y+10)
        self._my_turtle.setpos(x+100,y-20)
        self._my_turtle.setpos(x-20,y-20)
        self._my_turtle.setpos(x-20,y+10)
        self._my_turtle.pu()
        self._my_turtle.end_fill()
        self._my_turtle.setpos(x,y-10)
        
        
        #Output text:
        self._my_turtle.write(txt)

        #Add node to GUI model.
        self._gui_dm.add_node(x,y, 15)

        #Callback to function that adds node to the data model.        
        
        return()

    def remove_node(self):
        #Remove a node
        return()

    def new_edge(self):
        #Add an new edge
        return()

    def remove_edge(self):
        #Remove an edge
        return()
    
    def mode_node(self):
        #Move node to a new location on UI. Subsequently move connected edges.
        return()

    def recieve_click_left(self, x, y):
        #When the user left clicks the interface, call this function.
        #It will then intern call the correct functions.

        #If the user clicks the background, then create a new node on that spot.
        self.new_node(x, y)

        #If the user clicks a node, then (?) create a relation?
        return()

    def recieve_click_right(self, x, y):
        
        #If the user right clicks a node, then open context.
        occupant = self._gui_dm.is_occupied(x, y)
        print (str(occupant.node_id))
        if occupant != 0:
            self._my_turtle.pd()
            self._my_turtle.write("free space - make some nodes")
            print("free space")
            self._my_turtle.pu()  
        else:
            self._my_turtle.pd()
            self._my_turtle.write("this space is taken by:" + str(occupant.node_id))
            print("taken: " + str(occupant.node_id))
            self._my_turtle.pu()
        #Make a look up and see if there is a gui item on this location.
        txt = self._my_turtle.textinput("Context command", "command:")
        

        #Let user choose context item.
        return()

    def write(self, arg):
        self._my_turtle.write(arg)
        return()

        
