'''
Generators-> Our own custom built iterators
Write a generator function and it will return an iterator.
This iterator is called a generator.
It has yield instead of return
'''

def new_years_countdown(n):
    print('Begin countdown')
    while(n>=0):
        yield n
        n-=1
    print('Happy New Years!')


new_yr_2024 = new_years_countdown(10)
# print(new_yr_2024) #generator object
# print(iter(new_yr_2024)) #generator is also iterator,so this will also return same object
print(next(new_yr_2024))
print(next(new_yr_2024))
print(next(new_yr_2024))
print(next(new_yr_2024))
print(next(new_yr_2024))
print(next(new_yr_2024))
print(next(new_yr_2024))
print(next(new_yr_2024))
print(next(new_yr_2024))
print(next(new_yr_2024))
print(next(new_yr_2024))
print(next(new_yr_2024))