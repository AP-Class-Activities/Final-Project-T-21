class wallet :
    def __init__(self, balance):
        self.__balance = balance
    
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self,value): 
        self.__balance = value
       
    def __add__ (self, value):
        return self.__balance + value
    
    def __iadd__ (self, value):
        return self.__balance += value
    
    def __sub__ (self, value):
        if (self.__balance-value)<0:
            raise ValueError('There is not enough balance in your account!')
        return self.__balance - value
    
    def __isub__ (self, value):
        if (self.__balance-value)<0:
            raise ValueError('There is not enough balance in your account!')
        return  self.__balance -= value
    
    def __eq__(self, wallet2):
        return self.__balance == wallet2.__balance

    def __ne__(self, value):
        return self.__balance != value

    def __gt__ (self, value):
        return self.__balance > value

    def __ge__ (self, value):
        return self.__balance >= value
     
    def __lt__ (self, value):
        return self.__balance < value

    def __le__ (self, value):
        return self.__balance <= value