class Bank:
    bankname='sbi'
    def acc_create(self,name,acc_no):
        self.name=name
        self.acc_no=acc_no
        self.min_bal=5000
        self.bal=self.min_bal
    def deposit(self,amount):
        self.amount=amount
        self.bal +=self.amount
        print("your",Bank.bankname,"has been created with bal",self.amount,)
        print("current balance is",self.bal)
    def withdraw(self,amt):
        self.amt=amt
        if self.amt>self.bal:
            print("insufficient balance")
        else:
            print("debited with ",self.amt)
            self.bal-=self.amt
            print("available bal=",self.bal)
obj=Bank()
obj.acc_create("Athul",123456)
obj.deposit(20000)
obj.withdraw(2000)
