# Lambda functions
x = lambda a, b: a + b
print(x(5, 6))

def myFunction(n):
    return lambda a: a * n

myDoubler = myFunction(2)
print(myDoubler(11))
print('/n')

# another lambda function
a = lambda b: b
print(a(10))
