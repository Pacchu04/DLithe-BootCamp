# Iterator --> is an object which implements the iterator protocol

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


# Looping Through an Iterator
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

# Create an custom Iterator
class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        current = self.current
        self.current += 1
        return current

for num in MyIterator(1, 5):
    print(num)

# Generator -->Generators provide an easier way to create iterators using the yield keyword. 
def simple():  
  for i in range(10):  
    if(i%2==0):  
      yield i  
  
#Successive Function call using for loop  
for i in simple():  
    print(i) 

def my_generator(start, end):
    current = start
    while current < end:
        yield current
        current += 1

for num in my_generator(1, 5):
    print(num)

# Decorators -->are a way to modify or enhance functions or methods without changing their definition.
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()


# Filter --> The filter() function constructs an iterator from elements of an iterable for which a function returns true.
def is_even(num):
    return num % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(is_even, numbers)
print(list(even_numbers))

#----------------------------------------------------
ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)

for x in adults:
  print(x)


# Map --> The map() function applies a given function to all the items in an input list.
def square(num):
    return num * num

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)
print(list(squared_numbers)) 
#------------------------------------------------------
def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))
print(list(x))


# Reduce --> applies a given function to the elements of an iterable, reducing them to a single value.
from functools import reduce

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]
total = reduce(add, numbers)
print(total) 

#-------------------------------------
my_list = [1, 2, 3, 4, 5]  
   
product = reduce(lambda x, y: x * y, my_list)  
  
# Printing output  
print(f"Product = {product}")