market = {'dairy': ['yogurt', 'cheese'],'fruits': ['banana', 'apple', 'orange', 'lemon', 'apple', 'banana', 'banana']}
print('Market before changes: ', market)
market['candies'] = ['mars', 'kinder', 'twix'] 
market['fruits'].sort() #market['fruits'] = sorted(list(set(market['fruits']))) 
print('Market sorted:', market) 
set_market = set(market['fruits'])
market['fruits'] = list(set_market) 
print('Market after chhanges: ', market)