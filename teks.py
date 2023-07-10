class Teks:
    def enter(self):
        input("press enter to continue... ")

    def wrongInput(self):
        print("\nPlease enter the correct menu number!! [1-5]!!")
        input("press enter for try again... ")

    def wrongValue(self):
        print("\nsorry, only numeric number!!")
        input("press enter to try again...")

    def youwin(self):
        print("\n\nYOU WIN!!!")

    def youlose(self):
        print("\n\nUPS YOU LOST...")

    def draw(self):
        print("\n\nDRAW!")