class Animal:  
    def speak(self):  
        print("Animal Speaking")  

#child class Dog inherits the base class Animal  
class Dog(Animal):  
    def bark(self):  
        print("dog barking")  
d = Dog()  
d.bark()  #dog barking
d.speak()  #Animal speaking