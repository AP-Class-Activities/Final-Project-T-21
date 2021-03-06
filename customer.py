# from os import close
from Person import person
from Wallet import wallet
from Cart import cart
from Product import Product
import pickle

class customer (person):
    def __init__(self, name, lastname, username, sex, phone_numer, national_id, password, address, email, bank_account, wallet=wallet(), cart=cart(), favorites=[], previous_orders=[], returned_products=[], gift_cards=[] ):
        super(customer,self).__init__(name, lastname, username, sex, phone_numer, national_id, password, address, email, bank_account)
        self.__wallet = wallet
        self.__cart = cart
        self.__favorites = favorites
        self.__previous_orders = previous_orders
        self.__returned_products = returned_products
        self.__gift_cards = gift_cards
    



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
        if value is not Product: 
            raise ValueError('the type of value should be product')
        self.__favorites = value
    
    @property
    def previous_orders(self):
        return self.__previous_orders
    @previous_orders.setter
    def previous_orders(self,value): 
        if value is not Product: 
            raise ValueError('the type of value should be product')
        self.__previous_orders = value
    
    @property
    def returned_products(self):
        return self.__returned_products
    @returned_products.setter
    def returned_products(self,value): 
        if value is not Product: 
            raise ValueError('the type of value should be product')
        self.__returned_products = value

    @property
    def gift_cards(self):
        return self.__gift_cards
    @gift_cards.setter
    def gift_cards(self,value): 
        self.__gift_cards = value
    
    def id(self):
        for i in ['store1','store2']:
            file_name =r'data\{}_customers.dat'.format(i)
            with open(file_name, 'rb') as file:
                customers = pickle.load(file)  
            for j in customers:
                if j.id == 'CU'+ self.__national_id[3:-1]:
                    raise ValueError('custumer account with this national id already exist.')
            file.close
        return 'CU'+ self.__national_id[3:-1]
    
    def __str__(self):
        return super(person,self).__str__() 

    def __del__(self):
        print ('account of {} {} (id= {}) deleted.'.format(self.name , self.lastname, id))




c = customer ('seller','sellri','some username','female',['09158088635','05139141838'],'2680330668','12345','adress','gmail@gmail.com','1234567891234567')
print(c)   

