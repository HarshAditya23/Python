#parent class
class Mobile:
    
    #instantiate encapsulation using __
    def __init__(self):
        self.__maxprice = 900
        
    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))
        
    def set_Max_Price(self, price):
        self.__maxprice = price
        
mob = Mobile()
mob.sell()

#change the price
mob.__maxprice = 1000
mob.sell()

#using setter function
mob.set_Max_Price(1000)
mob.sell()

        
        
    
    