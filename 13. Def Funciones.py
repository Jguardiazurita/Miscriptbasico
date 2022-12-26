#defines a function double that takes a single argument,
#doubles it, and returns it
def double(x):
    y = x * 2
    return y

#calls function double with a single argument 3
#and gets the return value
result = double(3)
print(result)

def square(x):
    y = x * x
    return y

result = square(10)
print (result)

def greater_than(x, y):
    if x > y:
        return True
    else:
        return False

a=2
b=3
result = greater_than(a, b)
print("{} is greater than {}".format(a,b,result))

def greater_than(x, y):
    """Returns True if x is greater than y, otherwise False."""

    if x > y:
        return True
    else:
        return False

#prints general help on the function, including the docstring
help(greater_than)
