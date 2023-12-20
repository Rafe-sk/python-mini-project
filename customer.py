class Customer:
    def __init__(self, name, aadhar, age, email, address, yearofbuy, bikechoice):
        self.name = name
        self.aadhar = aadhar
        self.age = age
        self.email = email
        self.address = address
        self.year_of_buy = yearofbuy
        self.bike_choice = bikechoice
    def __str__(self):
        return f"Name: {self.name}\nAadhar Card: {self.aadhar}\nAge: {self.age}\nEmail: {self.email}\nAddress: {self.address}\nBike Choice: {self.bike_choice}\nYear of Purchase: {self.year_of_buy}"