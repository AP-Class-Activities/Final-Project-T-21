
from person import person
class customer (person):
    def __init__(name, lastname, username, sex, phone_numer, national_id, password, address, email, bank_account ,id ):
        super(customer,self).__init__(name, lastname, username, sex, phone_numer, national_id, password, address, email, bank_account)
        self.__id = id
    
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,value): 
        if : 
            raise ValueError('')
        self.__id = value

    @property
    def (self):
        return self.__
    @.setter
    def (self,value): 
        if : 
            raise ValueError('')
        self.__ = value
    
    @property
    def (self):
        return self.__
    @.setter
    def (self,value): 
        if : 
            raise ValueError('')
        self.__ = value
       
