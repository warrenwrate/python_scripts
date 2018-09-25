l = [0,1,2,3,4,5]
print("full list")
for num in l:
    print(num)

print("last three")
for num in l[-3:]:
    print(num)

print("up to 2")
for num in l:
    if num > 2:
        break
    print(num)

print("full list backwards")
# should run in reverse
for num in l[::-1]:
    print(num)

#from zero to ten
for num in l[0:3]:
    print('printing {number} out of 3'.format(number = num))

print("loop through tuple")
tl = [(1,2),(3,4),(5,6),(7,8)]

for (t1, t2) in tl:
    print(t2)


print("loop through dictionary")
d = {}
d['firstName'] = "Warren"
d['lastName'] = "Wrate"

for k,v in d.items():
    print("key {k}, value {v}".format(k = k, v = v))


print("While loop")

n_count = 0

# continue will send the loop back to the beginning
# break will end the loop
while n_count < 20:
    print(n_count)
    n_count += 1
    if n_count < 10:
        print("kid years")
        # continue
    elif n_count < 13:
        print("preteen years")
    elif n_count < 18:
        print("rebel years")
    else:
        print("adulthood")
    
    if n_count in l:
        print('little kid years ' + str(n_count))
    else:
        continue
else:
    print("while loop complete")
    