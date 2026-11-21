
from abc import ABC, abstractmethod

# Sales data
sales = [
    ["Laptop", "Delhi", 2, 40000],
    ["Mobile", "Noida", 3, 15000],
    ["Headphones", "Delhi", 5, 2000],
    ["Keyboard", "Noida", 4, 1000]
]

# Abstraction
class Shop(ABC):
    @abstractmethod
    def total_sales(self):
        pass


# Main class
class Ecommerce(Shop):

    def display(self):
        for i in sales:
            print(i)

    def total_sales(self):
        total = 0

        for i in sales:
            total = total + i[2] * i[3]

        print("Total Sales = Rs.", total)

    def product_sales(self):
        data = {}

        for i in sales:
            name = i[0]
            amount = i[2] * i[3]

            if name in data:
                data[name] += amount
            else:
                data[name] = amount

        print(data)


# Object
obj = Ecommerce()

# Menu
print("1. Display Sales")
print("2. Total Sales")
print("3. Product Wise Sales")
print("4. Exit")

choice = input("Enter choice: ")

if choice == "1":
    obj.display()

elif choice == "2":
    obj.total_sales()

elif choice == "3":
    obj.product_sales()

elif choice == "4":
    print("Thank You!")

else:
    print("Wrong Choice")
