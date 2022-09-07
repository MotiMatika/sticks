import random as rd
def p_1(player_decision,line):#שחקן מוחק מקל בודד
    print("\n"+"This is the new line of the sticks")
    for i in range (player_decision):
        line.pop()
    print(line)
    return line 

def p_2(player_decision,line):#שחקן מוחק 2 מקלות
    print("\n"+"This is the new line of the sticks")
    for i in range (player_decision):
        line.pop()
    print(line)
    return line

def p_3(player_decision,line):#שחקן מוחק 3 מקלות
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

def c_2(computer_decision,line):#מחשב מוחק 2 מקלות
    print("\n"+"This is the new line of the sticks")
    for i in range (computer_decision):
        line.pop()
    print(line)
    return line 

def c_3(computer_decision,line):#מחשב מוחק 3 מקלות
    print("\n"+"This is the new line of the sticks")
    for i in range (computer_decision):
        line.pop()
    print(line)
    return line 

def vc_5_2_1(player_decision,computer_name,line):#מחשב מנצח כששחקן לוקח 3 מקלות החל 5 
    p_3(player_decision,line)           #5-->2
    computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
    c_1(computer_decision,line)             #2-->1
    print(computer_name, "  W I N !!!") 

def vc_5_3_1(player_decision,computer_name,line):#מחשב מנצח כששחקן לוקח 2 מקלות החל 5
    p_2(player_decision,line)           #5-->3
    computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
    c_2(computer_decision,line)         #3-->1
    print(computer_name, "  W I N !!!")

def vc_5_4_1(player_decision,computer_name,line):#מחשב מנצח כששחקן לוקח מקל החל 5
        p_1(player_decision,line)           #5-->4
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        c_3(computer_decision,line)         #4-->1  
        print(computer_name, "  W I N !!!")

def vc_9_6_5(player_decision,computer_name,line):#מחשב מנצח כששחקן לוקח 2 מקלות החל 9
        p_3(player_decision,line)           #9-->6
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        c_1(computer_decision,line)             #6-->5     

def vc_9_7_5(player_decision,computer_name,line):#מחשב מנצח כששחקן לוקח 2 מקלות החל 9 
    p_2(player_decision,line)           #9-->7
    computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
    c_2(computer_decision,line)         #7-->5 

def vc_9_8_5(player_decision,computer_name,line):#מחשב מנצח כששחקן לוקח מקל החל 9 
        p_1(player_decision,line)               #9-->8
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        c_3(computer_decision,line)             #8-->5 

def vc_13_12_9(player_decision,computer_name,line):#מחשב מנצח כששחקן לוקח מקל החל 13 
        p_1(player_decision,line)                   #13-->12
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        c_3(computer_decision,line)                 #12-->9  

def vc_13_11_9(player_decision,computer_name,line):#מחשב מנצח כששחקן לוקח 2 מקלות החל 13 
        p_2(player_decision,line)                   #13-->11
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        c_2(computer_decision,line)                 #11-->9                      

def vc_13_10_9(player_decision,computer_name,line):#מחשב מנצח כששחקן לוקח 3 מקלות החל 13 
    p_3(player_decision,line)           #13--<10                              
    computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
    c_1(computer_decision,line)         #10-->9 

def vc_15_14_13(player_decision,computer_name,line):#מחשב מנצח כששחקן לוקח מקל החל 15 
    p_1(player_decision,line)
    computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
    c_1(computer_decision,line)         #14-->13 
    return line 

def vc_15_12_9(player_decision,computer_name,line):#מחשב מנצח כששחקן לוקח 3 מקלות החל 15
    p_3(player_decision,line)
    computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
    c_1(computer_decision,line)         #10-->9 
    return line 
     
def from_13_to_victory(computer_name,player_name,line):
    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
    if player_decision == 1:
        vc_13_12_9(player_decision,computer_name,line)                                              
        player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
        if player_decision == 1: 
            vc_9_8_5(player_decision,computer_name,line)                    
            player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
            if player_decision == 1:
                vc_5_4_1(player_decision,computer_name,line) 
            elif player_decision == 2:
                vc_5_3_1(player_decision,computer_name,line) 
            elif player_decision == 3:
                vc_5_2_1(computer_name,line)    
        elif player_decision == 2:
            vc_9_7_5(player_decision,computer_name,line)                     
            player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
            if player_decision == 1:
                vc_5_3_1(player_decision,computer_name,line)
            elif player_decision == 2: 
                vc_5_3_1(player_decision,computer_name,line)
            elif player_decision == 3:
                vc_5_2_1(player_decision,computer_name,line)          
        elif player_decision == 3:
            vc_9_6_5(player_decision,computer_name,line)                     
            player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
            if player_decision == 1:
                vc_5_4_1(player_decision,computer_name,line)
            elif player_decision == 2:
                vc_5_3_1(player_decision,computer_name,line) 
            elif player_decision == 3: 
                vc_5_2_1(player_decision,computer_name,line)   
    elif player_decision == 2:
        vc_13_11_9(player_decision,computer_name,line)                                        
        player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
        if player_decision == 1:
            vc_9_8_5(player_decision,computer_name,line)                     
            player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
            if player_decision == 1:
                vc_5_3_1(player_decision,computer_name,line)                 
            elif player_decision == 2:
                vc_5_3_1(player_decision,computer_name,line) 
            elif player_decision == 3:
                vc_5_2_1(player_decision,computer_name,line)    
        elif player_decision == 2: 
            vc_9_7_5(player_decision,computer_name,line)                    
            player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
            if player_decision == 1:
                vc_5_3_1(player_decision,computer_name,line)
            elif player_decision == 2: 
                vc_5_3_1(player_decision,computer_name,line)
            elif player_decision == 3:
                vc_5_2_1(player_decision,computer_name,line)          
    elif player_decision == 3:
        vc_13_10_9(player_decision,computer_name,line)
        player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
        if player_decision == 1:
            vc_9_8_5(player_decision,computer_name,line)
            player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
            if player_decision == 1:
                vc_5_4_1(player_decision,computer_name,line)
                player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
            elif player_decision == 2:
                    vc_9_7_5(player_decision,computer_name,line)
                    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
            elif player_decision == 3:
                    vc_9_6_5(player_decision,computer_name,line)
                    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
        elif player_decision == 2:
            vc_9_7_5(player_decision,computer_name,line)
            player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
            if player_decision == 1:
                vc_5_4_1(player_decision,computer_name,line)
                player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
            elif player_decision == 2:
                vc_5_3_1(player_decision,computer_name,line)
                player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
            elif player_decision == 3:
                vc_5_2_1(player_decision,computer_name,line)
        elif player_decision == 3:
            vc_9_6_5(player_decision,computer_name,line)
            player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
            if player_decision == 1:
                vc_5_4_1(player_decision,computer_name,line)
                player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
            elif player_decision == 2:
                vc_5_3_1(player_decision,computer_name,line)
                player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
            elif player_decision == 3:
                vc_5_2_1(player_decision,computer_name,line)        
 
def from_15_to_victory(computer_name,player_name,player_decision,line):              
        vc_15_12_9(player_decision,computer_name,line)
        player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
        if player_decision == 1:
           vc_9_8_5(player_decision,computer_name,line) 
        elif player_decision == 2:
           vc_9_7_5(player_decision,computer_name,line)
        elif player_decision == 3:
           vc_9_6_5(player_decision,computer_name,line)   
        player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))   
        if player_decision == 1:
           vc_5_4_1(player_decision,computer_name,line) 
        elif player_decision == 2:
           vc_5_3_1(player_decision,computer_name,line)
        elif player_decision == 3:
           vc_5_2_1(player_decision,computer_name,line)              
                
                
                
                
                
                
                      
#######################################################################
def main():

    player_name   = "Yonatan"
    computer_name = "Moti"
    line = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]    
    
    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
    if   player_decision == 1:              #15-->14 
        line = vc_15_14_13(player_decision,computer_name,line)
        line = from_13_to_victory(computer_name,player_name,line)       
######################################################################################    
    
    
    if   player_decision == 2:              #15-->13
        p_2(player_decision,line)
        print("\n" + computer_name + ",how many sticks do you want to remove ? " )
        computer_decision = rd.randint(1,3)
        print(computer_decision)
        if computer_decision == 1:
           c_1(computer_decision,line)
        elif computer_decision == 2:
            c_2(computer_decision,line)
        elif computer_decision == 3:
            c_3(computer_decision,line)     
        player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
        if player_decision == 1:
           p_1(player_decision,line)
        elif player_decision == 2:
            p_2(player_decision,line)
        elif player_decision == 3:
            p_3(player_decision,line)
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        if computer_decision == 1:
           c_1(computer_decision,line)
        elif computer_decision == 2:
            c_2(computer_decision,line)
        elif computer_decision == 3:
            c_3(computer_decision,line)
    #להוסיף מה קורה לאחר התגובה שלה לאקראיות שלי
    
    
##########################################################################################    
    if   player_decision == 3:              #15-->12
        from_15_to_victory(computer_name,player_name,player_decision,line)  
 
                   
if __name__ == "__main__":
        main() 
    
