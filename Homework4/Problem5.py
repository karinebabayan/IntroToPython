menu = ['ice cream', 'chocolate', 'apple crisp', 'cookies']
for x in menu:
    desert = input('Choose a desert: ')
    if desert not in menu:
        print('Please choose another desert')       
    else:
        print('Your desert will arrive in 10 minutes')
        break