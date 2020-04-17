products ={"candy": 10, "juice": 5, "pen": 50}

def check(product, num):
    
    if (product in products.keys()) and (products.values()>=num):
        return True
    else: 
        return False