from clothes import Clothes
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from main import cost


class Customer:

        customerNum =0
        def __init__(self,name, money, totalCost):
                self.__name = name
                self.__money = money
                self.__totalCost = totalCost

                Customer.customerNum += 1


        def get_customerName(self):
                return self.__name

        def set_customerName(self, new_name):
                self.__name = new_name

        def get_money(self):
                return self.__money
        
        def set_money(self, new_money):
                self.__money = new_money

        def get_totalCost(self):
                return self.__totalCost

        def set_totalCost(self, new_totalCost):
                self.__totalCost = new_totalCost
        


        @staticmethod
        def greeting():
                print('Welcome to our store!')

        @classmethod
        def show_customers(cls):
                print(f'There are {Customer.customerNum} customers today')


        def buy(self, totalCost):
                
                if totalCost >= self.get_money() : 
                        return'Sorry, you do\'t have enough money'


                else :
                        charge = self.get_money() - totalCost
                        self.set_money(charge)
                        return f'You pay {totalCost}, and your charge {charge}'



class DoubleCustomer(Customer):
        def __init__(self, name, money, totalCost) :
            super().__init__(name, money, totalCost)
            self.__totalCost = 2*totalCost
