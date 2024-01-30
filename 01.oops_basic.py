#Simple class with no functionality
class Item():
    '''
    Simple empty class named Item 
    '''
    pass


item1 = Item() #Creating an instance of the class
item1.name = "Phone"
item1.price = 1000
item1.quantity = 5 

print(type(item1))
print(type(item1.name))
print(type(item1.price))
print(type(item1.quantity))