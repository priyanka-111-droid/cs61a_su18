# Base class
class Parent:
	def func1(self):
		print("This function is in parent class.")


# Derived class1
class Son(Parent):
	def func2(self):
		print("This function is in child 1.")


# Derived class2
class Daughter(Parent):
	def func3(self):
		print("This function is in child 2.")




s = Son()
d = Daughter()
s.func1()
s.func2()
d.func1()
d.func3()
