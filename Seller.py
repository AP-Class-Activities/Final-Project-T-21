from Person import person
from Wallet import wallet
from import

class seller (person):
    def __init__(self, name, lastname, username, sex, phone_numer, national_id, password, address, email, bank_account ,company_name, id, rate ,sendingtimetostore, wallet=None, ):
        super(seller,self).__init__(name, lastname, username, sex, phone_numer, national_id, password, address, email, bank_account)
        self.__company_name = company_name
        self.__id = id
        self.__rate = rate
        self.__sendingtimetostore = sendingtimetostore
        self.__wallet = wallet
        self.__ =

    @property
    def company_name(self):
        return self.__company_name
    @company_name.setter
    def company_name(self,value): 
        self.__company_name = value
    
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self): 
        self.__id = 'SL'+ self.__national_id[3:-1]

    @property
    def rate(self):
        return self.__rate
    @rate.setter
    def rate(self,value): 
        if value not in [1,2,3,4,5]: 
            raise ValueError('The value of rating should be between 1 to 5.')
        self.__rate = value

    @property
    def sendingtimetostore(self):
        return self.__sendingtimetostore
    @sendingtimetostore.setter
    def sendingtimetostore(self,value): 
        self.__sendingtimetostore = value 
    
    @property
    def wallet(self):
        return self.__wallet
    @wallet.setter
    def wallet(self,value): 
        if type(value) is not wallet : 
            raise ValueError('the type of value should be wallet.')
        self.__wallet = value
    
    @property
    def (self):
        return self.__
    @.setter
    def (self,value): 
        if type(value) is not : 
            raise ValueError('the type of value should be ')
        self.__ = value
   
    
    # @property
    # def (self):
    #     return self.__
    # @.setter
    # def (self,value): 
    #     if : 
    #         raise ValueError('')
    #     self.__ = value

  
    def __str__(self):
        return super(person,self).__str__() +'name: {}'.format(self.company_name)
  

