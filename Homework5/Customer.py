import Productcheck

def buy(product, num, price):
    if Productcheck.check(product,num):
        print('You bought %s and spent %d'%(product, num*price))
    else:
        print('Sorry! We are out of this product.')

def main():
    product = input("Choose a product: ")
    num = input("Quantity: ")
    price = input("Price: ")
    buy(product, num, price)
    
if __name__ == '__main__':
    main()