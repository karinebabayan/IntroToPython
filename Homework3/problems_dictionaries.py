market = {'dairy': ['yogurt', 'cheese'],'fruits': ['banana', 'apple', 'orange', 'lemon', 'apple', 'banana', 'banana']}
print('Market before changes: ', market)
market['candies'] = ['mars', 'kinder', 'twix'] 
market['fruits'].sort()
print('Market sorted:', market)
del market['fruits'][3:5]
print('Market after chhanges: ', market)