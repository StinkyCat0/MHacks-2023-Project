"""wager class
should have the following attributes:
    - User name
    - amount
    - odds
    - result
    - payout"""

class Wager:
    user = ""
    amount = 0
    over_under = ""
    payout = 0
    result = ""
    line = 0
    testname = ""
    def __init__(self, user, amount, ou, payout, line, testname):
        self.user = user
        self.amount = amount
        self.over_under = ou
        self.payout = payout
        self.line = line
        self.testname = testname
    def get_user(self):
        return self.user
    def get_line(self):
        return self.line
    def get_testname(self):
        return self.testname
    def get_amount(self):
        return self.amount
    def get_ou(self):
        return self.over_under 
    def get_payout(self):
        return self.payout
    def get_result(self):
        return self.result
    def resolve(self, result):
        if(result == self.over_under):
            self.result = "win"
        else:
            self.result = "lose"
        return self.result
