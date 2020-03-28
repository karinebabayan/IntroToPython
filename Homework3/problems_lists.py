a = [1, 4, 5, 7, 8, -2, 0, -1]
print(a[3], a[5])
a_sorted = a.copy()
a_sorted.sort(reverse = True) 
print (a)
print(a_sorted)
print(a_sorted[1:3],a_sorted[2:6])
del a_sorted[2:4] 
print(a_sorted)
b = ['grapes', 'Potatoes', 'tomatoes','Orange', 'Lemon', 'Broccoli', 'Carrot', 'Sausages']
b_sorted = b.copy()
b_sorted.sort()
print(a)
print(b_sorted)
c = a[1:3]+b[4:6]
print(c)
