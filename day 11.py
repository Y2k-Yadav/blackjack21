import random

def deal_card(cards):
    return random.choice(cards)

def cal_score(user,computer):
    user_sum=sum(user)
    computer_sum=sum(computer)
    if user_sum>=21 or user_sum<0:
        if 11 in user:
            user.remove(11)
            user.append(1)
            print(user)
        else:
            return 1
    if computer_sum>=21 or computer_sum<0:
        if 11 in user:
            computer.remove(11)
            computer.append(1)
            print(computer)
        else:
            return 2
    if "yes"==input("if you want to draw another card. Type 'yes' : "):
        user.append(deal_card(cards))
        computer.append(deal_card(cards))
        print(f"\nuser={user} sum of user Points={sum(user)}\n")
        return cal_score(user,computer)
    else:
        if user_sum==computer_sum:
            return 3
        elif user_sum>computer_sum:
            return 2
        else:
            return 1
        
            
    
        
cards=[11,1,2,3,4,5,6,7,8,9,10,10,10,10]
user=[]
computer=[]
user.append(deal_card(cards))
user.append(deal_card(cards))
computer.append(deal_card(cards))
computer.append(deal_card(cards))
print(f"\nuser={user} sum of user Points={sum(user)}")
print(f"computer={computer[0]}")
store=cal_score(user,computer)
if store==1:
    print("\ncomputer wins")
elif store==2:
    print("\nuser wins")
elif store==3:
    print("\ndraw")
    
print(f"\nuser={user} sum of user Points={sum(user)}")
print(f"\ncomputer={computer} sum of computer Points={sum(computer)}")




    
