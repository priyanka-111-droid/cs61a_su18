'''
First class functions:
Python has first-class functions which means it can support operations such as being passed as 
argument,returned from function and assigned to a variable.


Higher order function:
Function is said to be higher order function if it accepts other function as argument or is
returned from a function.
'''


#normal function
def square(x):
    return x*x 
f = square 
print(square)
print(f(4))


#function that accepts other function (eg. our own implementation of map)
def my_map(func,obj):
    result=[]
    for x in obj:
        result.append(func(x))
    return result 

all_squares = my_map(square,[1,2,3])
print(all_squares)


#function that returns another function(eg. logger)
def logger(msg):
    def log_msg():
        print('Log:',msg)
    return log_msg 

test = logger('Hi')
test()


