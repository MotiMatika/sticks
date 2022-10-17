def p_1(player_decision,line):          #שחקן מוחק מקל בודד
    print("\n"+"This is the new line of the sticks")
    for i in range (player_decision):
        line.pop()
    length = len(line)
    print(line)
    length = len(line)
    return line , length 

def p_2(player_decision,line):          #שחקן מוחק  2 מקלות 
    print("\n"+"This is the new line of the sticks")
    for i in range (player_decision):
        line.pop()
    print(line)
    length = len(line)
    return line , length

def p_3(player_decision,line):          #שחקן מוחק  3 מקלות 
    print("\n"+"This is the new line of the sticks")
    for i in range (player_decision):
        line.pop()
    print(line)
    length = len(line)
    return line , length

def c_1(computer_decision,line):#מחשב מוחק מקל בודד
    print("\n"+"This is the new line of the sticks")
    for i in range (computer_decision):
        line.pop()
    print(line)
    return line 

def c_2(computer_decision,line):#מחשב מוחק 2 מקלות
    print("\n"+"This is the new line of the sticks")
    for i in range (computer_decision):
        line.pop()
    print(line)
    return line 

def p_starts_from_3_to_1(player_name,computer_name,line):
    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
    if player_decision == 1:                #2 long 
        p_1(player_decision,line)
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        if computer_decision == 1:          #1 long
            c_1(computer_decision,line)   
            print(computer_name,"W O N !!!")       
    elif player_decision == 2:              #1 long 
        p_2(player_decision,line)
        print(player_name,"W O N !!!") 

def c_starts_from_3_to_1(player_name,computer_name,line):
    computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
    if computer_decision == 1:          #2 long 
        c_1(computer_decision,line)
        player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
        p_1(player_decision,line)   
        print(player_name,"W O N !!!")       
    elif computer_decision == 2:        #1 long 
        c_2(computer_decision,line)
        print(computer_name,"W O N !!!") 



player_name   = "d"
computer_name = "m"
line = [1,2,3,4,5,6]    

print("\n",line)
length = len(line)

if  length <= 3: 
    turn = input("\nwho's turn ?")  
    if turn == "d":
        p_starts_from_3_to_1(player_name,computer_name,line) 
    elif turn == "m":
        c_starts_from_3_to_1(player_name,computer_name,line)
else:
    turn = input("\nwho's turn ?")  
    if turn == "d":
        player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
        if player_decision == 3:                             
            line,length = p_3(player_decision,line)   
            if  length <= 3:
                c_starts_from_3_to_1(player_name,computer_name,line)
        elif player_decision == 2:                             
            line,length = p_2(player_decision,line)
            if  length <= 3:
                c_starts_from_3_to_1(player_name,computer_name,line)
        elif player_decision == 1:                             
            line,length = p_1(player_decision,line)
            if  length <= 3:
                c_starts_from_3_to_1(player_name,computer_name,line)
           

                 