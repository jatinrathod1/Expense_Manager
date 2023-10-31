class Customer():
    def __init__(self) -> None:
        self.name = ""
        self.email = ""
        self.password = ""
        self.grocerry = 0
        self.personal = 0
        self.utility = 0

    def sign_up(self):
        self.name = input("Enter the name : ")
        self.email = input("Enter the Email : ")
        self.password = input("Enter the password : ")

        if self.email.count('@') == 1 and self.email.count('.') == 1 and self.email.endswith('.') == False:
            return 1
        else:
            return 0

    def login(self, userid, paswd):
        return self.email == userid and self.password == paswd

    def personal_expence(self, amount):
        self.personal += amount

    def grocerry_expence(self, amount):
        self.grocerry += amount

    def utility_expence(self, amount):
        self.utility += amount


list1 = []
while True:
    print("1 --- Sign-Up")
    print("2 --- Login")
    print("3 --- Show Customers")
    print("4 --- Exit")

    Choice = int(input("Enter Choice : "))

    if Choice == 1:
        c = Customer()
        if c.sign_up():
            list1.append(c)

    elif Choice == 2:
        userid = input("Enter the user ID : ")
        passwordd = input("Enter the password : ")

        for x in list1:
            if x.login(userid, passwordd):
                flag = 1
                while True:
                    print("1 ---- Grocerry Expense")
                    print("2 ---- Personal Expense")
                    print("3 ---- Utility Expense")
                    print("4 ---- Show Expenses")
                    print("5 ---- Back to Dashboard")

                    ex_choice = int(input("Enter Expense Choice : "))

                    if ex_choice == 1:
                        amt = int(input("Enter Expense Value: "))
                        x.grocerry_expence(amt)

                    elif ex_choice == 2:
                        amt = int(input("Enter Expense Value: "))
                        x.personal_expence(amt)
                    elif ex_choice == 3:
                        amt = int(input("Enter Expense Value: "))
                        x.utility_expence(amt)
                    elif ex_choice == 4:
                        print(
                            f"Values are add Below \ngrocerry value :{x.grocerry}\npersonal value :{x.personal}\nutility value :{x.utility}")
                    elif ex_choice == 5:
                        break

        if flag == 0:
            print("Cred Invalid")
    elif Choice == 3:
        for d in list1:
            print(d.name)
    elif Choice == 4:
        exit()
