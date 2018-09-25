# super basic
def my_first_function():
    print("hello world")

my_first_function()

# super basic with argument
# with a document string of "Simple greeting function"
def my_sec_function( name):
    """
    Simple greeting function
    """
    print("hello " + name)

my_sec_function('Warren')

def add_num(num1, num2):
    add = num1 + num2
    return add

print(add_num(384, 16))

def is_prime(num):
    l  = range(2, num)
    for x in l:
        if num % x == 0:
            return True
        else:
            continue
    
    return False

print(is_prime(18))
print(is_prime(17))
