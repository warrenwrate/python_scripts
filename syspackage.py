from sys import argv

# argv is to allow external parameters to be used; this is an easy example on how to use them.
def sayname(fname, lname, age):
    
    print("My name is %s %s with the age of %d" %(fname, lname, age))

Fname = argv[1]
Lname = argv[2]
Age = int(argv[3])

sayname(Fname, Lname, Age)

