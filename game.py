from tkinter import *

class Character():
    def __init__(self,str,int,dex):
        self.lvl = 1
        self.hp = 10
        self.mana = 10
        self.str = str
        self.int = int
        self.dex = dex

    def levelStats(stat, ammount):
        self.stat += ammount

    def walk(direction):
        return None

    def speak():
        return None

    def speak():
        return None

class Warrior(Character):
    def __str__(self):
        return "You see yourself. You are a Warrior with "+str(self.str)+ " Strength, "\
        + str(self.int) +" Intelligence and "+str(self.dex)+" Dexterity."

    def attack():
        return None

class Mage(Character):
    def __str__(self):
        return "You see yourself. You are a Warrior with "+str(self.str)+ " Strength, "\
        + str(self.int) +" Intelligence and "+str(self.dex)+" Dexterity."

    def attack():
        return None

class Ranger(Character):
    def __str__(self):
        return "You see yourself. You are a Warrior with "+str(self.str)+ " Strength, "\
        + str(self.int) +" Intelligence and "+str(self.dex)+" Dexterity."

    def attack():
        return None


def pickStats(points):
    while points != 0:
        print("You have "+str(points) +" points to spend. Which would you like to add to?")
        choice = input()
        if choice.lower == "str":
            hero.levelStats("str",1)
        elif choice.lower == "int":
            hero.levelStats("int",1)
        elif choice.lower == "dex":
            hero.levelStats("dex",1)
        points -= 1


def decision():
    choice = input("What do you want to do?")
    if choice == "walk":
        hero.walk()


def main():
    root = Tk()

    topFrame = Frame(root)
    topFrame.pack()

    bottomFrame = Frame(root)
    bottomFrame.pack(side = BOTTOM)

    one = Label(root, text="one", bg="red",fg="white")
    one.pack()

    two = Label(root, text="two", bg="orange",fg="white")
    two.pack(fill=X)

    three = Label(root, text="three", bg="green",fg="white")
    three.pack(side=LEFT, fill=Y)

    button1 = Button(topFrame, text ="Button 1", fg = "blue")
    button2 = Button(topFrame, text ="Button 2", fg = "red")
    button3 = Button(topFrame, text ="Button 3", fg = "pink")
    button4 = Button(bottomFrame, text ="Button 4", fg = "green")

    button1.pack(side=LEFT)
    button2.pack(side=LEFT)
    button3.pack(side=LEFT)
    button4.pack(side=BOTTOM)


    root.mainloop()

    done = False
    alive = True

    print("Welcome to the game.")

    while not done:
        choice = input("Please choose a class ")
        if choice.lower() == "warrior":
            done = True
            print("You have chosen the strong warrior.")
            hero = Warrior(6,3,5)
        elif choice.lower() == "mage":
            done = True
            print("You have chosen the wise mage.")
            hero = Mage(3,6,5)
        elif choice.lower() == "ranger":
            done = True
            print("You have chosen the quick ranger")
            hero = Ranger(3,5,6)
        else:
            print("You have to choose one of the options.")

    pickStats(5)


main()
