def p_1(player_decision,line):
    print("\n"+"This is the new line of the sticks")
    for i in range (player_decision):
        line.pop()
    print(line)
    return line 

def p_2(player_decision,line):
    print("\n"+"This is the new line of the sticks")
    for i in range (player_decision):
        line.pop()
    print(line)
    return line

def p_3(player_decision,line):
    print("\n"+"This is the new line of the sticks")
    for i in range (player_decision):
        line.pop()
    print(line)
    return line  

def c_1(computer_decision,line):
    print("\n"+"This is the new line of the sticks")
    for i in range (computer_decision):
        line.pop()
    print(line)
    return line 

def c_2(computer_decision,line):
    print("\n"+"This is the new line of the sticks")
    for i in range (computer_decision):
        line.pop()
    print(line)
    return line 

def c_3(computer_decision,line):
    print("\n"+"This is the new line of the sticks")
    for i in range (computer_decision):
        line.pop()
    print(line)
    return line 

def big_1(computer_name,player_name,computer_decision,line,):
            c_1(computer_decision,line)                         #12 long
            player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
            p_3(player_decision,line)                           #9 long   
            computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
            if computer_decision == 1:                          #8 long
                c_1(computer_decision,line)
                player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
                p_3(player_decision,line)                       #5 long  
                computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
                if computer_decision == 1:                      #4 long
                    c_1(computer_decision,line)
                    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
                    p_3(player_decision,line)                   #1 long  
                    print(player_name, "  W I N !!!")
                elif computer_decision == 2:
                    c_2(computer_decision,line)                 #11 long
                    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
                    p_2(player_decision,line)                   #9 long
                    print(player_name, "  W I N !!!")
                elif computer_decision == 3:
                    c_2(computer_decision,line)
                    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
                    p_1(player_decision,line)
                    print(player_name, "  W I N !!!")
            if computer_decision == 2:                          #8 long
                c_2(computer_decision,line)
                player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
                p_2(player_decision,line)                       #5 long  
                computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
                if computer_decision == 1:                      #4 long
                    c_1(computer_decision,line)
                    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
                    p_3(player_decision,line)                   #1 long  
                    print(player_name, "  W I N !!!")
                elif computer_decision == 2:
                    c_2(computer_decision,line)
                    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
                    p_2(player_decision,line)
                    print(player_name, "  W I N !!!")
                elif computer_decision == 3:
                    c_2(computer_decision,line)
                    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
                    p_1(player_decision,line)
                    print(player_name, "  W I N !!!")
            if computer_decision == 3:                          #8 long
                c_3(computer_decision,line)
                player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
                p_1(player_decision,line)                       #5 long  
                computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
                if computer_decision == 1:                      #4 long
                    c_1(computer_decision,line)
                    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
                    p_3(player_decision,line)                   #1 long  
                    print(player_name, "  W I N !!!")
                elif computer_decision == 2:
                    c_2(computer_decision,line)
                    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
                    p_2(player_decision,line)
                    print(player_name, "  W I N !!!")
                elif computer_decision == 3:
                    c_2(computer_decision,line)
                    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
                    p_1(player_decision,line)
                    print(player_name, "  W I N !!!")
#######################################################################
def main():

    player_name   = "Dror"
    computer_name = "Moti"
    line = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]    
    
    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
    if   player_decision == 1:
        p_1(player_decision,line)
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        c_1(computer_decision,line)   
    elif player_decision == 2:
        p_2(player_decision,line)                               #13 long
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        if computer_decision == 1:
            big_1(computer_name,player_name,computer_decision,line)
        if computer_decision == 2:
            big_1(computer_name,player_name,computer_decision,line)
        if computer_decision == 3:
            big_1(computer_name,player_name,computer_decision,line)     
    elif player_decision == 3:
        p_3(player_decision,line)#12 long
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        c_3(computer_decision,line)#9 long
        player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
        if player_decision == 1:#8 long
            p_1(player_decision,line)
            computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
            c_3(computer_decision,line)#5 long
            player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
            if player_decision == 1:#4 long
                p_1(player_decision,line)
                computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
                c_3(computer_decision,line)#1 long
                print(computer_name,"  W  I  N !!!")
            elif player_decision == 2:#2 long
                p_2(player_decision,line)
                computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
                c_2(computer_decision,line)#1 long
                print(computer_name,"  W  I  N !!!")
            elif player_decision == 3:#1 long
                p_1(player_decision,line)
                computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
                c_1(computer_decision,line)#1 long
                print(computer_name,"  W  I  N !!!")
        if player_decision == 2:#7 long
            p_2(player_decision,line)
            computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
            c_2(computer_decision,line)#5 long
            player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
            if player_decision == 1:#4 long
                p_1(player_decision,line)
                computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
                c_3(computer_decision,line)#1 long
                print(computer_name,"  W  I  N !!!")
            elif player_decision == 2:#2 long
                p_2(player_decision,line)
                computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
                c_2(computer_decision,line)#1 long
                print(computer_name,"  W  I  N !!!")
            elif player_decision == 3:#1 long
                p_1(player_decision,line)
                computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
                c_1(computer_decision,line)#1 long
                print(computer_name,"  W  I  N !!!")
        if player_decision == 3:#6 long
            p_3(player_decision,line)
            computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
            c_1(computer_decision,line)#5 long
            player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
            if player_decision == 1:#4 long
                p_1(player_decision,line)
                computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
                c_3(computer_decision,line)#1 long
                print(computer_name,"  W  I  N !!!")
            elif player_decision == 2:#2 long
                p_2(player_decision,line)
                computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
                c_2(computer_decision,line)#1 long
                print(computer_name,"  W  I  N !!!")
            elif player_decision == 3:#1 long
                p_1(player_decision,line)
                computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
                c_1(computer_decision,line)#1 long
                print(computer_name,"  W  I  N !!!")        
               
                
                
                
if __name__ == "__main__":
        main() 
    
