class Product:
    def __init__(self, name , price , amount , availability , product_ID , discount , rating , specifications = {} ,  comments = {}):
        
        if product_ID > 999999 or product_ID < 100000:
            raise ValueError('The product ID should be contain six characters.')
        self.__product_ID = product_ID
        
        self.__name = name

        if amount < 1:
            raise ValueError('Item out of stock')
        self.__availability = availability

        self.__specifications = specifications

        if price < 0:
            raise ValueError('The value of price should be positive.')
        self.__price = int(price)

        if amount < 0:
            raise ValueError('The value of amount should be positive.')
        self.__amount = int(amount)

         if rating not in [1,2,3,4,5]: 
            raise ValueError('The value of rating should be from 1 to 5.')
        self.__rating = rating

        self.__comments = comments

        if discount < 0:
            raise ValueError('The value of discount should be positive.')
        self.__discount = int(discount)


    ## Setters & Getters

    @property
    def name(self):
        return self.__name
     
    @name.setter
    def name(self,value): 
        self.__name = value

    @property
    def product_ID(self):
        return self.__product_ID
     
    @product_ID.setter
    def product_ID(self,value): 
        if product_ID > 999999 or product_ID < 100000:
            raise ValueError('The product ID should be contain six characters.')
        self.__product_ID = value

    @property
    def amount(self):
        return self.__amount
     
    @amount.setter
    def amount(self,value):
        if amount < 0:
            raise ValueError('The value of amount should be positive.')
        self.__amount = value

    @property
    def specifications(self):
        return self.specifications
     
    @specifications.setter
    def specifications(self,value): 
        self.specifications = value

    @property
    def price(self):
        return self.__price
     
    @price.setter
    def price(self,value):
        if price < 0:
            raise ValueError('The value of price should be positive.')
        self.__price = value
   
    @property
    def rating(self):
        return self.__rating
     
    @rating.setter
    def rating(self,value): 
        if rating not in [1,2,3,4,5]: 
            raise ValueError('The value of rating should be from 1 to 5.')
        self.__rating = value

    @property
    def comments(self):
        return self.__comments
     
    @comments.setter
    def comments(self,value): 
        self.__comments = value

    @property
    def discount(self):
        return self.__discount
     
    @discount.setter
    def discount(self,value):
        if discount < 0:
            raise ValueError('The value of discount should be positive.')
        self.__discount = value

    @property
    def availability(self):
        return self.__availability
     
    @availability.setter
    def availability(self,value):
        if amount < 1:
            raise ValueError('Item out of stock.')
        self.__availability = value
