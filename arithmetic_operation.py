
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b) :
    return a * b


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    add_result = add(a,b)
    subtract_result = subtract(a,b)
    multiply_result = multiply(a,b)
    
    print(add_result)
    print(subtract_result)
    print(multiply_result)
