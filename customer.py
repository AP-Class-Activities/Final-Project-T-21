from Person import person
from Wallet import wallet

class customer (person):
    def __init__(self, name, lastname, username, sex, phone_numer, national_id, password, address, email, bank_account , id, wallet=None):
        super(customer,self).__init__(name, lastname, username, sex, phone_numer, national_id, password, address, email, bank_account)
        self.__id = id
        # self.__wallet = wallet
    
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self):
        #  with open(self.__customer_file, 'rb') as file:
        #      if self.__national_id == pickle.load(file):
        #          raise ValueError('')
            
         self.__id = 'CU'+ self.__national_id[3:-1]

    # @property
    # def wallet(self):
    #     return self.__wallet
    # @wallet.setter
    # def wallet(self,value): 
    #      self.__wallet = value
    
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