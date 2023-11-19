"""user class
should have the following attributes:
    - name
    - password
    - balance
    - bets placed
"""
import wager
import json
from capitalOneUsers import create_customer, create_account, create_withdrawal,create_deposit,fetch_accounts
class User:
    name = ""
    password = ""
    balance = 0
    bets = []
    acc_id=""
    cus_id=""
    #init in cap 1 as well.
    def __init__(self, password, first_name, last_name, account_number, balance):
        self.name = first_name + " " + last_name
        self.password = password
        self.balance = balance

        response = create_customer(first_name, last_name, "101", "Packard", "Ann Arbor", "MI", "48306") 
        self.acc_id = response['objectCreated']['_id']

        response = create_account(self.acc_id, "Checking", "Checkings Account", 0, balance, account_number)
        self.cus_id = response['objectCreated']['customer_id']
        

        print("User", self.name, "Created")
        

    def get_id(self):
        return self.cus_id
    def get_name(self):
        return self.name
    def get_password(self):
        return self.password
    def get_balance(self):
        return self.balance
    def get_bets(self):
        return self.bets
        
    def place_bet(self, amount, ou, payout, line, testname):
        self.bets.append(wager.Wager(self.name, amount, ou, payout, line, testname))
        self.balance -= amount
        create_withdrawal(self.cus_id, "balance", "2023-11-18", "completed", amount, "Withdrawal")


    def resolve_bet(self, testname, result):
        bet = None
        for b in self.bets:
            if(b.get_testname() == testname):
                print(testname)
                bet = b
        if(bet == None):
            return 0
        print(bet.resolve(result))
        if(bet.get_result() == "win"):
            self.balance += bet.get_payout()
            return bet.get_payout()
        return 0
    def deposit(self, amount):
        self.balance += amount
        create_deposit(self.cus_id, "balance", "2023-11-18", "completed", amount, "Deposit")

    
    