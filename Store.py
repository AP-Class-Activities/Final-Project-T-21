from Person import person
from Seller import seller
from Customer import customer
from Operator import operator
import pickle
class store:
    def __init__(self, name, address,sendtimetostores, sellers=[], customers=[], operators=[] ):
        self.__name = name
        self.__address = address
        self.__sendtimetostores = sendtimetostores
        self.__seller_file = r'data\{}_sellers.dat'.format(self.__name)
        self.__customer_file = r'data\{}_customers.dat'.format(self.__name)
        self.__operator_file = r'data\{}_operators.dat'.format(self.__name)
        self.__sellers = sellers
        self.__customers = customers
        self.__operators = operators

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value): 
        self.__name = value

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self,value): 
        self.__address = value
        
    @property
    def sendtimetostores(self):
        return self.__sendtimetostores
    @sendtimetostores.setter
    def sendtimetostores(self,value): 
        self.__sendtimetostores = value
    
    @property
    def sellers(self): 
        return self.__sellers
    
    @property
    def customers(self): 
        return self.__customers
    
    @property
    def operators(self): 
        return self.__operators

    def __save_sellers(self): 
        with open(self.__seller_file, 'wb') as file:
            pickle.dump(self.sellers, file)

    def __read_sellers(self): 
        with open(self.__seller_file, 'rb') as file:
            self.__sellers = pickle.load(file)

    def __save_customers(self): 
        with open(self.__customer_file, 'wb') as file:
            pickle.dump(self.customers, file)
    
    def __read_customers(self): 
        with open(self.__customer_file, 'rb') as file:
            self.__customers = pickle.load(file)
    
    def __save_operators(self): 
        with open(self.__operators_file, 'wb') as file:
            pickle.dump(self.__operators, file)

    def __read_operators(self): 
        with open(self.__operators_file, 'rb') as file:
            self.__operators = pickle.load(file)

    def save_to_file(self): 
        self.__save_customers()
        self.__save_sellers()
        self.__save_operators()

    def read_from_file(self): 
        self.__read_customers()
        self.__read_sellers()
        self.__read_operators()
    
    def __add__(self, element): 
        if type(element) is customer: 
            if element not in self.__customers:
                self.__customers.append(element)
        elif type(element) is seller: 
            if element not in self.__sellers:
                self.__sellers.append(element)
        elif type(element) is operator: 
            if element not in self.__operators:
                self.__operators.append(element)
        else: 
            raise ValueError('the element you want to add should be of types [customers, sellers, oprators]')
        
        return self
    
    def __sub__(self, element): 
        if type(element) is customer: 
            if element  in self.__customers:
                self.__customers.remove(element)
        elif type(element) is seller: 
            if element  in self.__sellers:
                self.__sellers.remove(element)
        elif type(element) is operator: 
            if element  in self.__operators:
                self.__operators.remove(element)
        else: 
            raise ValueError('the element you want to add should be of types [customers, sellers, oprators]')
        
        return self

    def __str__(self): 
        S += '\nStore Name: {}    address: {}   send time to other stores:{}'.format(self.name, self.address, self.sendtimetostores)
        S += '\n\n____________________________________________operators___________________________________________________\n\n'
        
        for i in self.operators: 
            S += '%s\n'%(i) 
        
        S += '\n\n____________________________________________customers___________________________________________________\n\n'        
        for i in self.customers:
            S += '%s\n'%(i) 
        
        S += '\n\n____________________________________________sellers___________________________________________________\n\n'        
        for i in self.sellers:
            S += '%s\n'%(i) 
        return S

store1 = store('store1',{'city':'rasht', 'street':'namjo', 'no':12},{'store2':'2d'})
store2 = store('store2',{'city':'rasht', 'street':'moalem', 'no':35},{'store1':'2d'})
print (store1)
print (store2)