def p_1(player_decision,line):          #שחקן מוחק מקל בודד
    print("\n"+"This is the new line of the sticks")
    for i in range (player_decision):
        line.pop()
    length = len(line)
    print(line)
    print(length)
    return line,length 

def p_2(player_decision,line):          #שחקן מוחק  2 מקלות 
    print("\n"+"This is the new line of the sticks")
    for i in range (player_decision):
        line.pop()
    print(line)
    return line 

def p_3(player_decision,line):          #שחקן מוחק  3 מקלות 
    print("\n"+"This is the new line of the sticks")
    for i in range (player_decision):
        line.pop()
    print(line)
    return line 

def c_1(computer_decision,line):#מחשב מוחק מקל בודד
    print("\n"+"This is the new line of the sticks")
    for i in range (computer_decision):
        line.pop()
    print(line)
    return line 

def mevi_oto_3(player_name,computer_name,line):
    if player_decision == 1:#3 long 
        p_1(player_decision,line)
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        c_1(computer_decision,line)   
        print(computer_name,"W O N !!!")       
    elif player_decision == 2:#1 long 
        p_1(player_decision,line)
        print(player_name,"W O N !!!") 

def mevi_oti_3(computer_decision,player_decision,player_name,computer_name,line):
    if computer_decision == 1:#3 long 
        c_1(computer_decision,line)
        player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
        p_1(player_decision,line)   
        print(player_name,"W O N !!!")       
    elif computer_decision == 2:#1 long 
        c_1(computer_decision,line)
        print(computer_name,"W O N !!!") 

def finish():
    turn = input("\nwho's turn ?")  
    if turn == "d":
        player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
        mevi_oto_3(player_decision,player_name,computer_name,line) 
    elif turn == "m":
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        mevi_oti_3(computer_decision,player_name,computer_name,line)



# def main():

player_name   = "d"
computer_name = "m"
line = [1,2,3,4]    

length = len(line)

if  length <= 3: 
    finish()
else:
    turn = input("\nwho's turn ?")  
    if turn == "d":
        player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
        if player_decision   == 1:                             
            p_1(player_decision,line)
            if  length <= 3:
                finish()
        #     else:
        #         pass
        # elif player_decision   == 2:                             
        #     p_2(player_decision,line)
        # elif player_decision   == 3:                             
        #     p_3(player_decision,line)
    
    # if __name__ == "__main__":
    #     main()
                 