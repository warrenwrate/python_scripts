import zlib

t = 'warrrrrrrrrrrrrrrrrrrrrrrrrrreeeeeeeeeeennnn'
short = zlib.compress(t.encode('utf-8'))

#decode changes bytes back into string otherwise it will be 'warrrrrrrrrrrrrrrrrrrrrrrrrrreeeeeeeeeeennnn
longer = zlib.decompress(short).decode('utf-8')

print(longer)

