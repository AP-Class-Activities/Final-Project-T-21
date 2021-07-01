from Product import Product

class sellbasket:
   def __init__(self , amount=0 , item=[] , total = 0):
       if amount < 0:
          raise ValueError('The value of amount should be positive.')
       self.__amount = amount
       self.__item = item 
       self.__total = total

   def additem(self , name , amount=0):
        self.__item.update({name:amount})
        return self.__item

   def solditem(self , name , amount , price):
        if name in self.__item:
            if amount < self.__item[name] and amount > 0:
                self.__item[name] -= amount
                self.__total -= price * amount
            elif amount >= self.__item[name]:
                self.__total -= price * self.__item[name]
                del self.__item[name]
            return self.__item , self.__total

   def rejecteditem(self , name , amount , price):
       if name in self.__item:
            self.__item[name] += amount
            self.__total += price * amount
            return self.__item , self.__total

    

   # Setters & Getters

   @property
   def total(self):
      return self.__total
     
   @total.setter
   def total(self,value): 
      self.__total = value

   @property
   def item(self):
      return self.__item
     
   @item.setter
   def item(self,value): 
      self.__item = value

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