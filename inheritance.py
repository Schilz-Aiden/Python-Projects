#The parent class that has basic attributes for the child classes to use
class User:
    name = 'No Name Provided'
    email = ''
    password = 'password12345'
    account_number = 0
#A child class that inherit all data from the
#User class and also have their own attribute
class Employee(User):
    base_pay = 15.00
    department = 'General'
#A child class that inherit all data from the
#User class and also have their own attribute
class Customer(User):
    mailing_address = ''
    mailing_list = True
