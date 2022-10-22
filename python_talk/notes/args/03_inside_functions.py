'''
The visibility of the change depends on the type of argument passed into a function.
Changes to mutable objects inside a function will be visible outside, while
they will not be visible for immutable objects 

'''


def place_order(cargo_weight, free_shipping):
    
    free_shipping = True if cargo_weight > 10 else False 
    
free_shipping = False 
print(f"Free shipping status before placing the order order: {free_shipping}") # False

place_order(20, free_shipping)
print(f"Free shipping status after processing an eligible order: {free_shipping}") # False




def checkout_cart(shopping_cart):
    """ puts a free gift for shoppers who spend $100 or more """
    total = sum(shopping_cart)
    if total >= 100:
        shopping_cart.append('free gift')


cart = [50,50,50]
print(f"Shopping cart prior to checkout: {cart} ") # [50,50,50]
checkout_cart(cart)
print(f"Shopping cart after checkout: {cart}") # [50,50,50,"free gift"]
