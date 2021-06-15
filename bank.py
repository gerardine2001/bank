from datetime import  datetime
class Bank:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        self.balance=0
        self.loan=0
        self.statement=[]

            
    def show_balance(self):
        return f"Hello {self.name}, your balance is {self.balance}"
    def deposit(self,amount):
        try:
            10 + amount
        except TypeError:
            return f("The amount must be in figures")    
        if amount > 0:
            self.balance+=amount
            now=datetime.now()
            transaction={
                "amount":amount,
                "time":now,
                "narration":"you  have deposited"
            }
            self.statement.append(transaction)
   
            return self.show_balance()
        else:
            return f"Hello {self.name} you can is not enough"
   
    def withdraw(self,amount):
        try:
            13 + amount
        except TypeError:
            return f"The amount must ba in figure"    
        if self.balance<amount:
          return f"Hello {self.name} your balance is{self.balance} you can not withdraw {amount}" 
        else:
            self.balance-=amount
            return f"Hello  {self.name} you have deposited {amount}RWF you can withdraw {self.show_balance()} "
   
    def show_statement(self):
        
        for transaction in self.statement:
              amount=transaction["amount"]
              narration=transaction["narration"]
              time=transaction["time"]
              date=time.strftime("%d/%m/%y")
              print(f"{date} : {narration}  {amount}")
        
              return         
        
    def  borrow(self,amount):
        try:
            12 + amount
        except TypeError:
            return f"The amount must be in figures"           
        if amount<0:
            return f"Hello {self.name} your not allowed to borrow"
        elif self.loan>0:
            return f"hello {self.name} you have a loan already"
        elif amount>=0.1*self.balance:
            return   f"Hello {self.name} you are not qualified to borrow"
        else:
            loan=amount*1.05
            self.loan=loan
            self.balance+=loan
            self.balance+=amount
            now=datetime.now()
            transaction={
                "amount":amount,
                "time":now,
                "narration":"you  have borrowed"
            }
            self.statement.append(transaction)
   
            return f"Hello {self.name} you can borrow this  {amount}"


    def repay(self,amount):
        try:
            10 + amount
        except TypeError:
            return f"The amount must be in figures"    
        if amount<0:
            return f"Hello {self.name} your loan is not valid"
        
        elif amount>self.loan:
            self.loan-=amount
            return f"Hello {self.name} your loan has been decreased {self.loan}"
        else :
            diff=amount-self.loan
            self.loan=0
            self.deposit(diff)
            self.balance+=amount
            now=datetime.now()
            transaction={
                "amount":amount,
                "time":now,
                "narration":"you  have repaid"
            }
            self.statement.append(transaction)
   
            return f"Hello {self.name} your loan is cleared"
    def transfer(self,name,amount):
        try:
            1 + amount
        except TypeError:
            return f"The amount must be in figures"
        # if amount>0:
            fee=amount*0.05
            total=amount+fee
        if total>self.balance:
            return "Your balance {self.balance} and you need atleast {toatl} for this transfer "

           
        else:
            self.balance-=total
            name.deposit(amount)
class Mobile_moneyAccount:
    def __init__(self,name,phone,service_provider):
                Bank__init__(self,name,phone)
                self.service_provider=service_provider

    def buy_airtime(self,amount):
        try :
             10 +amount
        except TypeError:
            return f"The amount should be in figures"
        if amount<0:
            return f"You have but 500 Rwf as an airtime"   
        elif self.balance<amount:
    else:
        self.balance-=amount
        return f"you amount is small"                 
     