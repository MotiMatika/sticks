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
    
def type_player(player_decision,line):#מכילה הוראות צמצום רשימה והדפסתה
    for i in range (player_decision):
        line.pop()
    print(line)
    return line 

def type_computer(computer_decision,line):#מכילה הוראות צמצום רשימה והדפסתה
    for i in range (computer_decision):
        line.pop()
    print(line)
    return line 
   
def from_15_to_13(player_decision,computer_name,line):
    print("\n"+"This is the new line of the sticks")
    line = type_player(player_decision,line)
    computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
    if computer_decision == 1:
        type_computer(computer_decision,line)
    return line #13 long

#def Rand_Com(num_of_sticks,computer_name,computer_decision,line):
    num_of_sticks = num_of_sticks - computer_decision
    print("\n",computer_name, "decided to remove",computer_decision)
    print("Now we have",num_of_sticks,"sticks")
    type_computer(computer_decision,line)

<<<<<<< HEAD:sticks123/fresh.py
def from_13_to_9(computer_name,line):
    computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
    num_of_sticks = len(line) - computer_decision
    print("Now we have",num_of_sticks,"sticks")
    line = type_player(computer_decision,line)
    return line
=======
def from_13_to_9(player_name,computer_name,line):
    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
    if player_decision == 1:
        num_of_sticks = len(line) - player_decision
        print("Now we have",num_of_sticks,"sticks")
        line = type_player(player_decision,line) #12 long
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        num_of_sticks = num_of_sticks - computer_decision
        print("Now we have",num_of_sticks,"sticks")
        type_computer(computer_decision,line)
        return line #9 long
    if player_decision == 2:
        num_of_sticks = len(line) - player_decision
        print("Now we have",num_of_sticks,"sticks")
        line = type_player(player_decision,line) #11 long
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        num_of_sticks = num_of_sticks - computer_decision
        print("Now we have",num_of_sticks,"sticks")
        type_computer(computer_decision,line)
        return line #9 long
    if player_decision == 3:
        num_of_sticks = len(line) - player_decision
        print("Now we have",num_of_sticks,"sticks")
        line = type_player(player_decision,line) #10 long
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        num_of_sticks = num_of_sticks - computer_decision
        print("Now we have",num_of_sticks,"sticks")
        type_computer(computer_decision,line)
        return line #9 long
    
    
    
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
>>>>>>> 3d816a022c364ea149d23533af50048a7bab21db:sticks123/bliDror2908.py

def main():
         #השמות בסיסיות
    player_name   = "Dror"
    computer_name = "Moti"
    line = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]    
    
    openning(line)
    
    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
    if player_decision == 1:       #נותרו 14
        line = from_15_to_13(player_decision,computer_name,line)
        line = from_13_to_9(player_name,computer_name,line)
        #line = from_9_to_5(player_name,line)
if __name__ == "__main__":
        main() 
    

#def from_9_to_5(player_name,computer_name):
#     
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
#         print("Now we have",num_of_sticks,"sticks")
#         for i in range (3):
#             line.pop()
#         print(line)
#     if player_decision == 2:
#         num_of_sticks = num_of_sticks - 2
#         print("Now we have",num_of_sticks,"sticks")
#         for i in range (2):
#             line.pop()
#         print(line)
#         computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
#         num_of_sticks = num_of_sticks - computer_decision
#         print("Now we have",num_of_sticks,"sticks")
#         for i in range (2):
#             line.pop()
#         print(line)
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


     
#def from_9_to_5(player_name,computer_name):
#     line = [1,2,3,4,5,6,7,8,9]
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
#         print("Now we have",num_of_sticks,"sticks")
#         for i in range (3):
#             line.pop()
#         print(line)
#     if player_decision == 2:
#         num_of_sticks = num_of_sticks - 2
#         print("Now we have",num_of_sticks,"sticks")
#         for i in range (2):
#             line.pop()
#         print(line)
#         computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
#         num_of_sticks = num_of_sticks - computer_decision
#         print("Now we have",num_of_sticks,"sticks")
#         for i in range (2):
#             line.pop()
#         print(line)
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

