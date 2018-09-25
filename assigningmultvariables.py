

#assigning to three variables
a, b, c = ['Warren', 'Wrate', 'Happy']

print("{fname} {lname} is feeling {feeling}.".format( fname= a, lname=b, feeling=c))

beg, *mid, year, month, day = ["Warren", 10,20,30,40,50,60,70,80, 2017, 1, 29]

print("{fname} {year}-{month}-{day}.".format( fname= beg, year=year, month=month, day=day))

for x in mid:
    print("\tamount paid $%d.00" %x)
