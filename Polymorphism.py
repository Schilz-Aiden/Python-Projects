
#parent class
class User:
    name = "Aiden"
    email = "aidenschilz5@gmail.com"
    password = "12345abc"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if(entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")

#Child class 
class Employee(User):
    base_pay = 11.00
    department = "General"
    pin_number = "3980"

#Using the same method as the user class but using entry_pin instead.

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter your pin: ")
        if(entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The pin or email is incorrect")


#Child class 
class Backup(User):
    backup_code = "576432"

#Using the same method as user class but using a entry_code instead as a backup.
    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_code = input("Enter your backup code: ")
        if(entry_email == self.email and entry_code == self.backup_code):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The backup code or email is incorrect")
#The following codes invokes the methods inside each class for User and Employee.

customer = User()
customer.getLoginInfo()

manager = Employee()
manager.getLoginInfo()

recovery = Backup()
recovery.getLoginInfo()
