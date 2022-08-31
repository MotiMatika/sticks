import random as rd
def openning(line):
    print("\nS T I C K S")

    print("\n|  |  |  |  |  |  |  |  |  |  |")

    print("""\nYou have to remove,
        one,
        or two
        or three sticks.
        The player who takes the last stick - LOSES""")
    
    print("\n"+"This is the line of the sticks")
    print("\n",line)
    
def type_player(player_decision,line):                      #good מכילה הוראות צמצום רשימה והדפסתה
    for i in range (player_decision):
        line.pop()
    print(line)
    return line 

def type_computer(computer_decision,line):                  #good מכילה הוראות צמצום רשימה והדפסתה
    for i in range (computer_decision):
        line.pop()
    print(line)
    return line

def victory_computer(player_decision,computer_name,line):
        num_of_sticks = len(line) - player_decision
        print("Now we have",num_of_sticks,"sticks")
        line = type_player(player_decision,line) 
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        num_of_sticks = num_of_sticks - computer_decision
        print("Now we have",num_of_sticks,"sticks")
        type_computer(computer_decision,line)

def victory_player(computer_decision,player_name,line):
        num_of_sticks = len(line) - computer_decision
        print("Now we have",num_of_sticks,"sticks")
        line = type_computer(computer_decision,line) #12 long
        player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
        num_of_sticks = num_of_sticks - player_decision
        print("Now we have",num_of_sticks,"sticks")
        type_player(player_decision,line) 

def lose_computer(computer_decision,line):
        num_of_sticks = len(line) - computer_decision
        print("Now we have",num_of_sticks,"sticks")
        line = type_computer(computer_decision,line) 
        # player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
        # num_of_sticks = num_of_sticks - player_decision
        # print("Now we have",num_of_sticks,"sticks")
        # type_computer(player_decision,line)
        return line
   
def from_15_to_13_win(player_decision,computer_name,line):
    print("\n"+"This is the new line of the sticks")    #14 long
    line = type_player(player_decision,line)            #14 long
    computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
    if computer_decision == 1:                          #13 long
        type_computer(computer_decision,line)           #13 long
    return line #13 long

def from_15_to_13_lose(player_decision,line):               #good
    print("\n"+"This is the new line of the sticks")    #13 long
    line = type_player(player_decision,line) 
    return line                                         #13 long   

def from_13_to_9_win(player_name,computer_name,line):       #good
    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
    if player_decision == 1:
        victory_computer(player_decision,computer_name,line)
        return line #9 long
    if player_decision == 2:
        victory_computer(player_decision,computer_name,line)
        return line #9 long
    if player_decision == 3:
        victory_computer(player_decision,computer_name,line)
        return line #9 long

def from_13_to_9_lose(computer_name,line):  #not good
        #print("\n"+"This is the new line of the sticks")    #13 long
        #line = type_player(player_decision,line)            #13 long  
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        if computer_decision == 1:                          #12 long
            lose_computer(computer_decision,line)
            player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
            if player_decision == 1: 
                victory_player(player_decision,player_name,line)
            return line                                     #12 long 
        if computer_decision == 2:                          #11 long
            lose_computer(computer_decision,line)
            return line                                     #11 long
        if computer_decision == 3:                          #10 long
            lose_computer(computer_decision,line)
            return line                                     #10 long

def from_9_to_5_win(player_name,computer_name,line):        #good
    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
    if player_decision == 1:
        victory_computer(player_decision,computer_name,line)
        return line #8 long
    if player_decision == 2:
        victory_computer(player_decision,computer_name,line)
        return line #7 long
    if player_decision == 3:
        victory_computer(player_decision,computer_name,line)
        return line #6 long    
    
    
    # elif computer_decision == 2:
    #     num_of_sticks = len(line) - computer_decision
    #     print("Now we have",num_of_sticks,"sticks")
    #     line = type_player(computer_decision,line)
    #     return line #
    # elif computer_decision == 3:
    #     num_of_sticks = len(line) - computer_decision
    #     print("Now we have",num_of_sticks,"sticks")
    #     line = type_player(computer_decision,line)
    #     return line    
        
#def from_9_to_5(player_name,line):
    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
    if player_decision == 1:
        num_of_sticks = len(line) - player_decision
        print("Now we have",num_of_sticks,"sticks")
        line = type_player(player_decision,line)
        return line

def from_5_to_1_win(player_name,computer_name,line):        #good
    
    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
    if player_decision == 1:
        victory_computer(player_decision,computer_name,line)
        print(computer_name," W O N !!!")
        print("\n"+"******* END of GAME *******")
        return line
    if player_decision == 2:
        victory_computer(player_decision,computer_name,line)
        print(computer_name," W O N !!!")
        print("\n"+"******* END of GAME *******")
        return line
    if player_decision == 3:
        victory_computer(player_decision,computer_name,line)
        print(computer_name," W O N !!!")
        print("\n"+"******* END of GAME *******")
        return line

def from_15_to_9_win(player_decision,computer_name,line):
    print("\n"+"This is the new line of the sticks")
    line = type_player(player_decision,line)
    computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
    if computer_decision == 3:
        print("\n"+"This is the new line of the sticks")
        type_computer(computer_decision,line)
    return line #9 long

#######################################################################
def main():
         #השמות בסיסיות
    player_name   = "Dror"
    computer_name = "Moti"
    line = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]    
    
    openning(line)
    
    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
    if player_decision == 1:        #נותרו good 14
        line = from_15_to_13_win(player_decision,computer_name,line)
        line = from_13_to_9_win(player_name,computer_name,line)
        line = from_9_to_5_win(player_name,computer_name,line)
        from_5_to_1_win(player_name,computer_name,line)
    if player_decision == 2:        #נותרו 13
        line = from_15_to_13_lose(player_decision,line)#good נותרו 13
        line = from_13_to_9_lose(computer_name,line)
        
    if player_decision == 3:        #good נותרו 12
        line = from_15_to_9_win(player_decision,computer_name,line)
        line = from_9_to_5_win(player_name,computer_name,line)
        from_5_to_1_win(player_name,computer_name,line) 
        
if __name__ == "__main__":
        main() 
    
















#def from_15_to_13(player_name,computer_name):
#     line = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#     num_of_sticks = len(line)
#     print("\nHere we have",num_of_sticks,"sticks\n")
#     print(line)
#     player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
#     if player_decision == 1:
        
#     computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
#     num_of_sticks = num_of_sticks - computer_decision
#     print("Now we have",num_of_sticks,"sticks")
#     for i in range (1):
#         line.pop()
#     print(line)


     
    
  

# def from_15_to_9(computer_name):
#     line = [1,2,3,4,5,6,7,8,9,10,11,12]
#     num_of_sticks = len(line)
#     print("\nHere we have",num_of_sticks,"sticks\n")
#     print(line)
#     computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
#     num_of_sticks = num_of_sticks - computer_decision
#     print("Now we have",num_of_sticks,"sticks")
#     for i in range (3):
#         line.pop()
#     print(line)
# def start(player_name,computer_name):
#     player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
#     if player_decision == 1:
#         from_15_to_13(computer_name)
#         from_13_to_9(player_name,computer_name)
#         from_9_to_5(player_name,computer_name)
#         from_5_to_1(player_name,computer_name)  
            
#     elif player_decision == 3:
#         from_15_to_9(computer_name)
#         from_9_to_5(player_name,computer_name)
#         from_5_to_1(player_name,computer_name) 
 
# def main():
#     oppenning()
# #     #השמות בסיסיות
#     player_name   = "Dror"
#     computer_name = "Moti"
#     start(player_name,computer_name)
      

# if __name__ == "__main__":
#    main() 

