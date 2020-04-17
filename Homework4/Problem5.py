menu = ['ice cream', 'chocolate', 'apple crisp', 'cookies']
desert = input("Input your desert: ")

while desert not in menu:
    print("Please choose another desert")
    desert = input("Input your desert: ")
else:
    print("Your desert will arrive in 10 minutes")
    
"""
menu = ['ice cream', 'chocolate', 'apple crisp', 'cookies']

for i in range(10):
    desert = input("Input your desert: ")
    if desert in menu:
        print("Your desert will arrive in 10 minutes")
        break
"""