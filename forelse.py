

word = 'word'

# for else will run else statement only if the loop finishes
# if it doesn't complete, then else statement will not run
for l in word:
    print('letter is ', l)
else:
    print('end - else', l)


print('\ntry statement')

for i in range(0, len(word) + 5):
    try:
        if word[i] != 'd':
            print('letter is ', word[i])
    except:
        print( 'error index', i)
    else:
        print('was not an error', word[i])
else:
    print('end - with break', i)
