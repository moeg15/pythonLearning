class SimpleGame:
    def __init__(self):
        pass
    
    def beginGame(self):
        print("welcome home slice")    
        self.first_encounter()
    def first_encounter(self):
        print("Dark cave tee hee")
        print("uwu enter? enter 1")
        print("uwu do not enter? enter 2")
        choice = input("what do you do? 1/2:")

        if choice == "1":
            self.enter_cave()
        elif choice == "2":
            self.walk_away()
        else:
            print("invalid choice. try again")
            self.first_encounter()
    def enter_cave(self):
        print("you have enterd the cave!")
        print("you see a big ol spider")
        print("run away? enter 1")
        print("do epic battle? enter 2")
        choice = input("what do you do? enter 1 or 2")

        if choice == "1":
            self.run_away()
        elif choice == "2": 
            self.fight_spider()
        else:
            print("how dare you enter a third option when i provide two very good and clear choices try again")
            self.enter_cave()

    def fight_spider(self):
        print("launch nukes at spider? enter 1")
        print("stab spider with knife? enter 2")
        choice = input("what do you do? enter 1 or 2")

        if choice == "1":
            self.die_insantly()
        elif choice == "2": 
            self.stab_spider()
        else:
            print("how dare you enter a third option when i provide two very good and clear choices try again")
            self.fight_spider()

    def stab_spider(self):
        print("you win the million billion trillion dollar! yuhhhhh")

    def die_insantly(self):
        print("why on earth would you launch nukes while in the cave you idiot!")

    def walk_away (self):
        print("you trip on a rock and die")

    def run_away (self):
        print("you trip on a twig and die")
    

      

if __name__ == "__main__":
    game = SimpleGame()
    game.beginGame()

