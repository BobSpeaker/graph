import sqlite3
import turtle
import networkx as nx


#ISSUES: Input with apostroph don't work.

#Base functions for inserting, updateing, deleting in db.


#Connect to sqlite DB.
conn = sqlite3.connect('nodeRelation.db')
c = conn.cursor()
g = nx.Graph()


#Initialize.
def myInitialize():
    #wn = turtle.Screen()
    alex = turtle.Turtle()
    alex.forward(150)
    alex.right(200)
    alex.write("Initialization done.")
    print ("Initialization done.")

def commitData():
    global conn
    conn.commit()

#Create tables. Assuming sqlite3 creates a ROWID column that can be used as pk in other tables. Specificly the 'relation' table.
def createTables(c):
    #c.execute ('''DROP TABLE node''')
    c.execute ('''CREATE TABLE IF NOT EXISTS `node`(`id` INTEGER PRIMARY KEY, `nodeText` varchar(512) NOT NULL)''')
    c.execute ('''CREATE TABLE IF NOT EXISTS `relation` (`relationID1` INT NOT NULL, `relationID2` INT NOT NULL)''')
    return

#Test insert data.
#c.execute ("INSERT INTO node(nodeText) VALUES('nodeRelation is a computer program writen in Python') ")
#c.execute ("INSERT INTO node(nodeText) VALUES('Python is a high lvl scripting language.') ")
#c.execute ("INSERT INTO node(nodeText) VALUES('SQLite3 is a single user database.') ")
def insertNode(c):
    nodeText = input("Node text:")
    try:
       c.execute ('INSERT INTO node(nodeText) VALUES("'+nodeText+'")')
    except sqlite3.Error as msg:
        print (msg)
    commitData()

def select(c):
    c.execute ("SELECT * FROM node")
    rows = c.fetchall()
    for row in rows:
        print (row)
    return



def deleteNode(c):
    try:
        c.execute ('DELETE FROM node WHERE id =' + str(input("Input id:")))
    except sqlite3.Error as msg:
        print (msg)

def insertRelation(c):
    relation1 = input("Input rowID of first node in relation:")
    relation2 = input("Input rowID of second node in relation:")
    c.execute ("INSERT INTO relation(relationID1, relationID2) VALUES("+relation1+", "+relation2+")")

def drawNodeGraphTurtle(g):
    'Draws node map with turtle graphics.'
    alex = turtle.Turtle()
    alex.rt(30)

    #For every node: draw it.
    for n in g:
        alex.forward(25)
        alex.write(n[1])
        
    print ("Initialization done.")
    
def drawNodeGraph(g):
    nx.draw_networkx_nodes(g,g,nodelist=g.keys(),
                      node_size=80,
                      node_color=(list(g.values())),
                      cmap=plt.cm.Reds_r)
    plt.xlim(-0.05,1.05)
    plt.ylim(-0.05,1.05)
    plt.axis('off')
    plt.savefig('random_geometric_graph.png')
    plt.show()    

def graphFromDB(c, g):

        
    for row in c.execute ("SELECT * FROM node"):
        print (row[1])
        g.add_node(row)
        

    
    'Constructs a graph from DB data.'
    'Initialize Graph.'
    'Retrieve Nodes.'
    'For each node, insert it in graph.'

    'Possibly edges should be inserted in the same loop.'
    

    

#c.close()
#GUI

#Main loop.

myInitialize()
quitsy = False;
while not quitsy:
    ind = input("command:")
    if ind == 'quit':
        quitsy = True
    
    if ind == 'select':
        select(c)

    if ind == 'insertNode':
        insertNode(c)

    if ind == 'insertRelation':
        insertRelation(c)

    if ind == 'deleteNode':
        deleteNode(c)

    if ind == 'graph':
        graphFromDB(c, g)

    if ind == 'drawNodeGraph':
        drawNodeGraph(g)


#Clean up.
