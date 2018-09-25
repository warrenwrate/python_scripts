# This works
# mdata = 15

# def returndata(data):
#     data += mdata
#     return data

# print(returndata(5))


# This does not work
# mdata = 15

# def returndata(data):
#     mdata += 1
#     data += mdata
#     return data

# print(returndata(5))

# This does work when you set mdata to a global
mdata = 15

def returndata(data):
    global mdata
    mdata +=1
    data += mdata
    return data

print(returndata(5))