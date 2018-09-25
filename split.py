

string = 'a-b-c-d'
newstr = string.split('-')

print(newstr)


newstr = list(map(lambda x: '"' + x + '"', newstr))

joinstr = ",".join(newstr)

print(joinstr)