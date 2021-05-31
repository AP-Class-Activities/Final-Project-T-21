class seller:
    def __init__(name , adress , phone_number , rate , activity ,sending , vallet)
        self.__name = name
        self.__adress = adress
        self.__phone_number = phone_number
        self.__rate = rate
        self.__activity = activity
        self.__sending = sending

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        for i in value:
            if i in ('~`!@#$%^&*()_-+=|\?/><.,1234567890"[]}{:;'+"'"):
                 raise ValueError('you cant use number or ~`!@#$%^&*()_-+=|\?/><.,1234567890"[]}{:;'+"'"+'for name')
        self.__name = value

    @property
    def phone_number(self):
        return self.__phone_number
    @phone_number.setter
    def phone_number(self,value):
        if Number(value)!=11:
            raise ValueError('phone number should have 11 digits')
        self.__phone_number = value

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self,value):
        self.__address = value

    @property
    def rate(self):
        return self.__rate
    @rate.setter
    def rate(self,value): 
        if rate not in (1,2,3,4,5): 
            raise ValueError('The value of rating should be between 1 to 5.')
        self.__rating = value

    @property
    def activity(self):
        return self.__activity
    @rate.setter
    def activity(self,value): 
        if activiy<1900 or activity>2021:
            raise ValueError('Activity date is not vali.')
        self.__rating = value   

    @property
    def sending(self):
        return self.__sending
    @rate.setter
    def sending(self,value): 
        value = Depot_interval + Destination_interval
        self.__rating = value 

    @property
    def vallet(self):
        return self.__vallet
    @rate.setter
    def vallet(self,value): 
        self.__rating = value