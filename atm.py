class Atm(object):
    def __init__(self,card_number,pin_number):
        self.card_number=card_number
        self.pin_number=pin_number
       

    def CashWithdrawl(self):
        print("Cash With drawl")

    def BalanceEnquiry(self):
        print("Balance Enquiry")

    
        
atm = Atm("8735 6353 5363","9738")
print(atm.card_number)
print(atm.CashWithdrawl())
