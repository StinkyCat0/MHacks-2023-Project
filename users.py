"""user class
should have the following attributes:
    - name
    - password
    - balance
    - bets placed
"""
import wager

class User:
    name = ""
    password = ""
    balance = 0
    bets = []
    id=""
    def __init__(self, name, password, balance, id):
        self.name = name
        self.password = password
        self.balance = balance
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
    
    