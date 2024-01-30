#Simple class with no functionality
class Item():
    '''
    Simple empty class named Item with single method 
    to calculate total price
    '''
    def calc_tot_price(self,price,quantity):
        return price * quantity


item1 = Item() #Creating an instance of the class
item1.name = "Phone"
item1.price = 1000
item1.quantity = 5 
print(item1.calc_tot_price(item1.price,item1.quantity))