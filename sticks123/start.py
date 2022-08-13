print("\nS T I C K S")

print("\n| | | | | | | | | | |")
print("""\nYou have to remove,
      one,
      or two
      or three sticks.
      The player who takes the last stick - LOSE""")
num_of_sticks = 11
print("\nHere we have",num_of_sticks,"sticks")
print("\n")
print("|" * (num_of_sticks))

#player 1 coputer 1
player_decision = int(input("\nHow many sticks do you want to remove ?" ))
if player_decision == 1:
    res = num_of_sticks-player_decision
    print("now we have only",res) 
    print("|" * res)
    print("Now the coputer is thinking....")
    computer_decision = player_decision
    print("The computer decided to remove",computer_decision,"sticks")
    quantity = num_of_sticks-2
    print("Now we have only",quantity,"sticks") 
    print("|" * quantity)
#left 9    
player_decision = int(input("\nHow many sticks do you want to remove ?" ))
if player_decision == 1:
    res = quantity-player_decision
    print("now we have only",res) 
    print("|" * res)
    print("Now the coputer is thinking....")
    computer_decision = 3
    print("The computer decided to remove",computer_decision,"sticks")
    quantity = quantity-4
    print("Now we have only",quantity,"sticks") 
    print("|" * quantity) 
#left 5 - computer wins 
player_decision = int(input("\nHow many sticks do you want to remove ?" ))
    
elif:
    player_decision == 2
    res = quantity-player_decision
        print("now we have only",res) 
        print("|" * res)
        print("Now the coputer is thinking....")
        computer_decision = 2
        print("The computer decided to remove",computer_decision,"sticks")
        quantity = quantity-6
        print("Now we have only",quantity,"sticks") 
        print("|" * quantity)
    
if player_decision == 3:
    res = quantity-player_decision
    print("now we have only",res) 
    print("|" * res)
    print("Now the coputer is thinking....")
    computer_decision = 1
    print("The computer decided to remove",computer_decision,"sticks")
    quantity = quantity-6
    print("Now we have only",quantity,"sticks") 
    print("|" * quantity)      
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
      

# player_decision = int(input("\nHow many sticks do you want to remove ?" ))
# if player_decision == 1:
#     res = quantity-player_decision
#     print("now we have only",res) 
#     print("|" * res)
#     print("Now the coputer is thinking....")
#     computer_decision = 3-player_decision
#     print("The computer decided to remove",computer_decision,"sticks")
#     quantity = res-(3-player_decision)
#     print("Now we have only",quantity,"sticks") 
#     print("|" * quantity)      
    
# player_decision = int(input("\nHow many sticks do you want to remove ?" ))
# if player_decision == 1:
#     res = quantity-player_decision
#     print("now we have only",res) 
#     print("|" * res)
#     print("Now the coputer is thinking....")
#     computer_decision = 3-player_decision
#     print("The computer decided to remove",computer_decision,"sticks")
#     quantity = res-(3-player_decision)
#     print("Now we have only",quantity,"sticks") 
#     print("|" * quantity)    
    
    
# if player_decision == 2: 
#     pres = num_of_sticks-player_decision 
#     print("|" * res)
#     print("Now the coputer is thinking....")
# if player_decision == 3: 
#     pres = num_of_sticks-player_decision 
#     print("|" * res)
#     print("Now the coputer is thinking....") 

       

       