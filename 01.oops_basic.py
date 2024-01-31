#Simple class with no functionality
class Item():
    '''
    Simple empty class named Item with single method 
    to calculate total price
    '''

    def __init__(self,name: str,price: float,quantity: int): #Constructor 
        self.name = name
        self.price = price
        self.quantity = quantity

    def calc_tot_price(self):
        '''
        Function to calculate the total price of item, 
        price of product * quantity
        '''
        return self.price * self.quantity


item1 = Item("Phone",1000,10) #Creating an instance of the class
print(item1.calc_tot_price())