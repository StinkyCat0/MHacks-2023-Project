from capitalOneUsers import delete_data
from users import User
accountnumber = "0000000000000000"


#account_number_next ++ everytime we create a new user
def generate_next_account_number(current_account_number):
    next_account_number = str(int(current_account_number) + 1).zfill(16)
    return next_account_number



#HOUSE: 
#Generate NAM Dealer, of account number 0000000000000001
user1 = User(123, "NAM", "Dealer", generate_next_account_number(accountnumber), 1000)

#USERS: 
#Generate Alice Smith, of account number 0000000000000001
user1 = User(123, "Alice", "Smith", generate_next_account_number(accountnumber), 1000)
#Generate Ben Patel, of account number 0000000000000002
user2 = User(321, "Ben", "Patel", generate_next_account_number(accountnumber), 1000)
#Generate Nessi Lee, of account number 0000000000000003
user3 = User(132, "Nessi", "Lee", generate_next_account_number(accountnumber), 1000)

#Getters
print(user1.get_name()) 
print(user1.get_password()) 
print(user1.get_balance()) 
print(user1.get_id())
#Place Bet
user1.place_bet(100, "over", 1.8, -125)
print(user1.get_balance()) 
print(user1.get_bets())
#Resolve Bet
user1.resolve_bet("over", 3)
#Get Balance
print(user1.get_balance()) 
print(user1.get_bets())
#Deposit Money
user1.deposit(500)
#Review Balance
print(user1.get_balance())
