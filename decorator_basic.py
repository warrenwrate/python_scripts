
def my_decorator(some_function):

    def wrapper(*args):

        print("Something is happening before ", some_function.__name__ ," is called.")

        some_function(*args)

        print("Something is happening after",some_function.__name__ ," is called.\n")

    return wrapper

@my_decorator
def expressyourself(expression):
    print(expression)


@my_decorator
def mathfunction(a, b=15):
    print(a + b)


expressyourself("Wheee!! Fun with Functions!!")
mathfunction(30)