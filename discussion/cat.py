from pet import Pet
class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        Pet.__init__(self,name,owner)

    def talk(self):
        """ Print out a cat's greeting.
        >>> Cat('Thomas', 'Tammy').talk()
        Thomas says meow!
        """
        print(self.name+'says meow!')
    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero, 'is_alive'
        becomes False.
        """
        if(self.lives>0):
            self.lives-=1
            if(self.lives==0):
                self.is_alive = False 
        else:
            print("Cat already has no lives left")
