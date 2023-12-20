from bike import Bike
from customer import Customer

class Showroom:
    def __init__(self):
        self.bikesavailable = {
            1: Bike("Royal Enfield Classic 350", 193080),
            2: Bike("Royal Enfield Himalayan 450", 149000),
            3: Bike("Royal Enfield roadster 450 ", 193080),
            4:Bike("Royal Enfield interceptor 650",180000),
            5:Bike("Royal Enfield Meteor 350",943012),
            6:Bike("Royal Enfield Bobber 350",930213),
            7:Bike("Royal Enfield Bullet 350",483902),
            8:Bike("Royal Enfield continental GT 450",92301)
        }
    def welcome_message(self):
        print("*" * 30)
        print("Welcome to Royal Enfield Bike Showroom!")
        print("*" * 30)
    def display_menu(self):
        print("What would you like to do?")
        print("1. Display all bikes")
        print("2. Buy a bike")
        print("3. Exit")
    def display_bikes(self):
        print("Available Bikes:")
        for number, bikeinfo in self.bikesavailable.items():
            print(f"{number}. {bikeinfo}")
    def buy_bike(self):
        self.display_bikes()
        bike_choice = int(input("Choose a bike number from the available options: "))
        if bike_choice in self.bikesavailable:
            name = input("Enter your full name: ")
            aadhar = input("Enter your Aadhar Card number: ")
            age = input("Enter your age: ")
            email = input("Enter your email address: ")
            address = input("Enter your address: ")
            year_of_buy = input("Enter the year of purchase: ")
            customer = Customer(name, aadhar, age, email, address, year_of_buy, self.bikesavailable[bike_choice].name)
            selected_bike = self.bikesavailable[bike_choice]
            print("\nReceipt:")
            print(customer)
            print(f"Selected Bike: {selected_bike.name}")
            print(f"Price: ₹{selected_bike.price}")
        else:
            print("Invalid bike choice. Please choose from the available options.")
    def run_showroom(self):
        self.welcome_message()
        self.display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
                self.display_bikes()
        elif choice == '2':
                self.buy_bike()
        elif choice == '3':
                print("Thank you for visiting our Bike Showroom! Please keep the money in Indian Rupees.")
             
        else:
                print("Invalid choice. Please enter a valid option.")