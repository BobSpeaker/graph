class gui_item():

    x = 0
    y = 0
    node_id = 0

    def __init__(self, x, y, node_id):
        self.x = x
        self.y = y
        self.node_id = node_id
        return(None)

class gui_dm():

    def __init__(self):
        self.none_item = gui_item(0,0,0)
        self.data_model = [[self.none_item for y in range(1, 1000)] for x in range(1, 1000)]
        return(None)
    
    def add_node(self, x, y, node_id):
        #Adds a node to the memory_model and occupies the foot print.
        print(x)
        print(y)
        
        self.data_model[int(x)][int(y)] = gui_item(x,y, node_id)
        return()

    def is_occupied(self, x, y):
        #If x, y is occupied by a gui item, then return a reference to the item.
        return(self.data_model[int(x)][int(y)])
