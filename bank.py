from datetime import date, datetime, time


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
        if self.balance<amount:
          return f"Hello {self.name} your balance is{self.balance} you can not withdraw {amount}" 
        else:
            self.balance-=amount
            return f"Hello  {self.name} you have deposited {amount}RWF you can withdraw {self.show_balance()} "
    def borrow(self,amount):
        self.loan+=amount
        return f"Hello {self.name} you have get a loan {self.loan}"

    def repay(self,amount):                                           
        self.loan-=amount
        return f"Hello {self.name} you have repaid a loan{amount}"


    def show_statement(self):
        for transaction in self.statement:
              amount=transaction["amount"]
              narration=transaction["narration"]
              time=transaction["time"]
              date=time.strf("%d/%m/%y")
              print(f"{date} : {narration}  {amount}")
        
              return         
        
                         