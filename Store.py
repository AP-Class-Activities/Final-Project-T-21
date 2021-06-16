from Person import person 
from Seller import seller
from Customer import customer
from Operator import operator
import pickle
class store:
    def __init__(self, name, addres, sellers=[], customers=[], operators=[] ):
        self.__name = name
        self.__addres = addres
        self.__seller_file = r'data\{}_sellers.dat'.format(self.__############)
        self.__customer_file = r'data\{}_customers.dat'.format(self.__############)
        self.__operator_file = r'data\{}_operators.dat'.format(self.__############)
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
    def addres(self):
        return self.__addres
    @addres.setter
    def addres(self,value): 
        self.__addres = value
    
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

