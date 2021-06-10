from customer import customer
from Product import product

class sellbasket:
    def init(self , aproduct , sproduct , aamount , samount , rproduct , ramount):
       self.__aproduct = aproduct 
       if aamount<0:
          print("amount should be positive number")
       self.__aamount = aamount
       self.__sproduct = sproduct 
       self.__samount = samount
       self.__rproduct= rproduct
       self.__ramount = ramount


    def depot(self , aproduct , aamount): 
       self[aproduct] = [aamount]
    
    def sold(self , sproduct , samount):
       self[sproduct] = [samount]

    def rejected(self , rproduct , ramount):
      self[rproduct] = [ramount]