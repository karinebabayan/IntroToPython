t1 = ( 1, True, 'a', -2, 'Anna')
print('Tuple before deleting: ', t1)
l1 = list(t1)
l1.pop(True)
t1= tuple(l1)
print('Tuple after deleting: ', t1)
t2 = (1, 2, 3, 4, 5)
t3 = t1[:3]+ t2[:4]
print('Tuple 3: 't3)