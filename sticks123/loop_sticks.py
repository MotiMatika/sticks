# import random as rd
def p_1(player_decision,line):      #שחקן מוחק מקל בודד
    print("\n"+"This is the new line of the sticks")
    for i in range (player_decision):
        line.pop()
    print(line)
    return line 

def p_2(player_decision,line):      #שחקן מוחק 2 מקלות
    print("\n"+"This is the new line of the sticks")
    for i in range (player_decision):
        line.pop()
    print(line)
    return line

def p_3(player_decision,line):      #שחקן מוחק 3 מקלות
    print("\n"+"This is the new line of the sticks")
    for i in range (player_decision):
        line.pop()
    print(line)
    return line  

def c_1(computer_decision,line):    #מחשב מוחק מקל בודד
    print("\n"+"This is the new line of the sticks")
    for i in range (computer_decision):
        line.pop()
    print(line)
    return line 

def c_2(computer_decision,line):    #מחשב מוחק 2 מקלות
    print("\n"+"This is the new line of the sticks")
    for i in range (computer_decision):
        line.pop()
    print(line)
    return line 

def c_3(computer_decision,line):    #מחשב מוחק 3 מקלות
    print("\n"+"This is the new line of the sticks")
    for i in range (computer_decision):
        line.pop()
    print(line)
    return line 


def check_long_player(player_decision,line):
    
    if player_decision     == 1:             
        p_1(player_decision,line)
    elif player_decision   == 2:             
        p_2(player_decision,line)    
    elif player_decision   == 3:             
        p_3(player_decision,line)    

def check_long_computer(computer_decision,line):    
    if computer_decision     == 1:             
        c_1(computer_decision,line)
    elif computer_decision   == 2:             
        c_2(computer_decision,line)    
    elif computer_decision   == 3:             
        c_3(computer_decision,line)            
                
                

def main():

    player_name   = "d"
    computer_name = "m"
    line = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]    


    turn = input("who's turn ? ")
    if turn == player_name:
        player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
        if player_decision <= 3 :
            check_long_player(player_decision,line)
    elif turn == computer_name:
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        if computer_decision <= 3 :
            check_long_computer(computer_decision,line)
 
 
 
    
if __name__ == "__main__":
        main()
                 