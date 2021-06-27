from Person import person
from Wallet import wallet
from Cart import cart
from Prodoct import prodoct
import os

class customer (person):
    def __init__(self, name, lastname, username, sex, phone_numer, national_id, password, address, email, bank_account, id, wallet=None, cart=None, favorites=[], previous_orders=[], returned_products=[], gift_cards=[] ):
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
        if os.path.exists('CU{}.txt'.format(self.__national_id[3:-1])):
            raise ValueError('custumer account with this national id already exist.')
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

    def __del__(self):
        print ('account of {} {} (id= {}) deleted.'.format(self.name , self.lastname, self.id))

#  سه تا متد پایین با کل فایل کار میکنه (مثلا همه کاستومرا پاک میشن)
    def save_informations (self):
        file_name = '{}.txt'.format(self.national_id)
        f = open(file_name, 'a+')
        lst={
             '{}'.format(self.username):
                {'name':self.name,'lastname':self.lastname,
                'username':self.username,'sex':self.sex,'phone_numer':self.phone_numer,
                'national_id':self.national_id,'password':self.password,'address':self.address,
                'email':self.email,'bank_account':self.bank_account,'id':self.id,
                'wallet':self.wallet,'cart':self.cart,'favorites':self.favorites,
                'previous_orders':self.previous_orders,'returned_products':self.returned_products,
                'gift_cards':self.gift_cards}
            }
        # f.write('{} ={}'.format(self.id, lst))
        file.write('{')
        for self.username, data in lst.items():
           file.write('\'' + username + '\':' + str(data) + ',')
        file.write('}')
        f.close()

    def read_informations (self):
        f = open("customers.txt", "r")
        contents = f.read()
        print(contents)
        f.close()

    def delet_informations(self):
        f = open('dataBase.txt', 'a+')
        f.truncate(0)




