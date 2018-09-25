

#basic wrapper
def multiplyby(x):
    def wrapper(y):
        return  x * y
    return wrapper


multby4 = multiplyby(4)

print(multby4(10))


