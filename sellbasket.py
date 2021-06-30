from Product import Product

class sellbasket:
   def __init__(self , amount=0 , item=[] ):
       if amount < 0:
          raise ValueError('The value of amount should be positive.')
       self.__amount = amount
       self.__item = item 
       self.__total = total
       self.__totalrejected = totalrejected
       self.__totalsold = totalsold

   def additem(self , name , amount=0):
        self.__item.update({name:amount})
        return self.__items

   def solditem(self , name , amount=0 , price , totalsold=0 ):
       self.__items[name] -= amount
       self.__totalsold += price * amount
       return self.__items , self.__totalsold

   def rejecteditem(self , name , amount=0 , price , totalrejected=0)
       self.__items[name] += amount
       self.__totalrejected += price * amount
       return self.__items , self.__totalrejected  

    

   # Setters & Getters

   @property
   def total(self):
      return self.__total
     
   @total.setter
   def total(self,value): 
      self.__total = value

   @property
   def totalsold(self):
      return self.__total
     
   @total.setter
   def totalsold(self,value): 
        self.__total = value

   @property
   def totalrejected(self):
      return self.__total
     
   @total.setter
   def totalrejected(self,value): 
      self.__total = value

   @property
   def item(self):
      return self.__item
     
   @item.setter
   def item(self,value):
      if  type(value) is not Product:
         raise ValueError('the type of value should be product') 
      self.__item.append(value)

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
       

