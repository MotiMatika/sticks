# import random as rd
# player_name   = "Dror"
# computer_name = "Moti"
# # פונקציות רלוונטיות לשימוש
#  def from_9_to_5(player_name,computer_name):#משופרת
# #     line = [1,2,3,4,5,6,7,8,9]
# #     num_of_sticks = len(line)
# #     player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
# #     if player_decision == 1:
# #         num_of_sticks = num_of_sticks - player_decision
# #         print("Now we have",num_of_sticks,"sticks")
# #         for i in range (player_decision):
# #             line.pop()
# #         print(line)
#         computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
#         num_of_sticks = num_of_sticks - computer_decision
#         print("Now we have",num_of_sticks,"sticks")
#         for i in range (computer_decision):
#             line.pop()
#         print(line)
#         from_5_to_1
#     if player_decision == 2:
#         num_of_sticks = num_of_sticks - player_decision
#         print("Now we have",num_of_sticks,"sticks")
#         for i in range (player_decision):
#             line.pop()
#         print(line)
#         computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
#         num_of_sticks = num_of_sticks - computer_decision
#         print("Now we have",num_of_sticks,"sticks")
#         for i in range (computer_decision):
#             line.pop()
#         print(line)
#         from_5_to_1
#     if player_decision == 3:
#         num_of_sticks = num_of_sticks - player_decision
#         print("Now we have",num_of_sticks,"sticks")
#         for i in range (player_decision):
#             line.pop()
#         print(line)
#         computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
#         num_of_sticks = num_of_sticks - computer_decision
#         print("Now we have",num_of_sticks,"stick")
#         for i in range (1):
#             line.pop()
#         print(line)
#         from_5_to_1
# def from_5_to_1(player_name,computer_name):
#     line = [1,2,3,4,5]
#     num_of_sticks = len(line)
#     player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
#     if player_decision == 1:
#         num_of_sticks = num_of_sticks - 1
#         print("Now we have",num_of_sticks,"sticks")
#         for i in range (1):
#             line.pop()
#         print(line)
#         computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
#         num_of_sticks = num_of_sticks - computer_decision
#         print("Now we have",num_of_sticks,"stick")
#         for i in range (3):
#             line.pop()
#         print(line)
#         print(computer_name," W O N !!!")
#         print("       END of GAME")
#     if player_decision == 2:
#         num_of_sticks = num_of_sticks - 2
#         print("Now we have",num_of_sticks,"sticks")
#         for i in range (2):
#             line.pop()
#         print(line)
#         computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
#         num_of_sticks = num_of_sticks - computer_decision
#         print("Now we have",num_of_sticks,"stick")
#         for i in range (2):
#             line.pop()
#         print(line)
#         print(computer_name," W O N !!!")
#         print("       END of GAME")
#     if player_decision == 3:
#         num_of_sticks = num_of_sticks - 3
#         print("Now we have",num_of_sticks,"sticks")
#         for i in range (3):
#             line.pop()
#         print(line)
#         computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
#         num_of_sticks = num_of_sticks - computer_decision
#         print("Now we have",num_of_sticks,"stick")
#         for i in range (1):
#             line.pop()
#         print(line)
#         print(computer_name," W O N !!!")
#         print("       END of GAME") 


def DROR_win_9(player_name,computer_name):
    print("\n",computer_name, "decided to remove",rd.randint(1,3))
    num_of_sticks = num_of_sticks - player_decision
    print("Now we have",num_of_sticks,"sticks")
    for i in range (player_decision):
        line.pop()
    print(line)         
    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
    if   player_decision == 1:
        num_of_sticks = num_of_sticks - player_decision
        print("Now we have",num_of_sticks,"sticks")
        for i in range (player_decision):
            line.pop()
        pick_sticks = rd.randint(1,3)
        print("\n",computer_name, "decided to remove",pick_sticks)
        num_of_sticks = num_of_sticks - player_decision
        print("Now we have",num_of_sticks,"sticks")
        for i in range (player_decision):
            line.pop()
        print(line)
        print(player_name,"W O N !!!")
def DROR_win_5(player_name,computer_name) :       
#def RD_1(player_name,computer_name):
    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
    if player_decision == 1:#EE
        print("Now we have",num_of_sticks,"sticks")
        for i in range (player_decision):
            line.pop()
        print(line)
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        num_of_sticks = num_of_sticks - computer_decision
        print("Now we have",num_of_sticks,"sticks")
        for i in range (computer_decision):
            line.pop()
        print(line)
        from_5_to_1(player_name,computer_name)
    if player_decision == 2:#FF
        print("Now we have",num_of_sticks,"sticks")
        for i in range (player_decision):
            line.pop()
        print(line)
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        num_of_sticks = num_of_sticks - computer_decision
        print("Now we have",num_of_sticks,"stick")
        for i in range (computer_decision):
            line.pop()
        print(line)
        from_5_to_1(player_name,computer_name)
    if player_decision == 3:#GG
        num_of_sticks = 8
        print("Now we have",num_of_sticks,"sticks")
        for i in range (player_decision):
            line.pop()
        print(line)#נותרו 5###########################################################
        pick_sticks = rd.randint(1,3)
        print("\n",computer_name, "decided to remove",pick_sticks)
        if pick_sticks == 1:
            num_of_sticks = length-pick_sticks
            print("Now we have",num_of_sticks,"sticks")
            for i in range (pick_sticks):
                line.pop()
                print(line)#נותרו 4
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        num_of_sticks = num_of_sticks - computer_decision
        print("Now we have",num_of_sticks,"sticks")
        for i in range (computer_decision):
            line.pop()
        print(line)
        print(player_name," W O N !!!")
    print("       END of GAME")
def RD_Com(num_of_sticks,pick_sticks):
    print("\n",computer_name, "decided to remove",pick_sticks)
    num_of_sticks = num_of_sticks -pick_sticks
    print("Now we have",num_of_sticks,"sticks")
    for i in range (pick_sticks):
        line.pop()
    print(line)
 

#לאחר שהשחקן בחר לקחת 2
print("\n"+"Now we have 13 sticks")
line = [1,2,3,4,5,6,7,8,9,10,11,12,13]
num_of_sticks = len(line)
print(line)#נותרו 13
#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
pick_sticks = 1     #rd.randint(1,3)#AAAAA
# print("\n",computer_name, "decided to remove",pick_sticks)#AAAAA
if pick_sticks == 1: #AAAAA
    RD_Com(num_of_sticks,pick_sticks)
    # num_of_sticks = length-pick_sticks
    # print("Now we have",num_of_sticks,"sticks")
    # for i in range (pick_sticks):
    #     line.pop()
    # print(line)
    # length = len(line)
    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
    if  player_decision == 1:#BB
        num_of_sticks = num_of_sticks - player_decision#נותרו 11
        print("Now we have",num_of_sticks,"sticks")
        for i in range (player_decision):
            line.pop()
        print(line)#נותרו 11
        length = len(line)
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        num_of_sticks = num_of_sticks - computer_decision
        print("Now we have",num_of_sticks,"sticks")
        for i in range (computer_decision):
            line.pop()
        print(line)#נותרו 9
        length = len(line)
        from_9_to_5(player_name,computer_name)
        from_5_to_1(player_name,computer_name)
    elif player_decision == 2:#CC
        num_of_sticks = num_of_sticks - player_decision#10 נותרו
        print("Now we have",num_of_sticks,"sticks")
        for i in range (player_decision):
            line.pop()
        print(line)#נותרו 10
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        num_of_sticks = num_of_sticks - computer_decision
        print("Now we have",num_of_sticks,"sticks")
        for i in range (computer_decision):
            line.pop()
        print(line)
        from_9_to_5(player_name,computer_name)
        from_5_to_1(player_name,computer_name)
    elif player_decision == 3:#DD
        num_of_sticks = 9
        print("Now we have",num_of_sticks,"sticks")
        num_of_sticks = num_of_sticks - player_decision#נותרו 9
        for i in range (player_decision):
            line.pop()
        print(line)#נותרו 9
        #oved
        pick_sticks = 1#rd.randint(1,3)
        print("\n",computer_name, "decided to remove",pick_sticks)
        if pick_sticks == 1:#נותרו 8
            num_of_sticks = 8
            print("Now we have",num_of_sticks,"sticks")
            for i in range (pick_sticks):
                line.pop()
            print(line)#נותרו 8
            player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
            if player_decision == 1:#נותרו 7
                num_of_sticks = num_of_sticks - player_decision
                print("Now we have",num_of_sticks,"sticks")
                for i in range (player_decision):
                    line.pop()
                print(line) #נותרו 7 
                computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
                from_5_to_1
            if player_decision == 2:#נותרו 6
                num_of_sticks = num_of_sticks - player_decision
                print("Now we have",num_of_sticks,"sticks")
                for i in range (player_decision):
                    line.pop()
                print(line) #נותרו 5
                computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
                for i in range (computer_decision):
                    line.pop()
                print(line)
                from_5_to_1
            if player_decision == 3:# נותרו 5
                DROR_win_5
                # num_of_sticks = num_of_sticks - player_decision
                # print("Now we have",num_of_sticks,"sticks")
                # for i in range (player_decision):
                #     line.pop()
                # print(line) #נותרו 4
                # pick_sticks = rd.randint(1,3)
                # print(computer_name,"decided to take",pick_sticks,"sticks")
                # for i in range (pick_sticks):
                #     line.pop()
                # print(line)
                # player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
                # num_of_sticks = num_of_sticks - player_decision
                # for i in range (player_decision):
                #     line.pop()
                # print(line)
                # print(player_name,"W O N !!!")
if pick_sticks == 2:

    num_of_sticks = length-pick_sticks
    print("Now we have",num_of_sticks,"sticks")
    for i in range (pick_sticks):
        line.pop()
    print(line)
    length = len(line)
    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
    if  player_decision == 1:#נותרו 6
        num_of_sticks = num_of_sticks - player_decision#נותרו 6
        print("Now we have",num_of_sticks,"sticks")
        for i in range (player_decision):
            line.pop()
        print(line)#נותרו 6
        
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        num_of_sticks = num_of_sticks - computer_decision
        print("Now we have",num_of_sticks,"sticks")
        for i in range (computer_decision):
            line.pop()
        print(line)#נותרו 5
        from_5_to_1(player_name,computer_name)
    elif player_decision == 2:
        num_of_sticks = num_of_sticks - player_decision#10 נותרו
        print("Now we have",num_of_sticks,"sticks")
        for i in range (player_decision):
            line.pop()
        print(line)#נותרו 5
        print(computer_name,"decided to take",rd.randint,"sticks")
        num_of_sticks = num_of_sticks - computer_decision
        print("Now we have",num_of_sticks,"sticks")
        for i in range (computer_decision):
            line.pop()
        print(line)
        DROR_win
    elif player_decision == 3:
        num_of_sticks = num_of_sticks - player_decision#4 נותרו
        print("Now we have",num_of_sticks,"sticks")
        num_of_sticks = num_of_sticks - player_decision#נותרו 4
        for i in range (player_decision):
            line.pop()
        print(line)#נותרו 4 
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        num_of_sticks = num_of_sticks - computer_decision
        print("Now we have",num_of_sticks,"sticks")
        for i in range (computer_decision):
            line.pop()
        print(computer_name,"W O N !!!")            



if pick_sticks == 3:

    num_of_sticks = length-pick_sticks#נותרו 6
    print("Now we have",num_of_sticks,"sticks")
    for i in range (pick_sticks):
        line.pop()
    print(line)
    length = len(line)#נותרו 6
    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
    if  player_decision == 1:#נותרו 5
        num_of_sticks = num_of_sticks - player_decision#נותרו 6
        print("Now we have",num_of_sticks,"sticks")
        for i in range (player_decision):
            line.pop()
        print(line)#נותרו 5
        DROR_win
        # computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        # num_of_sticks = num_of_sticks - computer_decision
        # print("Now we have",num_of_sticks,"sticks")
        # for i in range (computer_decision):
        #     line.pop()
        # print(line)#נותרו 5
        # from_5_to_1(player_name,computer_name)
    elif player_decision == 2:
        num_of_sticks = num_of_sticks - player_decision#4 נותרו
        print("Now we have",num_of_sticks,"sticks")
        for i in range (player_decision):
            line.pop()
        print(line)#נותרו 4
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        num_of_sticks = num_of_sticks - computer_decision
        print("Now we have",num_of_sticks,"sticks")
        for i in range (computer_decision):
            line.pop()
        print(computer_name,"W O N !!!") 
    elif player_decision == 3:
        num_of_sticks = num_of_sticks - player_decision#3 נותרו
        print("Now we have",num_of_sticks,"sticks")
        for i in range (player_decision):
            line.pop()
        print(line)#נותרו 3
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        num_of_sticks = num_of_sticks - computer_decision
        print("Now we have",num_of_sticks,"sticks")
        for i in range (computer_decision):
            line.pop()
        print(computer_name,"W O N !!!")
        
        
        
        
        
        
        print(computer_name,"decided to take",rd.randint,"sticks")
        num_of_sticks = num_of_sticks - computer_decision
        print("Now we have",num_of_sticks,"sticks")
        for i in range (computer_decision):
            line.pop()
        print(line)
        DROR_win
    elif player_decision == 3:
        num_of_sticks = num_of_sticks - player_decision#4 נותרו
        print("Now we have",num_of_sticks,"sticks")
        num_of_sticks = num_of_sticks - player_decision#נותרו 4
        for i in range (player_decision):
            line.pop()
        print(line)#נותרו 4 
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        num_of_sticks = num_of_sticks - computer_decision
        print("Now we have",num_of_sticks,"sticks")
        for i in range (computer_decision):
            line.pop()
        print(computer_name,"W O N !!!")  






















        
# #BBBBB        
# if pick_sticks == 2:#נותרו 11
#     num_of_sticks = 11
#     num_of_sticks = num_of_sticks-pick_sticks#נותרו 7
#     print("Now we have",num_of_sticks,"sticks")
#     for i in range (pick_sticks):
#         line.pop()
#     print(line)#נותרו 11
#         # ###################################    
#     num_of_sticks = 11
#     player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
    
#     if player_decision == 1:
#         num_of_sticks = num_of_sticks - player_decision
#         print("Now we have",num_of_sticks,"sticks")
#         for i in range (player_decision):
#             line.pop()
#         print(line)  
#         computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
#         num_of_sticks = num_of_sticks - computer_decision
#         print("Now we have",num_of_sticks,"stick")
#         for i in range (computer_decision):
#             line.pop()
#         print(line)
#         #עובד
#         from_9_to_5(player_name,computer_name) 
#         from_5_to_1(player_name,computer_name) 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if player_decision == 2:
        #     num_of_sticks = num_of_sticks - player_decision
        #     print("Now we have",num_of_sticks,"sticks")
        #     for i in range (player_decision):
        #         line.pop()
        #     print(line)  
        #     pick_sticks = rd.randint(1,3)
        #     print("\n",computer_name, "decided to remove",pick_sticks)
        #     num_of_sticks = num_of_sticks - pick_sticks
        #     print("Now we have",num_of_sticks,"stick")
        #     for i in range (pick_sticks):
        #         line.pop()
        #     print(line)
        #     RD_DROR (player_name,computer_name)
        # if player_decision == 3:
        #     num_of_sticks = num_of_sticks - player_decision
        #     print("Now we have",num_of_sticks,"sticks")
        #     for i in range (player_decision):
        #         line.pop()
        #     print(line)  
        #     computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        #     num_of_sticks = num_of_sticks - computer_decision
        #     print("Now we have",num_of_sticks,"stick")
        #     for i in range (computer_decision):
        #         line.pop()
        #     print(line)
        #     print(computer_name,"W O N !!!")     
        #    # RD_1(player_name,computer_name)
        























# HHH
# def RD_2():
#     if player_decision == 2:
#         print("Now we have",num_of_sticks,"sticks")
#         for i in range (player_decision):
#             line.pop()
#         print(line)
#         computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
#         num_of_sticks = num_of_sticks - computer_decision
#         print("Now we have",num_of_sticks,"sticks")
#         for i in range (computer_decision):
#             line.pop()
#         print(line)
#         from_5_to_1(player_name,computer_name)
# def RD_3():
#         computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
#         num_of_sticks = num_of_sticks - computer_decision
#         print("Now we have",num_of_sticks,"sticks")
#         for i in range (computer_decision):
#             line.pop()
#         print(line)
#         player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))



    
    
    
# #if pick_sticks == 2:
#     # num_of_sticks = length-pick_sticks
#     # print("Now we have",num_of_sticks,"sticks")
#     # for i in range (pick_sticks):
#     #     line.pop()
#     # print(line)
#     # player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
#     # if player_decision == 1:
#         num_of_sticks = 13-pick_sticks - player_decision
#         print("Now we have",num_of_sticks,"sticks")
#         for i in range (player_decision):
#             line.pop()
#         print(line)
#         computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
#         num_of_sticks = num_of_sticks - computer_decision
#         print("Now we have",num_of_sticks,"sticks")
#         for i in range (computer_decision):
#             line.pop()
#         print(line)
#         from_9_to_5(player_name,computer_name)
#         from_5_to_1(player_name,computer_name)
        
# elif pick_sticks==2:
#     delete_sticks()
# elif pick_sticks==3:
#     delete_sticks()

#oved




# player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
# if player_decision == 1:
#     num_of_sticks = num_of_sticks - player_decision
#     print("Now we have",num_of_sticks,"sticks")
#     for i in range (1):
#         line.pop()
#     print(line)
    
# computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
# num_of_sticks = len(line)-computer_decision
# print("Now we have",num_of_sticks,"sticks")
# for i in range (computer_decision):
#         line.pop()
# print(line)
# if len(line) == 9:
#     from_9_to_5(player_name,computer_name)
#     from_5_to_1(player_name,computer_name)
# if player_decision == 2:
#     num_of_sticks = num_of_sticks - 2
#     print("Now we have",num_of_sticks,"sticks")
#     for i in range (2):
#         line.pop()
#     print(line)
    #     computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
    #     num_of_sticks = num_of_sticks - computer_decision
    #     print("Now we have",num_of_sticks,"sticks")
    #     for i in range (2):
    #         line.pop()
    #     print(line)
    # if player_decision == 3:
    #     num_of_sticks = num_of_sticks - 3
    #     print("Now we have",num_of_sticks,"sticks")
    #     for i in range (3):
    #         line.pop()
    #     print(line)
    #     computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
    #     num_of_sticks = num_of_sticks - computer_decision
    #     print("Now we have",num_of_sticks,"stick")
    #     for i in range (1):
    #         line.pop()
    #     print(line)