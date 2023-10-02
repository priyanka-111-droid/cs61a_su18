'''
Iterables 
    -> Book, can return objects one at a time, Sequence types(list,tuple), Non sequence(dictionary)
Iterators 
    -> Bookmark, give seq access to items one by one,always ordered.
All iterators are iterables, vice versa not true.
'''

book=[1,2,3,4,5,6,7,8,9,10] #10 page book
mark1,mark2 = iter(book),iter(book) #create bookmarks(iterators)
print(next(mark1)) #1
print(next(mark1)) #2

mark3 = iter(mark2) #move mark2 and mark3
print(next(mark3))

# Will soon print Stop Iteration if exceeds number of pages in book