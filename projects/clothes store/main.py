

from clothes import Clothes, TShirt
from customer import Customer, DoubleCustomer

# function to calculate the total cost
def cost(list):
    count = [list.count('Shoes'), list.count('Trousers'), list.count('Jackets'), list.count('T-Shirt')]
    prices = [count[0]* shose.get_price(), count[1]* trousers.get_price(), count[2]* jackets.get_price(), count[3]* t_shirt.get_price()]
    tolalCost =0
    for i in range(len(prices) - 1):
	    tolalCost += prices[i]


    shose.set_number(shose.get_number() - count[0])
    trousers.set_number(trousers.get_number() - count[1])
    jackets.set_number(jackets.get_number() - count[2])
    t_shirt.set_number(t_shirt.get_number() - count[3])

    return tolalCost

trousers = Clothes('Trousers', 5, 150, 'jeans')
jackets = Clothes('Jackets', 6, 330, 'denim')
shose = Clothes('Shoes', 3, 180, 'leather')
t_shirt = TShirt('T-Shirt', 10, 200, 'cotton', 'long sleeves')
t_shirt = TShirt('T-Shirt', 12, 200, 'cotton', 'short sleeves')

Customer.greeting()

# Customer 1
purchasesList1 = ['Shoes', 'Trousers', 'Trousers']
totalCost1 = cost(purchasesList1)
RegCustomer1 = Customer('Ahmed', 600, totalCost1 )
print(RegCustomer1.buy(totalCost1))


# Customer 2
purchasesList2 = ['Jackets', 'Trousers']
totalCost12 = cost(purchasesList2)
RegCustomer2 = Customer('Ahmed', 100, totalCost12)
print(RegCustomer2.buy(totalCost12))


# Customer 3 "double"
purchasesList3 = ['T-Shirt', 'Jackets', 'Shoes', 'Shoes']
totalCost13 = cost(purchasesList3)
DoubleCustomer3 = DoubleCustomer('Omar', 2000, totalCost13)
print(DoubleCustomer3.buy(totalCost13))

Customer.show_customers()




