print("\nS T I C K S")

print("\n|  |  |  |  |  |  |  |  |  |  |")

print("""\nYou have to remove,
      one,
      or two
      or three sticks.
      The player who takes the last stick - LOSE""")

player_name = "Tomer"
num_of_sticks = 11
print("\nHere we have",num_of_sticks,"sticks")
print("\n")
line = [1,2,3,4,5,6,7,8,9,10,11]

#111
player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ?" ))
if player_decision == 1:
    num_of_sticks = num_of_sticks-player_decision
    del line[0]
    print("Now we have only",num_of_sticks,"sticks")
    print(line)     
    print("Now the coputer is thinking....")
    computer_decision = 1
    num_of_sticks = num_of_sticks-computer_decision
    print("The computer decided to remove",computer_decision,"stick")
    print("Now we have only",num_of_sticks ,"sticks") 
    del line[0]
    print(line)
    
    #A
    player_decision = int(input("\nPlayer,how many sticks do you want to remove ?" ))
    if player_decision == 1:
        num_of_sticks = num_of_sticks-player_decision
        del line[0]
        print("Now we have only",num_of_sticks,"sticks")
        print(line)
        print("Now the coputer is thinking....")
        computer_decision = 3
        num_of_sticks = num_of_sticks-computer_decision
        print("The computer decided to remove",computer_decision,"sticks")
        print("Now we have only",num_of_sticks ,"sticks") 
        del line[0:3]
        print(line)
    #B
    elif player_decision == 2:
        num_of_sticks = num_of_sticks-player_decision
        del line[0:2]
        print("Now we have only",num_of_sticks,"sticks")
        print(line)
        print("Now the coputer is thinking....")
        computer_decision = 2
        num_of_sticks = num_of_sticks-computer_decision
        print("The computer decided to remove",computer_decision,"sticks")
        print("Now we have only",num_of_sticks ,"sticks") 
        del line[0:2]
        print(line)
    #C
    elif player_decision == 3:
        num_of_sticks = num_of_sticks-player_decision
        del line[0:3]
        print("Now we have only",num_of_sticks,"sticks")
        print(line)
        print("Now the coputer is thinking....")
        computer_decision = 1
        num_of_sticks = num_of_sticks-computer_decision
        print("The computer decided to remove",computer_decision,"stick")
        print("Now we have only",num_of_sticks ,"sticks") 
        del line[0]
        print(line)
    player_decision = int(input("\nHow many sticks do you want to remove ?" ))
    #D
    if player_decision == 1:
        num_of_sticks = 5-player_decision
        del line[0]
        print("Now we have only",num_of_sticks,"sticks")
        print(line)     
        print("Now the coputer is thinking....")
        computer_decision = 3
        num_of_sticks = num_of_sticks-computer_decision
        print("The computer decided to remove",computer_decision,"sticks")
        print("Now we have only",num_of_sticks ,"stick") 
        del line[0:3]
        print(line)
        print("COMPUTER WON !!! ")
    #E
    
    elif player_decision == 2:
        num_of_sticks = 5-player_decision
        del line[0:2]
        print("Now we have only",num_of_sticks,"sticks")
        print(line)     
        print("Now the coputer is thinking....")
        computer_decision = 2
        num_of_sticks = num_of_sticks-computer_decision
        print("The computer decided to remove",computer_decision,"sticks")
        print("Now we have only",num_of_sticks ,"stick") 
        del line[0:2]
        print(line)
        print("COMPUTER WON !!! ")
    #F
    elif player_decision == 3:
        num_of_sticks = 5-player_decision
        del line[0:3]
        print("Now we have only",num_of_sticks,"sticks")
        print(line)     
        print("Now the coputer is thinking....")
        computer_decision = 1
        num_of_sticks = num_of_sticks-computer_decision
        print("The computer decided to remove",computer_decision,"sticks")
        print("Now we have only",num_of_sticks ,"stick") 
        del line[0:1]
        print(line)
        print("COMPUTER WON !!! ")
        
#222
elif player_decision == 2:
    num_of_sticks = num_of_sticks-player_decision
    del line[0:2]
    print("Now we have only",num_of_sticks,"sticks")
    print(line)     
    print("Now the coputer is thinking....")
    computer_decision = 1
    num_of_sticks = num_of_sticks-computer_decision
    print("The computer decided to remove",computer_decision,"stick")
    print("Now we have only",num_of_sticks ,"sticks") 
    del line[0]
    print(line)
    
    #G 
    player_decision = int(input("\nPlayer,how many sticks do you want to remove ?" ))
    if player_decision == 1:
        num_of_sticks = num_of_sticks-player_decision
        del line[0]
        print("Now we have only",num_of_sticks,"sticks")
        print(line)
        print("Now the coputer is thinking....")
        computer_decision = 2 
        num_of_sticks = num_of_sticks-computer_decision
        print("The computer decided to remove",computer_decision,"sticks")
        print("Now we have only",num_of_sticks ,"sticks") 
        del line[0:2]
        print(line)
        player_decision = int(input("\nPlayer,how many sticks do you want to remove ?" ))

        if player_decision == 1:
            num_of_sticks = 5-player_decision
            del line[0]
            print("Now we have only",num_of_sticks,"sticks")
            print(line)    
            print("Now the coputer is thinking....")
            computer_decision = 3
            print("The computer decided to remove",computer_decision,"sticks")
            print("Now we have only",num_of_sticks ,"stick") 
            del line[0:3]
            print(line) 
            print("COMPUTER WON !!! ")
        elif player_decision == 2:
            num_of_sticks = 5-player_decision
            del line[0:2]
            print("Now we have only",num_of_sticks,"sticks")
            print(line)
            print("Now the coputer is thinking....")
            computer_decision = 2
            num_of_sticks = num_of_sticks - computer_decision
            print("The computer decided to remove",computer_decision,"sticks")
            print("Now we have only",num_of_sticks ,"stick") 
            del line[0:2]
            print(line) 
            print("COMPUTER WON !!! ")
        elif player_decision == 3:
            num_of_sticks = 5-player_decision
            del line[0:3]
            print("Now we have only",num_of_sticks,"stick")
            print(line)
            print("Now the coputer is thinking....")
            computer_decision = 1
            num_of_sticks = num_of_sticks - computer_decision
            print("The computer decided to remove",computer_decision,"stick")
            print("Now we have only",num_of_sticks ,"stick") 
            del line[0]
            print(line) 
            print("COMPUTER WON !!! ")
    #H 
        player_decision = int(input("\nPlayer,how many sticks do you want to remove ?" ))
    elif player_decision == 2:
        num_of_sticks = num_of_sticks-player_decision
        del line[0:2]
        print("Now we have only",num_of_sticks,"sticks")
        print(line)
        print("Now the coputer is thinking....")
        computer_decision = int(input("\nComputer,how many sticks do you want to remove ?" ))
        computer_decision = 1 
        num_of_sticks = num_of_sticks-computer_decision
        print("The computer decided to remove",computer_decision,"stick")
        print("Now we have only",num_of_sticks ,"sticks") 
        del line[0]
        print(line)
        player_decision = int(input("\nPlayer,how many sticks do you want to remove ?" ))
        if player_decision == 1:
            num_of_sticks = 5-player_decision
            del line[0]
            print("Now we have only",num_of_sticks,"sticks")
            print(line)    
            print("Now the coputer is thinking....")
            computer_decision = 3
            print("The computer decided to remove",computer_decision,"sticks")
            print("Now we have only",num_of_sticks ,"stick") 
            del line[0:3]
            print(line) 
            print("COMPUTER WON !!! ")
        elif player_decision == 2:
            num_of_sticks = 5-player_decision
            del line[0:2]
            print("Now we have only",num_of_sticks,"sticks")
            print(line)
            print("Now the coputer is thinking....")
            computer_decision = 2
            num_of_sticks = num_of_sticks - computer_decision
            print("The computer decided to remove",computer_decision,"sticks")
            print("Now we have only",num_of_sticks ,"stick") 
            del line[0:2]
            print(line) 
            print("COMPUTER WON !!! ")
        elif player_decision == 3:
            num_of_sticks = 5-player_decision
            del line[0:3]
            print("Now we have only",num_of_sticks,"stick")
            print(line)
            print("Now the coputer is thinking....")
            computer_decision = 1
            num_of_sticks = num_of_sticks - computer_decision
            print("The computer decided to remove",computer_decision,"stick")
            print("Now we have only",num_of_sticks ,"stick") 
            del line[0]
            print(line) 
            print("COMPUTER WON !!! ")
       
        
    #I   
        player_decision = int(input("\nPlayer,how many sticks do you want to remove ?" ))
    elif player_decision == 3:
        num_of_sticks = 5
        del line[0:3]
        print("Now we have only",num_of_sticks,"sticks")
        print(line)
        print("Now the coputer is thinking....")
        #J
        computer_decision = int(input("\nComputer,how many sticks do you want to remove ?" ))
        if computer_decision == 1: 
            num_of_sticks = 4
            print("The computer decided to remove",computer_decision,"stick")
            print("Now we have only",num_of_sticks ,"sticks") 
            del line[0]
            print(line)
            player_decision = int(input("\nPlayer,how many sticks do you want to remove ?" ))
            if player_decision == 1:
                num_of_sticks = 4-player_decision
                del line[0]
                print("Now we have only",num_of_sticks,"sticks")
                print(line)     
                print("Now the coputer is thinking....")
                computer_decision = 2
                num_of_sticks = num_of_sticks-computer_decision
                print("The computer decided to remove",computer_decision,"sticks")
                print("Now we have only",num_of_sticks ,"stick") 
                del line[0:2]
                print(line)
                print("COMPUTER WON !!! ")
            
            elif player_decision == 2:
                num_of_sticks = 4-player_decision
                del line[0:2]
                print("Now we have only",num_of_sticks,"sticks")
                print(line)     
                print("Now the coputer is thinking....")
                computer_decision = 1
                num_of_sticks = num_of_sticks-computer_decision
                print("The computer decided to remove",computer_decision,"stick")
                print("Now we have only",num_of_sticks ,"stick") 
                del line[0]
                print(line)
                print("COMPUTER WON !!! ")
            
            elif player_decision == 3:
                num_of_sticks = 4-player_decision
                del line[0:3]
                print("Now we have only",num_of_sticks,"stick")
                print(line)     
                print("YOU WON !!! ")
        #K
        elif computer_decision == 2: 
            num_of_sticks = 3
            print("The computer decided to remove",computer_decision,"sticks")
            print("Now we have only",num_of_sticks ,"stick") 
            del line[0:2]
            print(line)
            player_decision = int(input("\nPlayer,how many sticks do you want to remove ?" ))
            if player_decision == 1:
                del line[0]
                print("Now we have only 2 sticks")
                print(line)
                print("Now the coputer is thinking....")
                computer_decision = int(input("\nComputer,how many sticks do you want to remove ?" ))
                computer_decision = 1
                del line[0]
                print("COMPUTER WON !!! ")
            elif player_decision == 2:
                print("YOU WON !!! ")
        # #L
        elif computer_decision == 3: 
            num_of_sticks = 4-computer_decision
            print("The computer decided to remove",computer_decision,"sticks")
            print("Now we have only",num_of_sticks ,"stick") 
            del line[0:3]
            print(line)
            player_decision = int(input("\nPlayer,how many sticks do you want to remove ?" ))
            if player_decision == 1:
                print("YOU WON !!! ")  

#333
elif  player_decision == 3:
    num_of_sticks = num_of_sticks-player_decision
    del line[0:3]
    print("Now we have only",num_of_sticks,"sticks")
    print(line)     
    print("Now the coputer is thinking....")
    computer_decision = 3
    num_of_sticks = num_of_sticks-computer_decision
    print("The computer decided to remove",computer_decision,"sticks")
    print("Now we have only",num_of_sticks ,"sticks") 
    del line[0:3]
    print(line) 
    player_decision = int(input("\nPlayer,how many sticks do you want to remove ?" ))

    if player_decision == 1:
        num_of_sticks = 5-player_decision
        del line[0]
        print("Now we have only",num_of_sticks,"sticks")
        print(line)    
        print("Now the coputer is thinking....")
        computer_decision = 3
        print("The computer decided to remove",computer_decision,"sticks")
        print("Now we have only",num_of_sticks ,"stick") 
        del line[0:3]
        print(line) 
        print("COMPUTER WON !!! ")
    elif player_decision == 2:
        num_of_sticks = 5-player_decision
        del line[0:2]
        print("Now we have only",num_of_sticks,"sticks")
        print(line)
        print("Now the coputer is thinking....")
        computer_decision = 2
        num_of_sticks = num_of_sticks - computer_decision
        print("The computer decided to remove",computer_decision,"sticks")
        print("Now we have only",num_of_sticks ,"stick") 
        del line[0:2]
        print(line) 
        print("COMPUTER WON !!! ")
    elif player_decision == 3:
        num_of_sticks = 5-player_decision
        del line[0:3]
        print("Now we have only",num_of_sticks,"stick")
        print(line)
        print("Now the coputer is thinking....")
        computer_decision = 1
        num_of_sticks = num_of_sticks - computer_decision
        print("The computer decided to remove",computer_decision,"stick")
        print("Now we have only",num_of_sticks ,"stick") 
        del line[0]
        print(line) 
        print("COMPUTER WON !!! ")
