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
    print("The computer decided to remove",computer_decision,"stick")
    quantity = num_of_sticks-(player_decision+computer_decision)
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
        quantity = quantity- (player_decision+computer_decision)
        print("Now we have only",quantity,"sticks") 
        print("|" * quantity) 
#11;13;left 5 - computer wins 

    
    elif player_decision == 2:
        res = quantity-player_decision
        print("now we have only",res) 
        print("|" * res)
        #7 left
        print("Now the coputer is thinking....")
        computer_decision = 2
        print("The computer decided to remove",computer_decision,"sticks")
        quantity = quantity- (player_decision+computer_decision)
        print("Now we have only",quantity,"sticks") 
        print("|" * quantity)
#11;22;left 5 - computer wins
    
    elif player_decision == 3:
        res = quantity-player_decision
        print("Now we have only",res) 
        print("|" * res)
        print("Now the coputer is thinking....")
        computer_decision = 1
        print("The computer decided to remove",computer_decision,"sticks")
        quantity = quantity- (player_decision+computer_decision)
        print("Now we have only",quantity,"stick") 
        print("|" * quantity)      
#11;31;5 left  - computer wins    
    player_decision = int(input("\nHow many sticks do you want to remove ?" ))
    if player_decision == 1:
        print("Now we have only",5-player_decision)
        print("|" * (5-player_decision)) 
        print("Now the coputer is thinking....")
        computer_decision = 3
        print("The computer decided to remove",computer_decision,"sticks")
        print("\nC O M P U T E R    W O N !!!")
    
    elif player_decision == 2:
        print("Now we have only",5-player_decision)
        print("|" * (5-player_decision)) 
        print("Now the coputer is thinking....")
        computer_decision = 2
        print("The computer decided to remove",computer_decision,"sticks")
        print("\nC O M P U T E R    W O N !!!")
         
    elif player_decision == 3:
        print("Now we have only",5-player_decision)
        print("|" * (5-player_decision)) 
        print("Now the coputer is thinking....")
        computer_decision = 1
        print("The computer decided to remove",computer_decision,"stick")
        print("\nC O M P U T E R    W O N !!!")    
     
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   

#player 2 coputer 1
elif player_decision == 2:
    res = num_of_sticks-player_decision
    print("now we have only",res) 
    print("|" * res)
    print("Now the coputer is thinking....")
    computer_decision = 1
    print("The computer decided to remove",computer_decision,"stick")
    quantity = num_of_sticks-(player_decision+computer_decision)
    print("Now we have only",quantity,"sticks") 
    print("|" * quantity) 
    #8 left  @@@@@@@@@@@@@@@
    player_decision = int(input("\nHow many sticks do you want to remove ?" ))
    if player_decision == 1:
        print("Now we have only",quantity,"sticks")
        print("|" * (quantity)) 
        print("Now the coputer is thinking....")
        computer_decision = 2
        print("The computer decided to remove",computer_decision,"sticks")
        #5 left
        player_decision = int(input("\nHow many sticks do you want to remove ?" ))
        if player_decision == 1:
            print("Now we have only",5-player_decision)
            print("|" * (5-player_decision)) 
            print("Now the coputer is thinking....")
            computer_decision = 3
            print("The computer decided to remove",computer_decision,"sticks")
            print("\nC O M P U T E R    W O N !!!")
    #@@@@@@@@@@@@@@@@@@
        elif player_decision == 2:
            print("Now we have only",5-player_decision)
            print("|" * (5-player_decision)) 
            print("Now the coputer is thinking....")
            computer_decision = 2
            print("The computer decided to remove",computer_decision,"sticks")
            print("\nC O M P U T E R    W O N !!!")
         #@@@@@@@@@@@@@@@@@@
        elif player_decision == 3:
            print("Now we have only",5-player_decision)
            print("|" * (5-player_decision)) 
            print("Now the coputer is thinking....")
            computer_decision = 1
            print("The computer decided to remove",computer_decision,"stick")
            print("\nC O M P U T E R    W O N !!!")
            
#2;1 2;1    
    if player_decision == 2:
        print("Now we have only",quantity,"sticks")
        print("|" * (quantity)) 
        print("Now the coputer is thinking....")
        computer_decision = 1
        print("The computer decided to remove",computer_decision,"stick")
            #5 left
        player_decision = int(input("\nHow many sticks do you want to remove ?" ))
        if player_decision == 1:
            print("Now we have only",5-player_decision)
            print("|" * (5-player_decision)) 
            print("Now the coputer is thinking....")
            computer_decision = 3
            print("The computer decided to remove",computer_decision,"sticks")
            print("\nC O M P U T E R    W O N !!!")
    
        elif player_decision == 2:
            print("Now we have only",5-player_decision)
            print("|" * (5-player_decision)) 
            print("Now the coputer is thinking....")
            computer_decision = 2
            print("The computer decided to remove",computer_decision,"sticks")
            print("\nC O M P U T E R    W O N !!!")
         
        elif player_decision == 3:
            print("Now we have only",5-player_decision)
            print("|" * (5-player_decision)) 
            print("Now the coputer is thinking....")
            computer_decision = 1
            print("The computer decided to remove",computer_decision,"stick")
            print("\nC O M P U T E R    W O N !!!")
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#2;1 3;1             
    if player_decision == 3:
        print("Now we have only 5 sticks")
        print("|" * (5)) 
        print("Now the coputer is thinking....")
        if computer_decision == 1:
            print("The computer decided to remove",computer_decision,"stick")
            print("Now we have only 4 sticks")
            print("|" * (4)) 
            player_decision = int(input("\nHow many sticks do you want to remove ?" ))
            if player_decision == 3:
                print("You W O N")
                
        elif computer_decision == 2:
            print("The computer decided to remove",computer_decision,"sticks")
            print("Now we have only 3 sticks")
            print("|" * (3))  
            player_decision = int(input("\nHow many sticks do you want to remove ?" ))
            if player_decision == 2:
                print("You W O N")
        elif computer_decision == 3:
            print("The computer decided to remove",computer_decision,"sticks")
            print("Now we have only 2 sticks")
            print("|" * (2)) 
            player_decision = int(input("\nHow many sticks do you want to remove ?" ))
            if player_decision == 1:
                print("You W O N")
            
    
if player_decision == 3:
    print("Now we have only 8 sticks")
    print("|" * (8)) 
    print("Now the coputer is thinking....")
    computer_decision = 3
    print("The computer decided to remove",computer_decision,"sticks")
    print("Now we have only 5 sticks")
    print("|" * (5))
    player_decision = int(input("\nHow many sticks do you want to remove ?" ))
    if player_decision == 1:
        print("Now we have only",5-player_decision,"sticks")
        print("|" * (5-player_decision)) 
        print("Now the coputer is thinking....")
        computer_decision = 3
        print("The computer decided to remove",computer_decision,"sticks")
        print("\nC O M P U T E R    W O N !!!")
    
    elif player_decision == 2:
        print("Now we have only",5-player_decision,"sticks")
        print("|" * (5-player_decision)) 
        print("Now the coputer is thinking....")
        computer_decision = 2
        print("The computer decided to remove",computer_decision,"sticks")
        print("\nC O M P U T E R    W O N !!!")
         
    elif player_decision == 3:
        print("Now we have only",5-player_decision,"stick")
        print("|" * (5-player_decision)) 
        print("Now the coputer is thinking....")
        computer_decision = 1
        print("The computer decided to remove",computer_decision,"stick")
        print("\nC O M P U T E R    W O N !!!")
            
      
                


       

       