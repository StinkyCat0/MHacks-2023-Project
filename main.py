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
user2 = User(123, "Alice", "Smith", generate_next_account_number(accountnumber), 1000)
#Generate Ben Patel, of account number 0000000000000002
user3 = User(321, "Ben", "Patel", generate_next_account_number(accountnumber), 1000)
#Generate Nessi Lee, of account number 0000000000000003
user4 = User(132, "Nessi", "Lee", generate_next_account_number(accountnumber), 1000)

#Getters
print("User1 Name:", user1.get_name(), "Password:", user1.get_password()) 
#Place Bet
print("User1 Placing Bet: 100$, over 85 for the Calc 2 Final Exam")
user1.place_bet(100, "over", 1.8, 85, "Calc 2 Final Exam")
print("User1 Balance", user1.get_balance()) 
# #Resolve Bet
print("Resolving Bet, with a final score of 84. Result:")
if(user1.resolve_bet("Calc 2 Final Exam", 84) == 0):
    print("Lose")
else:
    print("Win")
# #Get Balance
print("User1 Balance:", user1.get_balance()) 
# #Deposit Money
user1.deposit(500)
# #Review Balance
print("User1 Balance after deposit:", user1.get_balance())
