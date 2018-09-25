

print(ord('1') - 48)
print(ord('2')- 48)
print(chr(49))
print(chr(50))

print(int('123456'))
print(str(123456) + '7')

### reverse array = range(arr, stop at, decrement)
for x in range(len([1,2,3,4,5])-1, -1, -1):
     print('test',x)

def num(array):

    numstr = ''
    output = []
    for num in array:
        numstr += str(num)
    
    fullnum = int(numstr) + 1
    numstr = str(fullnum)

    for s in numstr:
        output.append(int(s))
    
    print(output)

num([9,9,99])

def num2(array):

    output = []
    carry = 1

    for n in range(len(array)-1, -1, -1):
        if n == 0 and carry == 1:
            output.append(0)
            output.append(1)
        else:
            if array[n] + carry == 10:
                output.append(0)
                carry = 1
            else:
                output.append(array[n] + carry)
                carry = 0
    print(output[::-1])

num2([1,2,3,4,5,6])
