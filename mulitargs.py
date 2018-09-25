
#multiple args

def multiple(*args):
    param1 = args[0] 
    param2 = args[1] 
    param3 = args[2] 
    print('args length', len(args))
    print('first:', param1)
    print('second:', param2)
    print('third:', param3)


multiple('Warren', "Wrate", 35)


def whatarekwargs(*args, **kwargs):
    print('kwargs',kwargs)
    print('args',args)

    if 'location' in kwargs:
        print('location:', kwargs['location'])


whatarekwargs(10, 15, name="warren", location='SEA')