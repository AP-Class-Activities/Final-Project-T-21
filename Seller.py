from person import person

class seller (person):
    def __init__(name, lastname, username, sex, phone_numer, national_id, password, address, email, bank_account ,company_name, store, id, rate , activity ,sendingtimetostore ):
        super(seller,self).__init__(name, lastname, username, sex, phone_numer, national_id, password, address, email, bank_account)
        self.__company_name = company_name
        self.__id = id
        self.__rate = rate
        # self.__activity = activity
        self.__sendingtimetostore = sendingtimetostore

    @property
    def company_name(self):
        return self.__company_name
    @company_name.setter
    def company_name(self,value): 
        self.__company_name = value
    
    
    
    # @property
    # def id(self):
    #     return self.__id
    # @id.setter
    # def id(self,value): 
    #     if : 
    #         raise ValueError('')
    #     self.__id = value
    
    # @property
    # def (self):
    #     return self.__
    # @.setter
    # def (self,value): 
    #     if : 
    #         raise ValueError('')
    #     self.__ = value
    
    # @property
    # def (self):
    #     return self.__
    # @.setter
    # def (self,value): 
    #     if : 
    #         raise ValueError('')
    #     self.__ = value

    # @property
    # def rate(self):
    #     return self.__rate
    # @rate.setter
    # def rate(self,value): 
    #     if rate not in (1,2,3,4,5): 
    #         raise ValueError('The value of rating should be between 1 to 5.')
    #     self.__rate = value

    # @property
    # def activity(self):
    #     return self.__activity
    # @activity.setter
    # def activity(self,value): 
    #     if activiy<1900 or activity>2021:
    #         raise ValueError('Activity date is not vali.')
    #     self.__activity = value   

    # @property
    # def sendingtimetostore(self):
    #     return self.__sendingtimetostore
    # @sendingtimetostore.setter
    # def sendingtimetostore(self,value): 
    #     # value = Depot_interval + Destination_interval
    #     self.__sendingtimetostore = value 