from person import person
import pickle

class operator:
    def __init__(self , name, lastname, username, sex, phone_numer, national_id, password, address, email, bank_account , new_customer , new_operator , new_Product , status="checking"):
        super(operator,self).__init__(name, lastname, username, sex, phone_numer, national_id, password, address, email, bank_account , nearest_store = None)
        self.__new_Product = new_Product
        self.__new_customer = new_customer
        self.__new_operator = new_operator
        self.__status = status

    def check_status (self , status):
        if status == "accepted" :
            self.__person.update
            return self.__person

        elif status == "unaccepted" :
            del self.__person
            return self.__person


    @property
    def distance(self):
        return self.__distance
     
    @distance.setter
    def distance(self,value): 
        self.__distance = value

    @property
    def new_Product(self):
        return self.__new_Product
     
    @new_Product.setter
    def new_Product(self,value): 
        self.__new_Product = value

    @property
    def new_customer(self):
        return self.__new_customer
     
    @new_customer.setter
    def new_customer(self,value): 
        self.__new_customer = value

    @property
    def new_operator(self):
        return self.__new_operator
     
    @new_operator.setter
    def new_operator(self,value): 
        self.__new_operator = value

    @property
    def status(self):
        return self.__status
     
    @status.setter
    def status(self,value): 
        self.__status = value

    def id(self):
        for i in ['store1','store2']:
            file_name =r'data\{}_operators.dat'.format(i)
            with open(file_name, 'rb') as file:
                operators = pickle.load(file)  
            for j in operators:
                if j.id == 'OP'+ self.__national_id[3:-1]:
                    raise ValueError('operator account with this national id already exist.')
            file.close
        return 'OP'+ self.__national_id[3:-1]


    def __str__(self):
        return super(person,self).__str__() +' new_customer: {}  new_operator:{} new_product:{}'.format(self.new_customer, self.new_operator , self.new_Product)
    
    def __del__(self):
        print ('{} {} with (id= {}) deleted.'.format(self.name , self.lastname, self.id))



    

    


