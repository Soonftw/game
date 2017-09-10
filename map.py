from tkinter import *
import random

root = Tk()

# def callback(event):
    # print ("clicked at", event.x, event.y)




class Grid():
    def __init__(self,value, photo):
        self.monster = "hello there"
        self.image = photo
        self.item = None
        self.value = value
        self.has_hero = False

        self.north = None
        self.south = None
        self.east = None
        self.west = None

    def __str__(self):
        # return str(self.east.monster)+str(self.west.monster)+str(self.north.monster)+str(self.south.monster)
        return str(self.value)

background_url="img\\background_tile.gif"
hero_url="img\\guy.gif"

def mapCreator():
    value = 1
    world = [[i for i in range(10)] for j in range(10)]
    worldmap = [[i for i in range(10)] for j in range(10)]
    photo = PhotoImage(file=background_url)
    # print(world)
    for row in range(0,10):
        for column in range(0,10):
            world[row][column] = Grid(value,photo)
            value +=1

    random_tile=random.randint(51,59)
    for i in range(0,10):
        for j in range(0,10):
            if world[i][j].value == random_tile:
                world[i][j].image=PhotoImage(file=hero_url)
                world[i][j].has_hero=True

    # print(world[0][0])

    for row in range(0,10):
        #Connect the squares to the right
        for column in range(0,10):
            try:
                world[row][column].east = world[row][column+1]
            except IndexError:
                world[row][column].east = world[row][0]

            try:
                world[9-row][9-column].west = world[9-row][9-column-1]
            except IndexError:
                world[9-row][9-column].west = world[row][9]

            try:
                world[row][column].south = world[row+1][column]
            except IndexError:
                world[row][column].south = world[0][column]

            try:
                world[9-row][9-column].north = world[9-row-1][9-column]
            except IndexError:
                world[row][column].north = world[0][column]


    return world

        # print(world[1][0])
                # square = Label(root,text=world[row][column])
                # square = Button(root, height=100,width=100,image=photo,command=lambda:printName(world,row,column))
                # square.photo = photo
                # square.bind("<Button-1>",lambda:printName(world,row,column))
                # square.grid(row=row,column=column)


world = mapCreator()

def key(event):
    print ("pressed", repr(event.char))

def press_left(event,world):
    for i in range(0,10):
        for j in range(0,10):
            if world[i][j].has_hero:
                print(world[i][j])
                world[i][j].has_hero=False
                world[i][j].image=PhotoImage(file=background_url)
                world[i][j-1].has_hero=True
                world[i][j-1].image=PhotoImage(file=hero_url)
            square = Label(root,borderwidth=0,highlightthickness=0,height=100,width=100,image=world[row][column].image,text=world[row][column], compound = CENTER)
            # square.photo = photo
            square.grid(row=row,column=column)
            square.photo = world[row][column].image
    root.update()


    print ("pressed left")
def press_right(event):
    print ("pressed right")
def press_up(event):
    print ("pressed up")
def press_down(event):
    print ("pressed down")

def callback(event):
    square.focus_set()
    print ("clicked at", event.x, event.y)

for row in range(0,10):
    for column in range(0,10):
        square = Label(root,borderwidth=0,highlightthickness=0,height=100,width=100,image=world[row][column].image,text=world[row][column], compound = CENTER)
        # square.photo = photo
        square.grid(row=row,column=column)
        square.photo = world[row][column].image
        square.bind("<Key>",key)
        square.bind("<Left>",lambda event: press_left(event,world))
        square.bind("<Right>",press_right)
        square.bind("<Up>",press_up)
        square.bind("<Down>",press_down)
        square.bind("<Button-1>", callback)


root.mainloop()
# for i in range(len(world[0])):
#     print(world[5][i].west)
