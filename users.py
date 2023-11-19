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
    id=""
    #init in cap 1 as well.
    def __init__(self, password, first_name, last_name, account_number, balance):
        self.name = first_name + " " + last_name
        self.password = password
        self.balance = balance
        #dashes replace address stuff that we dont rly need.

        response = create_customer(first_name, last_name, "101", "Packard", "Ann Arboer", "MI", "48306") 
        id = response['objectCreated']['_id']
        response = create_account(id, "Checking", "Checkings Account", 0, balance, account_number)
        print("User", self.name, "Created")
        

    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_password(self):
        return self.password
    def get_balance(self):
        return self.balance
    def get_bets(self):
        return self.bets
    def place_bet(self, amount, ou, payout, line):
        self.bets.append(wager.Wager(self.name, amount, ou, payout, line))
        self.balance -= amount
        create_withdrawal(self.id, "balance", "2023-11-18", "completed", amount, "Withdrawal")


    def resolve_bet(self, testname, result):
        bet = None
        for b in self.bets:
            if(b.get_testname() == testname):
                bet = b
        if(bet == None):
            return 0
        bet.resolve(result)
        if(bet.get_result() == "win"):
            self.balance += bet.get_payout()
            return bet.get_payout()
        return 0
    def deposit(self, amount):
        self.balance += amount
        create_deposit(self.id, "balance", "2023-11-18", "completed", amount, "Deposit")

    
    