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
