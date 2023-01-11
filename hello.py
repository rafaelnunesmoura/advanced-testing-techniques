def add_this(x, y):
    
    print(f"This is x: {x} and the type is {type(x)}")
    print(f"This is y: {y} and the type is {type(y)}")
    
    try:
        result = x+y
    except TypeError:
        print(f"The wrong type passed")
        result = int(x) + int(y)
    
    print(f"This is the result {result}")
    
    return result

print(add_this("1", 2))


    