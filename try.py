class mpesa ():
    def __init__(self,account_balance,phone_number) :
       self.account_balance=account_balance
       self.phone_number=phone_number

    def send_money(self,amount,recipient):
        if self.account_balance>=amount:
            self.account_balance-=amount 
            print(f"{amount}kes sent to {recipient} successfully")

        else:
            print("insufficient funds")

class credo(mpesa):
    def __init__(self, account_balance, phone_number,Id_number):
        super().__init__(account_balance, phone_number)
        self.Id_number=Id_number
    def buy_airtime(self,amount) :
        if self.account_balance>=amount:
           self.account_balance-=amount 
           print(f"{amount}kes airtime bought successfully")
        else:
            print ("inmsufficient funds") 

class bussiness_mpesa(mpesa) :
    def __init__(self, account_balance, phone_number,bussiness_name):
        super().__init__(account_balance, phone_number)  
        self.bussiness_name=bussiness_name

    def receive_money(self,amount):
        self.account_balance+=amount
        print(F"{amount} kes received successfully")

personal=credo(500,713509121,263314195)
personal.send_money=(300,87654321)
personal.buy_airtime=(50)
biz=bussiness_mpesa(2000,713509121,"onaires")
biz.receive_money(3000)
biz.send_money(1500,87654321)





class agriculture :
    def __init__(self,rearing,planting) :
        self.rearing=rearing
        self.planting=planting

    def tuposite (self):
        return "f my job is {rearing} and {planting}"
    
    
    #creating instances of the agriculture class
agriculture1 =agriculture("goats","cabbages")
agriculture2=agriculture("sheep","sukumawiki")

#using methods of class instances
print(agriculture1.tuposite()) #my job is rearing goat and planting cabbages
print(agriculture2.tuposite()) #my job is rearing sheep and planting sukumawikipython






class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def info(self):
        return f"{self.title} by {self.author}, {self.pages} pages."

# Creating instances of the Book class
book1 = Book("Harry Potter", "J.K. Rowling", 400)
book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", 250)

# Using methods of class instances
print(book1.info())  # Output: Harry Potter by J.K. Rowling, 400 pages.
print(book2.info())  # 

class prolife:
    def __init__(self,vision,mission) :
        self.vision=vision
        self.mission=mission

    def club(self):
        return f" it is our role to {self.vision} and {self.mission} life upto natural death"
    
prolife1=prolife("protect", "promote  ") 
prolife2=prolife("defend","preserve")    

print (prolife1.club())
print (prolife2.club())

class person:
    def __init__(self,firstname,secondname):
        self.firstname=firstname
        self.secondname=secondname
    def printname(self):
        print(self.firstname,self.secondname)
    
x=person("alice","sammy")       
x.printname()


class student(person):
    def __init__(self, firstname, secondname,year):
        super().__init__(firstname, secondname)
        self.graduationyear=year

    def welcome(self):
        print("welcome",self.firstname,self.secondname ,"to the class of" ,self.graduationyear)

x=student("oliva","ndungu",2024)
x.welcome()



  
