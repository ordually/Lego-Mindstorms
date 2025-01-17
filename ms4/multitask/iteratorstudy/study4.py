#!/usr/bin/python

print("study4 - special iterator: generator")

# This function is a _generator_ of all Fibonacci numbers.
# Note that the function body has the keyword `yield`, a trigger for the Python interpreter. 
# A function that contains a `yield` statement is called a "generator function", see PEP 0255.
# A generator function is an ordinary function object in all respects, 
# but when a generator function is called no code in the body of the function is executed. 
# Instead a generator-iterator is returned, e.g. check type(fib()).
# The generator-iterator object conforms to the iterator protocol, i.e. it has a `next()`.
# The value returned by `next()` is the expression passed to `yield`.
# The function may have multiple `yield` statements, each next() runs until yield (and starts from previous yield).
# If the function `return`s (with explicit return statement, or implicitly at the end of the function), the iterator stops.
# This could also be implemented with an iterable class, but this is much shorter.
def fib() :
    a = 0
    b = 1
    while True:
      yield a
      a,b = b,a+b
        
# Getting the iterator from the generator: for-in
print("  study4 - for-in")
for element in fib() :
    print( "   ", element )
    if element==13 :
        break # Emergency break


# This generator is made to show what happens when in its lifecycle.
def lifecycle():
    print("    A")
    yield 1
    print("    B")
    yield 2
    print("    C")

print("  study4 - life-cycle")

print( "   ", lifecycle )
lc = lifecycle();
print( "   ", lc )
it = iter(lc)
print( "   ", it )

print("    --------")
try :
    print( "   ", next(lc) )
except StopIteration:
    print( "    StopIteration" )
print("    --------")
try :
    print( "   ", next(lc) )
except StopIteration:
    print( "    StopIteration" )
print("    --------")
try :
    print( "   ", next(lc) )
except StopIteration:
    print( "    StopIteration" )
print("    --------")

   
# study4 - special iterator: generator
#   study4 - for-in
#     0
#     1
#     1
#     2
#     3
#     5
#     8
#     13
#   study4 - life-cycle
#     <function lifecycle at 0x000001133CDEE280>
#     <generator object lifecycle at 0x000001133C93FAC0>
#     <generator object lifecycle at 0x000001133C93FAC0>
#     --------
#     A
#     1
#     --------
#     B
#     2
#     --------
#     C
#     StopIteration
#     --------
