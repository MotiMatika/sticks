import random as rd
def oppenning(line):
    print("\nS T I C K S")

    print("\n|  |  |  |  |  |  |  |  |  |  |")

    print("""\nYou have to remove,
        one,
        or two
        or three sticks.
        The player who takes the last stick - LOSES""")
    
    print("\n"+"This is the line of the sticks")
    print("\n",line)
    return line
def type_player(player_decision,line):#מכילה הוראות צמצום רשימה והדפסתה עבור השחקן
    for i in range (player_decision):
        line.pop()
    print(line) 
def from_14_to_13(player_decision,line):
    print("\n"+"This is the new line of the sticks")
    type_player(player_decision,line)
    num_of_sticks = 14
    
    return num_of_sticks,line 
def Rand_Com(num_of_sticks,computer_name,compuer_decision,line):
    num_of_sticks = num_of_sticks - computer_decision
    print("\n",computer_name, "decided to remove",computer_decision)
    print("Now we have",num_of_sticks,"sticks")
    type_computer(computer_decision,line)
def from_13_to_9(computer_name,nume_of_sticks,line):
    computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
    num_of_sticks = num_of_sticks - computer_decision
    print("Now we have",num_of_sticks,"sticks")
    for i in range (computer_decision):
        line.pop()
    print(line)



def main():
         #השמות בסיסיות
    player_name   = "Dror"
    computer_name = "Moti"
    line = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]    
    oppenning(line)
    
    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
    if player_decision == 1:       #נותרו 14
        from_14_to_13(player_decision,line)
        
        from_13_to_9(computer_name,line)
        
        #line=Rand_Com(13,computer_name,rd.randint(1,3),line)     

if __name__ == "__main__":
        main() 
    

# def from_13_to_9(computer_name):
#     computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
#     num_of_sticks = num_of_sticks - computer_decision
#     print("Now we have",num_of_sticks,"sticks")
#     type_computer
#     for i in range (1):
#         line.pop()
#     print(line)
#     line = [1,2,3,4,5,6,7,8,9,10,11,12,13]
#     num_of_sticks = len(line)
#     player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
#     if player_decision == 1:
#         num_of_sticks = num_of_sticks - player_decision
#         print("Now we have",num_of_sticks,"sticks")
#         for i in range (player_decision):
#             line.pop()
#         print(line)














    #   for i in range (player_decision):
    #     line.pop()
    # print(line)  
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
# # def main():
# #     oppenning()
# #     #השמות בסיסיות
#     player_name   = "Dror"
#     computer_name = "Moti"
#     from_15_to_13(player_name,computer_name)
#     #start(player_name,computer_name)
      


#def from_13_to_9(player_name,computer_name):
#     player_name   = "Dror"
#     computer_name = "Moti"
#     line = [1,2,3,4,5,6,7,8,9,10,11,12,13]
#     num_of_sticks = len(line)
#     player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
#     if player_decision == 1:
#         num_of_sticks = num_of_sticks - player_decision
#         print("Now we have",num_of_sticks,"sticks")
#         for i in range (player_decision):
#             line.pop()
#         print(line)

# def main():
#     oppenning()
#      #השמות בסיסיות
# player_name   = "Dror"
# computer_name = "Moti"
    #start(player_name,computer_name)
      

# if __name__ == "__main__":
#    main() 


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
#         print("Now we have",num_of_sticks,"sticks")
#         for i in range (1):
#             line.pop()
#         print(line)
    
# def from_9_to_5(player_name,computer_name):
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

