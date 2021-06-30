from Person import person
from Wallet import wallet
from sellbasket import sellbasket
import os

class seller (person):
    def __init__(self, name, lastname, username, sex, phone_numer, national_id, password, address, email, bank_account ,company_name, rate ,sendingtimetostore, wallet=wallet(0), sellbasket=sellbasket(), status='checking' ):
        super(seller,self).__init__(name, lastname, username, sex, phone_numer, national_id, password, address, email, bank_account)
        self.__company_name = company_name
        self.__rate = rate
        self.__sendingtimetostore = sendingtimetostore
        self.__wallet = wallet
        self.__sellbasket = sellbasket
        self.__status = status

    @property
    def company_name(self):
        return self.__company_name
    @company_name.setter
    def company_name(self,value): 
        self.__company_name = value
    

    def id(self):
        if os.path.exists('SL{}.txt'.format(self.__national_id[3:-1])):
            raise ValueError('seller account with this national id already exist.')
        return 'SL'+ self.__national_id[3:-1]

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
    def sellbasket(self):
        return self.__sellbasket
    @sellbasket.setter
    def sellbasket(self,value): 
        if type(value) is not sellbasket: 
            raise ValueError('the type of value should be sellbasket')
        self.__sellbasket = value
   
    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self,value): 
        if value not in ['accepted','unaccepted','checking']: 
            raise ValueError('status could be accepted or unaccepted or checking')
        self.__status = value

    # @property
    # def (self):
    #     return self.__
    # @.setter
    # def (self,value): 
    #     if : 
    #         raise ValueError('')
    #     self.__ = value

  
    def __str__(self):
        return super(person,self).__str__() +'   company name: {}   rate:{}'.format(self.company_name, self.rate)
    
    def __del__(self):
        print ('{} {} seller from {}company (id= {}) deleted.'.format(self.name , self.lastname, self.company_name, id))

    def save_informations (self):
        lst={
             '{}'.format(id):
                {'name':self.name,'lastname':self.lastname,
                'username':self.username,'sex':self.sex,'phone_numer':self.phone_numer,
                'national_id':self.national_id,'password':self.password,'address':self.address,
                'email':self.email,'bank_account':self.bank_account,'id':id,
                'company_name':self.company_name,'rate':self.rate,
                'sendingtimetostore':self.sendingtimetostore,'wallet':self.wallet,
                'sellbasket':self.sellbasket,'status':self.status}
            }
        file = open('sellers.txt','ab+')    
        file.write('{')
        for username, data in lst.items():
           file.write('\'' + username + '\':' + str(data) + ',')
        file.write('}')
        file.close()

S = seller('seller','sellri','some username','female',['09158088635','05139141838'],'2680330668','12345','adress','gmail@gmail.com','1234567891234567','company',2,'3',wallet=(123))
print(S)
