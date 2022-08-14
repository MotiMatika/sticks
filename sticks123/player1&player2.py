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

player1_decision = int(input("\nPlayer1,how many sticks do you want to remove ?" ))
if player1_decision == 1:
    res1 = num_of_sticks-player1_decision
    print("Now we have only",res1) 
    print("|" * res1)
    player2_decision = int(input("\nPlayer2,how many sticks do you want to remove ?" ))
    if player2_decision == 1:
        res2 = res1-player2_decision
        print("Now we have only",res2) 
        print("|" * res2)
    elif player2_decision == 2:
        res2 = res1-player2_decision
        print("Now we have only",res2) 
        print("|" * res2)
    elif player2_decision == 3:
        res2 = res1-player2_decision
        print("Now we have only",res2) 
        print("|" * res2)
    
    
    
    
    
    
if player1_decision == 2:
    res1 = num_of_sticks-player1_decision
    print("Now we have only",res1) 
    print("|" * res1)
    player2_decision = int(input("\nPlayer2,how many sticks do you want to remove ?" ))
    if player2_decision == 1:
        res2 = res1-player2_decision
        print("Now we have only",res2) 
        print("|" * res2)
    elif player2_decision == 2:
        res2 = res1-player2_decision
        print("Now we have only",res2) 
        print("|" * res2)
    elif player2_decision == 3:
        res2 = res1-player2_decision
        print("Now we have only",res2) 
        print("|" * res2)    
    
    
    
    
    
    
    
    
    
    
    
    
# if player1_decision == 3:
#     res = num_of_sticks-player1_decision
#     print("now we have only",res) 
#     print("|" * res)    
    
    
    