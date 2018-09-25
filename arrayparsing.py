array = [8,13,24,18,65,13,21,9,5,12,4, 73, 29, 62]

print(':-3',array[:-3])  # prints out everything except for last 3 items
print(':3',array[:3])  # prints out beginning to third index
print('::3',array[::3]) # prints out every three items - from beginning to end
print('::-3', array[::-3]) # prints out every three items - from end to beginning
print('-----------------------------------------------------------')

print('-3:',array[-3:])  # only does the last three items
print('3:',array[3:])  # starting from index 3, and get the rest
print('3::',array[3::]) # same as '3:'
print('-3::', array[-3::]) # same as '-3:'

print('-----------------------------------------------------------')

print('-3:-1',array[-3:-1])  # last three except the last one
print('3::-1',array[3::-1]) # starting from index 3 and backwards
print('-3::-1', array[-3::-1]) # goes by everyone one from the third item to the end.


