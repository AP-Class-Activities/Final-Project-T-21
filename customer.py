from Person import person
from Wallet import wallet
from Cart import cart
from Prodoct import prodoct
class customer (person):
    def __init__(self, name, lastname, username, sex, phone_numer, national_id, password, address, email, bank_account, id, wallet=None, cart, favorites=[], previous_orders=[], returned_products=[], gift_cards=[] ):
        super(customer,self).__init__(name, lastname, username, sex, phone_numer, national_id, password, address, email, bank_account)
        self.__id = id
        self.__wallet = wallet
        self.__cart = cart
        self.__favorites = favorites
        self.__previous_orders = previous_orders
        self.__returned_products = returned_products
        self.__gift_cards = gift_cards
    
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self):
        #  with open(self.__customer_file, 'rb') as file:
        #      if self.__national_id == pickle.load(file):
        #          raise ValueError('')
            
         self.__id = 'CU'+ self.__national_id[3:-1]

    @property
    def wallet(self):
        return self.__wallet
    @wallet.setter
    def wallet(self,value): 
        if type(value) is not wallet : 
            raise ValueError('the type of value should be wallet.')
        self.__wallet = value
    
    @property
    def cart (self):
        return self.__cart
    @cart.setter
    def cart(self,value): 
        if type(value) is not cart: 
            raise ValueError('the type of value should be cart')
        self.__cart = value

    @property
    def favorites(self):
        return self.__favorites
    @favorites.setter
    def favorites(self,value): 
        if value is not prodoct: 
            raise ValueError('the type of value should be product')
        self.__favorites = value
    
    @property
    def previous_orders(self):
        return self.__previous_orders
    @previous_orders.setter
    def previous_orders(self,value): 
        if value is not prodoct: 
            raise ValueError('the type of value should be product')
        self.__previous_orders = value
    
    @property
    def returned_products(self):
        return self.__returned_products
    @returned_products.setter
    def returned_products(self,value): 
        if value is not prodoct: 
            raise ValueError('the type of value should be product')
        self.__returned_products = value

    @property
    def gift_cards(self):
        return self.__gift_cards
    @gift_cards.setter
    def gift_cards(self,value): 
        # if : 
        #     raise ValueError('')
        self.__gift_cards = value

    # @property
    # def (self):
    #     return self.__
    # @.setter
    # def (self,value): 
    #     if : 
    #         raise ValueError('')
    #     self.__ = value
    
    def __str__(self):
        return super(person,self).__str__() +''