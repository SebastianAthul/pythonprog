acc_bal = 10000
amount=int(input("enter the amount to withdraw :"))
if amount>10000:
    print("insufficient Balance")
elif amount==0:
    print("invalid Entry")
else:
    bal=acc_bal-amount
    print("Balance amount in account=", bal)
    print("Thank you for banking with us")

