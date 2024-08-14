

def logCalls (func):
    def outputFunc(*args, **kwargs):
        result = func (*args, **kwargs)
        print (f"Log: calling function {func.__name__} with arguments {args} and {kwargs}. Result: {result} ")
    return outputFunc
    
@logCalls
def add(a, b):
    return a + b

@logCalls
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

add(3, 5)
greet("Alice")
greet("Bob", greeting="Hi")