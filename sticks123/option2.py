import random as rd
player_name   = "Dror"
computer_name = "Moti"
def from_9_to_5(player_name,computer_name):
    line = [1,2,3,4,5,6,7,8,9]
    num_of_sticks = len(line)
    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
    if player_decision == 1:
        num_of_sticks = num_of_sticks - 1
        print("Now we have",num_of_sticks,"sticks")
        for i in range (1):
            line.pop()
        print(line)
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        num_of_sticks = num_of_sticks - computer_decision
        print("Now we have",num_of_sticks,"sticks")
        for i in range (3):
            line.pop()
        print(line)
    if player_decision == 2:
        num_of_sticks = num_of_sticks - 2
        print("Now we have",num_of_sticks,"sticks")
        for i in range (2):
            line.pop()
        print(line)
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        num_of_sticks = num_of_sticks - computer_decision
        print("Now we have",num_of_sticks,"sticks")
        for i in range (2):
            line.pop()
        print(line)
    if player_decision == 3:
        num_of_sticks = num_of_sticks - 3
        print("Now we have",num_of_sticks,"sticks")
        for i in range (3):
            line.pop()
        print(line)
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        num_of_sticks = num_of_sticks - computer_decision
        print("Now we have",num_of_sticks,"stick")
        for i in range (1):
            line.pop()
        print(line)
def from_5_to_1(player_name,computer_name):
    line = [1,2,3,4,5]
    num_of_sticks = len(line)
    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
    if player_decision == 1:
        num_of_sticks = num_of_sticks - 1
        print("Now we have",num_of_sticks,"sticks")
        for i in range (1):
            line.pop()
        print(line)
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        num_of_sticks = num_of_sticks - computer_decision
        print("Now we have",num_of_sticks,"stick")
        for i in range (3):
            line.pop()
        print(line)
        print(computer_name," W O N !!!")
        print("       END of GAME")
    if player_decision == 2:
        num_of_sticks = num_of_sticks - 2
        print("Now we have",num_of_sticks,"sticks")
        for i in range (2):
            line.pop()
        print(line)
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        num_of_sticks = num_of_sticks - computer_decision
        print("Now we have",num_of_sticks,"stick")
        for i in range (2):
            line.pop()
        print(line)
        print(computer_name," W O N !!!")
        print("       END of GAME")
    if player_decision == 3:
        num_of_sticks = num_of_sticks - 3
        print("Now we have",num_of_sticks,"sticks")
        for i in range (3):
            line.pop()
        print(line)
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        num_of_sticks = num_of_sticks - computer_decision
        print("Now we have",num_of_sticks,"stick")
        for i in range (1):
            line.pop()
        print(line)
        print(computer_name," W O N !!!")
        print("       END of GAME") 
def RD_1(player_name,computer_name):
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
        print("Now we have",num_of_sticks,"sticks")
        for i in range (computer_decision):
            line.pop()
        print(line)
        from_5_to_1(player_name,computer_name)
        if player_decision == 3:#GG
            print("Now we have",num_of_sticks,"sticks")
            for i in range (player_decision):
                line.pop()
            print(line)
            pick_sticks = rd.randint(1,3)
            print("\n",computer_name, "decided to remove",pick_sticks)
            print("Now we have",num_of_sticks,"sticks")
            for i in range (player_decision):
                line.pop()
            print(line)
            player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
            if player_decision == 1:#u take 3 and lose
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
            print(player_name," W O N !!!")
        print("       END of GAME")
            
        ########################################################continue yarok HHH    
            
            
            # if player_decision == 2: u take 2 and lose    
            # if player_decision == 3: u take 1 and lose

#def from_13_to_rrrr(player_name,computer_name):


print("\n"+"Now we have 13 sticks")
line = [1,2,3,4,5,6,7,8,9,10,11,12,13]
length = len(line)
print(line)
pick_sticks = rd.randint(1,3)
print("\n",computer_name, "decided to remove",pick_sticks)
if pick_sticks == 1: #AAAAA
    num_of_sticks = length-pick_sticks
    print("Now we have",num_of_sticks,"sticks")
    for i in range (pick_sticks):
        line.pop()
    print(line)
    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
    if   player_decision == 1:#BB
        num_of_sticks = 13-pick_sticks - player_decision
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
        from_9_to_5(player_name,computer_name)
        from_5_to_1(player_name,computer_name)
    elif player_decision == 2:#CC
        num_of_sticks = 13-pick_sticks - player_decision
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
        from_9_to_5(player_name,computer_name)
        from_5_to_1(player_name,computer_name)
    elif player_decision == 3:#DD
        print("Now we have",num_of_sticks,"sticks")
        num_of_sticks = num_of_sticks - player_decision
        for i in range (player_decision):
            line.pop()
        print(line)
        pick_sticks = rd.randint(1,3)
        print("\n",computer_name, "decided to remove",pick_sticks)
        RD_1(player_name,computer_name)
























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