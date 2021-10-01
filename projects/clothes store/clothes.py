

class Clothes:

        def __init__(self, pieceName, number, price, material):
                self.__pieceName = pieceName
                self.__number = number
                self.__price = price
                self.__material = material

        def get_name(self):
                return self.__pieceName

        def set_name(self, new_pieceName):
                self.__pieceName = new_pieceName

        def get_number(self):
                return self.__number

        def set_number(self, new_number):
                self.__number = new_number

        def get_price(self):
                return self.__price

        def set_price(self, new_price):
                self.__price = new_price

        def get_material(self):
                return self.__material

        def set_material(self, new_material):
                self.__material = new_material



class TShirt(Clothes):
        def __init__(self, pieceName, number, price, material, state):
                super().__init__(pieceName, number, price, material)
                self.__state = state
              
        def get_state(self):
                return self.__state

        def set_state(self, new_state):
                self.__state = new_state


