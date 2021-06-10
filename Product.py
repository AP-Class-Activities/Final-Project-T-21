class Product:
    def __init__(self, name , product_ID , model , price , amount , availability , rating , discount = 0, specifications = {} ,  comments = [] , category = {}):
        
        if product_ID > 999999 or product_ID < 100000:
            raise ValueError('The product ID should be contain six characters.')
        self.__product_ID = product_ID
        
        self.__name = name

        if amount < 1:
            raise ValueError('Item out of stock')
        self.__availability = availability

        self.__specifications = specifications

        self.__model = model

        if category not in ['Electronics','Clothing','Health Care','Garden & Outdoor','Books','Collectibles & Fine Art','Home & Kitchen','Toys & Games'] :
            raise ValueError('The category for a product should be in [Electronics','Clothing','Health Care',\
                 'Garden & Outdoor','Books','Collectibles & Fine Art','Home & Kitchen','Toys & Games]')
        self.__category = category

        if price < 0:
            raise ValueError('The value of price should be positive.')
        self.__price = int(price)

        if amount < 0:
            raise ValueError('The value of amount should be positive.')
        self.__amount = int(amount)

        if rating not in [1,2,3,4,5]: 
            raise ValueError('The value of rating should be from 1 to 5.')
        self.__rating = rating

        self.__comments = []

        if discount < 0:
            raise ValueError('The value of discount should be positive.')
        self.__discount = int(discount)
        
    def ovrall_price(self):
        price_after_discount= self.price - self.price * (self.discount/100)
        if price_after_discount < 0:
           raise ValueError('The value of price after discount should be positive.')
        return price_after_discount

    def add_comment(self,str):
        self.comments.append(str)
        
    ## Setters & Getters

    @property
    def product_ID(self):
        return self.__product_ID
     
    @product_ID.setter
    def product_ID(self,value): 
        self.__product_ID = 'pr' + value   

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
    def specifications(self):
        return self.__specifications
     
    @specifications.setter
    def specifications(self,value): 
        self.specifications = value

    @property
    def model(self):
        return self.__model
     
    @model.setter
    def model(self,value): 
        self.__model = value

    @property
    def category(self):
        return self.__category
     
    @category.setter
    def category(self,value):
        if category not in ['Electronics','Clothing','Health Care','Garden & Outdoor','Books','Collectibles & Fine Art','Home & Kitchen','Toys & Games'] :
            raise ValueError('The category for a product should be in [Electronics','Clothing','Health Care',\
                 'Garden & Outdoor','Books','Collectibles & Fine Art','Home & Kitchen','Toys & Games]')
        self.__category = value
        

    @property
    def price(self):
        return self.__price
     
    @price.setter
    def price(self,value):
        if value < 0:
            raise ValueError('The value of price should be positive.')
        self.__price = value
   
    @property
    def rating(self):
        return self.__rating
     
    @rating.setter
    def rating(self,value): 
        if value not in [1,2,3,4,5]: 
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
        if value > 0:
            raise ValueError('The value of discount should be positive.')
        self.__discount = value

    @property
    def availability(self):
        return self.__availability
     
    @availability.setter
    def availability(self,value):
        if value.amount < 1:
            raise ValueError('Item out of stock.')
        self.__availability = value


    def __str__(self):
         return 'name : {}   product_ID : {}   model : {}   price : {}   amount : {}  availability: {}   rating : {}   discount:{}   specifications:{}  comments :{}  category : {}'\
            .format(self.name, self.product_ID, self.model, self.price, self.amount, self.availability ,self.rating, self.discount, self.specifications, self.comments , self.category)
'''
object = Product("name",222222,"model",10000,1,"yes",3,100,"spec","comment","Books")
print(object.ovrall_price())
'''