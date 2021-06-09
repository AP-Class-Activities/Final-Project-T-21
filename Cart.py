class cart:
    def __init__(self , amount = 0 , total = 0 , items = {}):
         self.__total = total
         self.__items = items

         if amount < 0:
            raise ValueError('The value of amount should be positive.')
         self.__amount = amount


    def add_item(self , name , amount , price):
        self.__total += price * amount
        self.__items.update({name:amount})
        return self.__total , self.__items

    def remove_item(self , name , amount , price):
        if name in self.__items:
            if amount < self.__items[name] and amount > 0:
                self.__items[name] -= amount
                self.__total -= price * amount
            elif amount >= self.__items[name]:
                self.__total -= price * self.__items[name]
                del self.__items[name]
            return self.__items , self.__total

    def checkout(self , wallet):
            if wallet >= self.__total:
                return wallet - self.__total
            else:
                return "Cash paid not enough"

    # Setters & Getters

    @property
    def total(self):
        return self.__total
     
    @total.setter
    def total(self,value): 
        self.__total = value

    @property
    def items(self):
        return self.__items
     
    @items.setter
    def items(self,value): 
        self.__items = value

    @property
    def name(self):
        return self.__name
     
    @name.setter
    def name(self,value): 
        self.__name = value

    @property
    def amount(self):
        return self.__amount
     
    @amount.setter
    def amount(self,value):
        if value < 0:
            raise ValueError('The value of amount should be positive.')
        self.__amount = value

    @property
    def price(self):
        return self.__price
     
    @price.setter
    def price(self,value): 
        self.__price = value

    @property
    def wallet(self):
        return self.__wallet
     
    @wallet.setter
    def wallet(self,value): 
        self.__wallet = value


