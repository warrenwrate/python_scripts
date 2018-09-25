from optparse import OptionParser

parser = OptionParser()


parser.add_option('-n', '--name', dest='name' , help="please enter in name")

options, args = parser.parse_args()

#option should show the value of passed into the (opitons)
#arg are the arguments coming afterwards.
print('options:', options, '\n', 'args:', args)

v = ', '.join(args)

print('The', str(options.name) + ':', v)

lname = input("place lastname: ")

print('Oh! I thought it was the', lname + 's')