import users
import wager

class House:
    users=[]
    balance = 0
    tests=[]
    testlines={}
    def __init__(self, tests):
        self.users = []
        self.balance = 0
        self.tests = tests
        for t in self.tests:
            line=85
            self.testlines.update({t:line})

    #getters
    def get_users(self):
        return self.users
    def get_balance(self):
        return self.balance
    def get_tests(self):   
        return self.tests
    def get_line(self, testname):
        return self.testlines[testname]

    #user adding funcions
    def add_user(self, name, password, balance, id):
        self.users.append(users.User(name, password, balance, id))
    def add_user(self, user):
        self.users.append(user)

    #user functions
    def resolve_test(self, testname, result):
        for u in self.users:
            self.balance-=u.resolve_bet(testname, result)
    def deposit(self, amount):
        self.balance += amount
    def update_line(self, testname):
        wagers=[]
        for u in self.users:
            for w in u.get_bets():
                if(w.get_testname() == testname):
                    wagers.append(w)
        over=0
        under=0
        for w in wagers:
            if(w.get_ou() == "over"):
                over += w.get_amount()
            else:
                under += w.get_amount()
        if(over > under):
            self.testlines[testname] += 1
        elif(under > over):
            self.testlines[testname] -= 1
    def place_bet(self, user, amount, ou, testname):
        line = self.testlines[testname]
        payout = amount*1.9
        user.place_bet(amount, ou, payout, line, testname)
        self.balance += amount  
    def updatebals(self):
        #written to update capone api later
        return
    
    

