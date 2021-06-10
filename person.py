class person:
    def __init__(self, name, lastname, username, sex, phone_number, national_id, password, address, email, bank_account, nearest_store):
        self.__name = name
        self.__lastname = lastname
        self.__username = username
        self.__sex = sex
        self.__phone_number = phone_number
        self.__national_id = national_id
        self.__password = password
        self.__address = address
        self.__email = email
        self.__bank_account = bank_account
        self.__nearest_store = nearest_store
    
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
    def lastname(self):
        return self.__lastname
    @lastname.setter
    def lastname(self,value):
        for i in value:
            if i in ('~`!@#$%^&*()_-+=|\?/><.,1234567890"[]}{:;'+"'") :
                 raise ValueError('you cant use number or ~`!@#$%^&*()_-+=|\?/><.,1234567890"[]}{:;'+"'"+' for lastname.')
        self.__lastname = value
    
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self,value):
        self.__username = value

    @property
    def sex(self): 
        return self.__sex
    @sex.setter
    def sex(self,value): 
        if value not in ['male', 'female']: 
            raise ValueError('the value of sex should be male or female.')
        self.__sex = value

    @property
    def phone_number(self):
        return self.__phone_number
    @phone_number.setter
    def phone_number(self,value):
        if len(value)!=11:
            raise ValueError('phone number should have 11 digits')
        self.__phone_number = value

    @property
    def national_id(self):
        return self.__national_id
    @national_id.setter
    def national_id(self,value):
        if len(value)!=10:
            raise ValueError('national id should have 10 digits')
        self.__national_id = value
    
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self,value):
        if len(value)<4 or len(value)>10:
            raise ValueError('password should have 4 to 10 digits or Letters')
        self.__password = value
    
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self,value):
        self.__address = value
    
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self,value):
        self.__email = value
    
    @property
    def bank_account(self):
        return self.__bank_account
    @bank_account.setter
    def bank_account(self,value):
        if len(value)!=16:
            raise ValueError('bank account should have 16 digits')
        self.__bank_account = value
    
    @property
    def nearest_store(self):
        return self.__nearest_store
    @nearest_store.setter
    def nearest_store(self,value): 
        self.__nearest_store = value


    
    def __str__(self):
         return 'name: {}   lastname{}   user name: {}   sex:{}   phone number: {}   national id: {}   default address: {}   email: {}   default bank_account:{}   nearest store:{}'\
             .format(self.name, self.lastname, self.username, self.sex, self.phone_number, self.national_id,self. address, self.email, self.bank_account, self.nearest_store)
        

