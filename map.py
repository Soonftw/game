from tkinter import *

root = Tk()

def printName(world,row,column):
    print (world[row][column])

class Grid():
    def __init__(self):
        self.monster = "hello there"
        self.item = None
        self.value = "hello there"

        self.north = None
        self.south = None
        self.east = None
        self.west = None

    def __str__(self):
        return str(self.east.monster)+str(self.west.monster)+str(self.north.monster)+str(self.south.monster)

def mapCreator():
    world = [[i for i in range(10)] for j in range(10)]
    worldmap = [[i for i in range(10)] for j in range(10)]
    # print(world)
    for row in range(0,10):
        for column in range(0,10):
            world[row][column] = Grid()
    print(world[5][0].monster)

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

        photo = PhotoImage(file="hello_there.jpg")

        for row in range(0,10):
            for column in range(0,10):
                square = Button(root, height=100,width=100,image=photo,command=lambda: printName(world,row,column))
                square.photo = photo
                square.grid(row=row,column=column)


mapCreator()
root.mainloop()
