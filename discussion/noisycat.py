from cat import Cat
class NoisyCat(Cat):
    def talk(self):
        """Talks twice as much as a regular cat.

        >>> NoisyCat('Magic', 'James').talk()
        Magic says meow!
        Magic says meow!
        """
        # self.talk()
        # self.talk() 
        # Above code WRONG,recursive error!
        Cat.talk(self)
        Cat.talk(self)

# main
NoisyCat('Magic', 'James').talk()