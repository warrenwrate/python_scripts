


def memo_one(n):
    if n == 0 or n == 1:
        return n
    else:
        print(n)
        return memo_one(n - 1) + n

m1 = memo_one(3)
print('last value',m1)

def perm(s):

    output = []
    
    if len(s) == 1:
        output = [s]

    else:
        for i, l in enumerate(s):
            print(s[:i], s[i + 1:])
            #_bc, a_c, ab_
            for p in perm(s[:i] + s[i+1:]):
                print('perm val', l, p)
                output += [l + p]
    return output

prm = perm('abcd')

print(prm)


