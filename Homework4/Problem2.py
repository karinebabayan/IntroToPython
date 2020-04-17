d = {'name': 'Armen', 'age': 15, 'grades': [10, 8, 8,4, 6, 7]}
mean = sum(d['grades'])/len(d['grades'])
#from statistics import mean mean(grades)
if mean>7:
    print('Good job')
else:
    print('You need to work more')