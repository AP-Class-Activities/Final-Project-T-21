import person from person

class operator:
    def __init__(self , nearest_store , store_number ):
        self.__nearest_store = nearest_store
        self.__store_number = store_number

    def nearst_store(self):
        print("nearest store is: "+ self.nearst_store)
    
    @property
    def store_number(self):
        return self.__store_number
    @store_number.setter
    def store_number(self,value):
        if len(value)!=11:
            raise ValueError('phone number should have 11 digits')
        self.__store_number = value
    

