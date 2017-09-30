from map import *


class Character():
    def __init__(self,str,int,dex):
        self.lvl = 1
        self.hp = 10
        self.mana = 10
        self.str = str
        self.int = int
        self.dex = dex

    def levelStats(self,stat, ammount):
        self.__dict__[stat] += ammount

    def walk(self, direction):
        print("You walk "+ direction+"...")
        return

    def speak():
        return None

    def speak():
        return None

class Warrior(Character):
    def __str__(self):
        return "You see yourself. You are a level "+str(self.lvl)+" Warrior with "+str(self.str)+ " Strength, "\
        + str(self.int) +" Intelligence and "+str(self.dex)+" Dexterity."

    def attack():
        return None

class Mage(Character):
    def __str__(self):
        return "You see yourself. You are a level "+str(self.lvl)+" Mage with "+str(self.str)+ " Strength, "\
        + str(self.int) +" Intelligence and "+str(self.dex)+" Dexterity."

    def attack():
        return None

class Ranger(Character):
    def __str__(self):
        return "You see yourself. You are a level "+str(self.lvl)+" Ranger with "+str(self.str)+ " Strength, "\
        + str(self.int) +" Intelligence and "+str(self.dex)+" Dexterity."

    def attack():
        return None


def pickStats(hero, points):
    while points != 0:
        print("You have "+str(points) +" points to spend. Which would you like to add to?")
        choice = input()
        if choice.lower() == "str":
            hero.levelStats("str",1)
            points -= 1
        elif choice.lower() == "int":
            hero.levelStats("int",1)
            points -= 1
        elif choice.lower() == "dex":
            hero.levelStats("dex",1)
            points -= 1
        else:
            print("You have to choose between 'Str', 'Dex, or 'Int'.")

    return hero


def decision(hero):
    print("You have "+str(hero.hp)+" health and "+ str(hero.mana)+ " mana.")
    choice = input("What do you want to do?")
    if choice == "look":
        print(hero)
    if choice == "walk":
        direction = input("Which direction? ")
        hero.walk(direction)

    return hero


def main():
    # root = Tk()
    #
    # label1 = Label(root, text = "Name: ")
    # label2 = Label(root, text = "Password: ")
    # entry1 = Entry(root)
    # entry2 = Entry(root)
    #
    # label1.grid(row=0, sticky=E)
    # label2.grid(row=1)
    #
    # entry1.grid(row=0,column=1, sticky=W)
    # entry2.grid(row=1,column=1, sticky=W)
    #
    # c = Checkbutton(root, text="Keep me logged in.")
    # c.grid(columnspan=2)
    #
    # root.mainloop()

    #-------------------------------

    # root = Tk()
    #
    # topFrame = Frame(root)
    # topFrame.pack()
    #
    # bottomFrame = Frame(root)
    # bottomFrame.pack(side = BOTTOM)
    #
    # one = Label(root, text="one", bg="red",fg="white")
    # one.pack()
    #
    # two = Label(root, text="two", bg="orange",fg="white")
    # two.pack(fill=X)
    #
    # three = Label(root, text="three", bg="green",fg="white")
    # three.pack(side=LEFT, fill=Y)
    #
    # button1 = Button(topFrame, text ="Button 1", fg = "blue")
    # button2 = Button(topFrame, text ="Button 2", fg = "red")
    # button3 = Button(topFrame, text ="Button 3", fg = "pink")
    # button4 = Button(bottomFrame, text ="Button 4", fg = "green")
    #
    # button1.pack(side=LEFT)
    # button2.pack(side=LEFT)
    # button3.pack(side=LEFT)
    # button4.pack(side=BOTTOM)
    #
    #
    # root.mainloop()

    done = False

    alive = True

    print("Welcome to the game.")

    # while not done:
    #     choice = input("Please choose a class ")
    #     if choice.lower() == "warrior":
    #         done = True
    #         print("You have chosen the strong warrior.")
    #         hero = Warrior(6,3,5)
    #     elif choice.lower() == "mage":
    #         done = True
    #         print("You have chosen the wise mage.")
    #         hero = Mage(3,6,5)
    #     elif choice.lower() == "ranger":
    #         done = True
    #         print("You have chosen the quick ranger")
    #         hero = Ranger(3,5,6)
    #     else:
    #         print("You have to choose one of the options.")
    #
    # hero = pickStats(hero, 5)

    global x
    global y

    while alive:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                alive = False
            print(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x -= 10
                    print("Hello there")
                if event.key == pygame.K_RIGHT:
                    x += 10
                    print("Hello there")
                if event.key == pygame.K_UP:
                    y -= 10
                    print("Hello there")
                if event.key == pygame.K_DOWN:
                    y += 10
                    print("Hello there")


        gameDisplay.fill(white)
        hero(x,y)
        pygame.display.update()
        clock.tick(30)

    pygame.quit()


        # hero = decision(hero)

main()
