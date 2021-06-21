import person from person

class operator:
    def __init__(self , name, lastname, username, sex, phone_numer, national_id, password, address, email, bank_account , distance , new_customer , new_operator , new_Product , status):
    super(operator,self).__init__(name, lastname, username, sex, phone_numer, national_id, password, address, email, bank_account)
       self.__distance = distance
       self.__new_Product = new_Product
       self.__new_customer = new_customer
       self.__operator = new_operator
       self.__status = status


    @property
    def distance(self):
        return self.__distance
     
    @distance.setter
    def distance(self,value): 
        self.__distance = value


