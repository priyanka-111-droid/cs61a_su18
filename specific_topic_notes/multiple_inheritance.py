class Mother:
    def look(self):
        print('I have blue eyes')

class Father:
    def height(self):
        print("I am tall.")

class Child(Mother,Father):
    def appearance(self):
        print('I have blue eyes and am tall')

alex=  Child()
alex.appearance() # I have blue eyes and am tall