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

def vc_5_2_1(computer_decision,player_decision,computer_name,line):
    p_3(player_decision,line)           #5-->2
    computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
    c_1(computer_decision,line)             #2-->1
    print(computer_name, "  W I N !!!") 

def vc_5_3_1(computer_decision,player_decision,computer_name,line):
    p_2(player_decision,line)           #5-->3
    computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
    c_2(computer_decision,line)         #3-->1
    print(computer_name, "  W I N !!!")

def vc_5_4_1(computer_decision,player_decision,computer_name,line):
        p_1(player_decision,line)           #5-->4
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        c_3(computer_decision,line)         #4-->1  
        print(computer_name, "  W I N !!!")

def vc_9_6_5(computer_decision,player_decision,computer_name,line):
        p_3(player_decision,line)           #9-->6
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        c_1(computer_decision,line)             #6-->5     

def vc_9_7_5(computer_decision,player_decision,computer_name,line):
    p_2(player_decision,line)           #9-->7
    computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
    c_2(computer_decision,line)         #7-->5 

def vc_9_8_5(computer_decision,player_decision,computer_name,line):
        p_1(player_decision,line)               #9-->8
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        c_3(computer_decision,line)             #8-->5 

def vc_13_12_9(computer_decision,player_decision,computer_name,line):
        p_1(player_decision,line)                   #13-->12
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        c_3(computer_decision,line)                 #12-->9  

def vc_13_11_9(computer_decision,player_decision,computer_name,player_name,line):
        p_2(player_decision,line)                   #13-->11
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        c_2(computer_decision,line)                 #11-->9                      
        # player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
             
def from_13_to_victory(computer_name,player_name,computer_decision,line):
    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
    if player_decision == 1:
        vc_13_12_9(computer_decision,player_decision,computer_name,line)                                              
        player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
        if player_decision == 1: 
            vc_9_8_5(computer_decision,player_decision,computer_name,line)                    
            player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
            if player_decision == 1:
                vc_5_4_1(computer_decision,player_decision,computer_name,line) 
            if player_decision == 2:
                vc_5_3_1(computer_decision,player_decision,computer_name,line) 
            if player_decision == 3:
                vc_5_2_1(computer_decision,player_decision,computer_name,line)    
        if player_decision == 2:
            vc_9_7_5(computer_decision,player_decision,computer_name,line)                     
            player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
            if player_decision == 1:
                vc_5_3_1(computer_decision,player_decision,computer_name,line)
            if player_decision == 2: 
                vc_5_3_1(computer_decision,player_decision,computer_name,line)
            if player_decision == 3:
                vc_5_2_1(computer_decision,player_decision,computer_name,line)          
        if player_decision == 3:
            vc_9_6_5(computer_decision,player_decision,computer_name,line)                     
            player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
            if player_decision == 1:
                vc_5_4_1(computer_decision,player_decision,computer_name,line)
            if player_decision == 2:
                vc_5_3_1(computer_decision,player_decision,computer_name,line) 
            if player_decision == 3: 
                vc_5_2_1(computer_decision,player_decision,computer_name,line)   
    if player_decision == 2:
        vc_13_11_9(computer_decision,player_decision,computer_name,player_name,line)                                        
        player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
        if player_decision == 1:
            vc_9_8_5(computer_decision,player_decision,computer_name,line)                     
            player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
            if player_decision == 1:
                vc_5_3_1(computer_decision,player_decision,computer_name,line)                 
            if player_decision == 2:
                vc_5_3_1(computer_decision,player_decision,computer_name,line) 
            if player_decision == 3:
                vc_5_2_1(computer_decision,player_decision,computer_name,line)    
        if player_decision == 2: 
            vc_9_7_5(computer_decision,player_decision,computer_name,line)                    
            player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
            if player_decision == 1:
                vc_5_3_1(computer_decision,player_decision,computer_name,line)

            if player_decision == 2: 
                vc_5_3_1(computer_decision,player_decision,computer_name,line)
            if player_decision == 3:
                vc_5_2_1(computer_decision,player_decision,computer_name,line)          
    if player_decision == 3:###################################להמשיך מכאן
        p_3(player_decision,line)                               
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        c_1(computer_decision,line)#10-->9
        player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
        if player_decision == 1:
            cv_9_8_5(computer_decision,player_decision,computer_name,line)
            player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
            if player_decision == 1:
                cv_5_4_1(computer_decision,player_decision,computer_name,line)
                player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
                if player_decision == 2:
                    cv_9_7_5(computer_decision,player_decision,computer_name,line)
                    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
                if player_decision == 3:
                    cv_9_6_5(computer_decision,player_decision,computer_name,line)
                    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
        
    if player_decision == 1:
    if player_decision == 2:
                
        if player_decision == 3:
#######################################################################
def main():

    player_name   = "Dror"
    computer_name = "Moti"
    line = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]    
    
    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
    if   player_decision == 1:              #15-->14 
        p_1(player_decision,line)
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        c_1(computer_decision,line)   #14-->13
        from_13_to_victory(computer_name,player_name,computer_decision,line)       
                
if __name__ == "__main__":
        main() 
    
