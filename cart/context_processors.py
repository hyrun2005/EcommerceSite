from .cart import Cart


#create context processor
def cart(request):
    #return default data from Cart
    return {'cart': Cart(request)}