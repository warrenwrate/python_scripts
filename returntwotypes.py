

def returnMult():

    wordlist = ['Hello', 'World', 'Warren', 'Wrate']
    l = [x for x in range(1, len(wordlist) + 1 )]

    return wordlist, l

a, b = returnMult()

print('a', a)
print('b', b)