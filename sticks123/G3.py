from msilib.schema import ListView
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

# def vc_5_3_1(player_decision,computer_name,line):#מחשב מנצח כששחקן לוקח 2 מקלות החל 5
#     p_2(player_decision,line)           #5-->3
#     computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
#     c_2(computer_decision,line)         #3-->1
#     print(computer_name, "  W I N !!!")

# def vc_5_4_1(player_decision,computer_name,line):#מחשב מנצח כששחקן לוקח מקל החל 5
#         p_1(player_decision,line)           #5-->4
#         computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
#         c_3(computer_decision,line)         #4-->1  
#         print(computer_name, "  W I N !!!")

# def vc_9_6_5(player_decision,computer_name,line):#מחשב מנצח כששחקן לוקח 2 מקלות החל 9
#         p_3(player_decision,line)           #9-->6
#         computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
#         c_1(computer_decision,line)             #6-->5     

# def vc_9_7_5(player_decision,computer_name,line):#מחשב מנצח כששחקן לוקח 2 מקלות החל 9 
#     p_2(player_decision,line)           #9-->7
#     computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
#     c_2(computer_decision,line)         #7-->5 

# def vc_9_8_5(player_decision,computer_name,line):#מחשב מנצח כששחקן לוקח מקל החל 9 
    p_1(player_decision,line)               #9-->8
    computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
    c_3(computer_decision,line)             #8-->5 

# def vc_13_12_9(player_decision,computer_name,line):#מחשב מנצח כששחקן לוקח מקל החל 13 
#         p_1(player_decision,line)                   #13-->12
#         computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
#         c_3(computer_decision,line)                 #12-->9  

# def vc_13_11_9(player_decision,computer_name,line):#מחשב מנצח כששחקן לוקח 2 מקלות החל 13 
#         p_2(player_decision,line)                   #13-->11
#         computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
#         c_2(computer_decision,line)                 #11-->9                      

# def vc_13_10_9(player_decision,computer_name,line):#מחשב מנצח כששחקן לוקח 3 מקלות החל 13 
#     p_3(player_decision,line)           #13--<10                              
#     computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
#     c_1(computer_decision,line)         #10-->9 

# def vc_15_14_13(player_decision,computer_name,line):#מחשב מנצח כששחקן לוקח מקל החל 15 
#     p_1(player_decision,line)
#     computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
#     c_1(computer_decision,line)         #14-->13 
#     return line 

# def vc_15_12_9(player_decision,computer_name,line):#מחשב מנצח כששחקן לוקח 3 מקלות החל 15
#     p_3(player_decision,line)
#     computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
#     c_1(computer_decision,line)         #10-->9 
#     return line 
     
# def from_13_to_victory(computer_name,player_name,line):
#     player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
#     if player_decision == 1:
#         vc_13_12_9(player_decision,computer_name,line)                                              
#         player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
#         if player_decision == 1: 
#             vc_9_8_5(player_decision,computer_name,line)                    
#             player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
#             if player_decision == 1:
#                 vc_5_4_1(player_decision,computer_name,line) 
#             elif player_decision == 2:
#                 vc_5_3_1(player_decision,computer_name,line) 
#             elif player_decision == 3:
#                 vc_5_2_1(computer_name,line)    
#         elif player_decision == 2:
#             vc_9_7_5(player_decision,computer_name,line)                     
#             player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
#             if player_decision == 1:
#                 vc_5_3_1(player_decision,computer_name,line)
#             elif player_decision == 2: 
#                 vc_5_3_1(player_decision,computer_name,line)
#             elif player_decision == 3:
#                 vc_5_2_1(player_decision,computer_name,line)          
#         elif player_decision == 3:
#             vc_9_6_5(player_decision,computer_name,line)                     
#             player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
#             if player_decision == 1:
#                 vc_5_4_1(player_decision,computer_name,line)
#             elif player_decision == 2:
#                 vc_5_3_1(player_decision,computer_name,line) 
#             elif player_decision == 3: 
#                 vc_5_2_1(player_decision,computer_name,line)   
#     elif player_decision == 2:
#         vc_13_11_9(player_decision,computer_name,line)                                        
#         player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
#         if player_decision == 1:
#             vc_9_8_5(player_decision,computer_name,line)                     
#             player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
#             if player_decision == 1:
#                 vc_5_3_1(player_decision,computer_name,line)                 
#             elif player_decision == 2:
#                 vc_5_3_1(player_decision,computer_name,line) 
#             elif player_decision == 3:
#                 vc_5_2_1(player_decision,computer_name,line)    
#         elif player_decision == 2: 
#             vc_9_7_5(player_decision,computer_name,line)                    
#             player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
#             if player_decision == 1:
#                 vc_5_3_1(player_decision,computer_name,line)
#             elif player_decision == 2: 
#                 vc_5_3_1(player_decision,computer_name,line)
#             elif player_decision == 3:
#                 vc_5_2_1(player_decision,computer_name,line)          
#     elif player_decision == 3:
#         vc_13_10_9(player_decision,computer_name,line)
#         player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
#         if player_decision == 1:
#             vc_9_8_5(player_decision,computer_name,line)
#             player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
#             if player_decision == 1:
#                 vc_5_4_1(player_decision,computer_name,line)
#                 player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
#             elif player_decision == 2:
#                     vc_9_7_5(player_decision,computer_name,line)
#                     player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
#             elif player_decision == 3:
#                     vc_9_6_5(player_decision,computer_name,line)
#                     player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
#         elif player_decision == 2:
#             vc_9_7_5(player_decision,computer_name,line)
#             player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
#             if player_decision == 1:
#                 vc_5_4_1(player_decision,computer_name,line)
#                 player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
#             elif player_decision == 2:
#                 vc_5_3_1(player_decision,computer_name,line)
#                 player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
#             elif player_decision == 3:
#                 vc_5_2_1(player_decision,computer_name,line)
#         elif player_decision == 3:
#             vc_9_6_5(player_decision,computer_name,line)
#             player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
#             if player_decision == 1:
#                 vc_5_4_1(player_decision,computer_name,line)
#                 player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
#             elif player_decision == 2:
#                 vc_5_3_1(player_decision,computer_name,line)
#                 player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
#             elif player_decision == 3:
#                 vc_5_2_1(player_decision,computer_name,line)        
 
# def from_15_to_victory(computer_name,player_name,player_decision,line):              
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






def c_mevi_p_M5_L4_LPV(player_name,computer_decision,line):
    c_1(computer_decision,line)
    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
    if player_decision == 1:
        p_3(player_decision,line)
        print(player_name," W O N !!!")
                
def c_mevi_p_M5_L3_LPV(player_name,computer_decision,line):
    c_2(computer_decision,line)
    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
    if player_decision == 3:
        p_2(player_decision,line)
        print(player_name," W O N !!!")

def c_mevi_p_M5_L2_LPV(player_name,computer_decision,line):
    c_3(computer_decision,line)
    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
    if player_decision == 1:
        p_1(player_decision,line)
        print(player_name," W O N !!!")


def c_mevi_p_M4_L2_LPV(player_name,line):
    c_2(player_decision,line)
    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
    if player_decision == 1:
        p_1(player_decision,line)
        print(player_name,"W O N !!!")

def c_mevi_p_M4_L3_LPV(player_name,computer_decision,line):
    c_1(computer_decision,line)
    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
    if player_decision == 2:
        p_2(player_decision,line)
        print(player_name,"W O N !!!")


def c_mevi_p_M3_L1_LPV(player_name,line):
    c_2(player_decision,line)
    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
    if player_decision == 1:
        p_1(player_decision,line)
        print(player_name,"W O N !!!")


def c_mevi_c_M4_LCV(computer_name,computer_decision,line):
    c_3(computer_decision,line)
    print(computer_name,"W O N !!!")     
    
def c_mevi_c_M3_LCV(computer_name,computer_decision,line):
    c_2(computer_decision,line)
    print(computer_name,"W O N !!!")

def c_mevi_c_M2_LCV(computer_name,computer_decision,player_decision,line):
    p_2(player_decision,line)        
    computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
    c_1(computer_decision,line)
    print(computer_name,"W O N !!!")    



def p_mevi_c_M5_L2_LCV(computer_name,computer_decision,player_decision,line):
    p_3(player_decision,line)
    computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
    c_1(computer_decision,line)
    print(computer_name," W O N !!!")

def p_mevi_c_M5_L3_LCV(computer_name,computer_decision,player_decision,line):
    p_2(player_decision,line)
    computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
    c_2(computer_decision,line)
    print(computer_name," W O N !!!")
    
def p_mevi_c_M5_L4_LCV(computer_name,computer_decision,player_decision,line):
    p_1(player_decision,line)
    computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
    c_3(computer_decision,line)
    print(computer_name," W O N !!!")


def p_mevi_c_M4_L3_LCV(computer_name,computer_decision,player_decision,line):
    p_1(player_decision,line)
    computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
    c_2(computer_decision,line)
    print(computer_name," W O N !!!")

def p_mevi_c_M4_L2_LCV(computer_name,computer_decision,player_decision,line):
    p_2(player_decision,line)
    computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
    c_1(computer_decision,line)
    print(computer_name," W O N !!!")


def p_mevi_c_M3_L2_LCV(computer_name,computer_decision,player_decision,line):
    p_1(player_decision,line)
    computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
    c_1(computer_decision,line)
    print(computer_name," W O N !!!")


def p_mevi_p_M4_LPV(player_name,player_decision,line):
    p_3(player_decision,line)
    print(player_name," W O N !!!")

def p_mevi_p_M3_LPV(player_name,player_decision,line):
    p_2(player_decision,line)
    print(player_name," W O N !!!")

def p_mevi_p_M2_LPV(player_name,player_decision,line):
    p_1(player_decision,line)         
    print(player_name,"W O N !!!")                      
#######################################################################
def main():

    player_name   = "Dror"
    computer_name = "Moti"
    line = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]    
    
    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
    # if   player_decision == 1:              #15-->14 
    #     line = vc_15_14_13(player_decision,computer_name,line)
    #     line = from_13_to_victory(computer_name,player_name,line)       
######################################################################################    
    
    
    if  player_decision == 2:                                          #15-->13
        p_2(player_decision,line)
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        if computer_decision == 1:
            c_1(computer_decision,line)                                 #13-->12 long
            player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
            if   player_decision == 1:                                  #12-->11 long
                p_1(player_decision,line)
                computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
                if computer_decision == 1:                              #11-->10 long
                    c_1(computer_decision,line) 
                    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
                    if player_decision   == 1:                          #10-->9 long
                        p_1(player_decision,line)
                        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
                        if computer_decision   == 1:                    #9-->8 long
                            c_1(computer_decision,line)
                            player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
                            if player_decision   == 1:                  #8-->7 long
                                p_1(player_decision,line) 
                                computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
                                if computer_decision     == 1:          #7-->6 long
                                    c_1(computer_decision,line) 
                                    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
                                    if player_decision   == 1:         #6-->5 long
                                        p_1(player_decision,line)    
                                        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
                                        if computer_decision   == 1:   #5-->4 long
                                            c_1(computer_decision,line)
                                            player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
                                            if player_decision   == 1:  #4-->3 long
                                                p_1(player_decision,line)
                                                computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
                                                if computer_decision == 1:#3-->2 long
                                                    c_1(computer_decision,line)
                                                    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
                                                    if player_decision == 1:
                                                        p_mevi_p_M2_LPV
                                                elif computer_decision == 2:#3-->1 long
                                                    c_mevi_c_M2_LCV
                                            elif player_decision == 2:  #4-->2 long 
                                                p_mevi_c_M4_L2_LCV
                                            elif player_decision == 3:  #4-->1 long  
                                                p_mevi_p_M4_LPV
                                        elif computer_decision == 2:    #5-->3 long
                                            c_2(computer_decision,line)       
                                            player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
                                            if player_decision == 1:    #3-->2 long
                                                p_1(player_decision,line)
                                            elif player_decision == 2:  #3-->1
                                                mevi_azmo_M3_LV   
                                                computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
                                                if computer_decision == 1:
                                                    print(computer_name," W O N !!!")
                                        elif computer_decision == 3:    #5-->2 long
                                            c_mevi_p_M5_L2_LPV                                            
                                    elif player_decision == 2:          #6-->4 long
                                        p_2(player_decision,line)
                                        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
                                        if   computer_decision == 1:    #4-->3 long
                                            c_1(computer_decision,line)
                                            player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
                                            if player_decision == 1:    #3-->2 long
                                                p_mevi_c_M3_L2_LCV
                                            elif player_decision == 2:# 3-->1 long
                                                p_mevi_p_M3_LPV                                            
                                        elif computer_decision == 2:    #4-->2 long
                                            c_2(computer_decision,line)
                                            player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
                                            if player_decision == 1: 
                                                p_mevi_p_M2_LPV                                                                                            
                                        elif computer_decision == 3:    #4-->1 long
                                            c_mevi_c_M4_LCV                                                         
                                    elif player_decision == 3:          #6-->3 long 
                                        p_3(player_decision,line) 
                                        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
                                        if computer_decision == 1:#2 long
                                            c_1(computer_decision,line)
                                            player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
                                            if player_decision == 1:
                                              print(player_name," W O N !!!")
                                        elif computer_decision == 2:
                                            c_1(computer_decision,line) 
                                            print(computer_name," W O N !!!")         
                                elif computer_decision   == 2:          #7-->5 long
                                    c_2(computer_decision,line)
                                    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
                                    if player_decision   == 1:#4 long
                                        p_1(player_decision,line)
                                        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
                                        if computer_decision   == 1:#2 long
                                            c_1(computer_decision,line)
                                            player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
                                            if player_decision   == 1:#2 long
                                                p_1(player_decision,line)
                                                computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
                                                if computer_decision   == 1:#1 long
                                                    c_mevi_c_M2_LCV
                                            elif player_decision ==2:
                                                p_mevi_p_M2_LPV                               
                                        elif computer_decision == 2: #1 long
                                            c_2(computer_decision,line)
                                            player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
                                            p_mevi_p_M2_LPV                                           
                                        elif computer_decision == 3: #1 long
                                            c_3(computer_decision,line)   
                                            if player_decision   == 1:#2 long
                                                p_mevi_c_M3_L2_LCV                                                                 
                                    elif player_decision == 2:#3 long
                                        p_2(player_decision,line)
                                        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
                                        if computer_decision == 1: #2 long
                                            c_1(computer_decision,line)                                   
                                            player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
                                            if player_decision   == 1:#1 long
                                                print(player_name,"W O N !!!")
                                        elif computer_decision == 2: #1 long 
                                            c_mevi_c_M3_LCV                 
                                    elif player_decision == 3:
                                        p_3(player_decision,line) #2 long
                                        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
                                        if computer_decision == 1:
                                            c_mevi_c_M2_LCV               
                                elif computer_decision   == 3:          #7-->4 long
                                    c_3(computer_decision,line)
                                    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
                                    if player_decision   == 1:      #3 long
                                        p_1(player_decision,line)
                                        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
                                        if computer_decision == 1:#2 long
                                            c_1(computer_decision,line)
                                            player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
                                            if player_decision == 1:
                                                p_mevi_p_M2_LPV                                                   
                                        elif computer_decision == 2:
                                            c_mevi_c_M3_LCV
                                            c_2(computer_decision,line)
                                            print(computer_name,"W O N !!!")      
                                    elif player_decision == 2:      #2 long
                                        p_2(player_decision,line)
                                        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
                                        if computer_decision == 1:
                                            c_mevi_c_M2_LCV
                                    elif player_decision == 3:      #1 long
                                        p_mevi_p_M3_LPV                                    
                            elif player_decision == 2:                  #8-->6 long
                                p_2(player_decision,line)
                                computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
                                if computer_decision   == 1:#5 long
                                    c_1(computer_decision,line)
                                    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
                                    if player_decision == 1:#4 long
                                        p_1(player_decision,line) 
                                        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
                                        if computer_decision   == 1:#3 long
                                            c_1(computer_decision,line)                                            
                                            player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
                                            if player_decision == 1:#2 long
                                                p_2(player_decision,line)
                                                computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
                                                if computer_decision   == 1:#1 long
                                                    c_mevi_c_M2_LCV    
                                            elif player_decision == 2:#1 long
                                                p_mevi_p_M2_LPV
                                        elif computer_decision == 2:#2 long
                                            c_2(computer_decision,line)
                                            player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
                                            if player_decision == 1: #1 long
                                                p_mevi_p_M2_LPV                                          
                                        elif computer_decision == 3:#1 long
                                            c_mevi_c_M4_LCV
                                    elif player_decision == 2:#3 long
                                        p_2(player_decision,line)        
                                        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
                                        if computer_decision   == 1:#2 long     
                                            c_2(computer_decision,line)   
                                            player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
                                            if player_decision == 1: #1 long
                                                p_1(player_decision,line)
                                                print(player_name,"W O N !!!")
                                        elif computer_decision   == 2:#1 long     
                                            c_1(computer_decision,line)  
                                            print(computer_name,"W O N !!!")    
                                    elif player_decision == 3:#2 long
                                        p_1(player_decision,line)
                                        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
                                        if computer_decision   == 1:#1 long     
                                            c_1(computer_decision,line)                               
                                            print(computer_name,"W O N !!!")
                                elif computer_decision == 2:#4 long
                                    c_2(computer_decision,line)
                                    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
                                    if player_decision == 1:#3 long
                                        p_1(player_decision,line)
                                        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
                                        if computer_decision   == 1:#2 long
                                            c_2(computer_decision,line)        
                                            player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
                                            if player_decision == 1:#1 long
                                                print(player_name,"W O N !!!")
                                        elif computer_decision == 2:#1 long
                                            c_1(computer_decision,line)
                                            print(computer_name,"W O N !!!")
                                    elif player_decision == 2:#2 long
                                        p_2(player_decision,line)
                                        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
                                        c_1(computer_decision,line)
                                        print(computer_name,"W O N !!!")
                                    elif player_decision == 3:#1 long
                                        p_2(player_decision,line)
                                        print(player_name,"W O N !!!")
                                elif computer_decision == 3:#3 long
                                    c_3(computer_decision,line)
                                    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
                                    if player_decision == 1:#2 long                        
                                        p_1(player_decision,line)
                                        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
                                        c_1(computer_decision,line)
                                        print(computer_name,"W O N !!!")
                                    if player_decision == 2:#1 long                        
                                        p_2(player_decision,line)       
                                        print(player_name,"W O N !!!")
                            elif player_decision == 3:                  #8-->5 long
                                p_3(player_decision,line)
                                computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
                                if   computer_decision   == 1:          #5-->4 long
                                    c_1(computer_decision,line)    
                                    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
                                    if player_decision   == 1:          #4-->3 long 
                                        p_1(player_decision,line)
                                        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
                                        if computer_decision   == 1:#2 long
                                            c_1(computer_decision,line)
                                            player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
                                            if player_decision == 1:#1 long
                                                p_mevi_p_M2_LPV                                         
                                        elif computer_decision   == 2:#1 long
                                            c_mevi_c_M3_LCV                               
                                    elif player_decision == 2:          #4-->2 long 
                                        c_mevi_c_M2_LCV
                                    elif player_decision == 3:          #4--<1 long 
                                        p_mevi_p_M4_LPV                          
                                elif computer_decision   == 2:          #5-->3 long
                                    c_2(computer_decision,line)    
                                    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
                                    if player_decision == 1:            #3--<2 long 
                                        p_1(player_decision,line)
                                        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
                                        c_mevi_c_M2_LCV                                           
                                    elif player_decision == 2:          #3--<1 long 
                                        p_mevi_p_M2_LPV                                          
                                elif computer_decision   == 3:          #5-->2 long
                                    c_mevi_p_M5_L2_LPV

#                                 p_2(player_decision,line)        
#                                 computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
                                              
                                       
    
# ##########################################################################################    
    #if   player_decision == 3:              #15-->12
        #from_15_to_victory(computer_name,player_name,player_decision,line)  
 
                   
if __name__ == "__main__":
        main() 
    
