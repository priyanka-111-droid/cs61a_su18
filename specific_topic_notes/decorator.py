'''
Decorators are used to wrap an outer function around an inner one.
Let us take this trace function for example:
It returns a function that takes a single argument 
which traces the inputs and outputs of each function.
'''

def trace(func):
    def inner_args(x):
        print(f"Input: {x}")
        result = func(x)
        print(f"Output: {result}")
        return result
    return inner_args

print(trace(abs)(-4))

# apply this decorator to all functions
def square(x):
    return x*x
sq = trace(square) #wrap trace around square
print(sq(4)) #when you call sq,trace will be applied
#OR
# @trace
# def square(x):
#     return x*x


