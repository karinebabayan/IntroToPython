list4 = [[10, 20, 40], [40, 50, 60],[70, 80, 90]]
'''
import copy
list5 = copy.deepcopy(list4)
for i in range(len(list5)):
    list5[i][-1] = 100
'''
list4 = [i[:2]+[100] for i in list4]
print(list4)
print(list5)