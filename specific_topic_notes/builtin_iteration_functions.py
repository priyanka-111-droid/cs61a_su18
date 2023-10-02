'''MAP means map a function to every element'''
def square(x):
    return x*x

m = map(square,[1,2,3,4,5,6]) # map(function,iterable) -> returns iterator
print(m) # iterator (CANNOT VIEW CONTENTS)
print(next(m))
print(list(m)) #[1,4,9,16,25,36]



'''FILTER based on a condition'''
def greater(x):
    return x>=4
f = filter(greater,[1,2,3,4,5,6]) #filter(function,iterable)->returns iterator
print(list(f))



'''ZIP means combine 2 or more iterables into 1'''
name=['abc','def','ghi']
age=[18,19,20]
z = zip(name,age)
lst = list(z)

name,age = zip(*lst) #unzip
print(age)
