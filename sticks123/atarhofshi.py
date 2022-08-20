def oppenning():
    print("\nS T I C K S")

    print("\n|  |  |  |  |  |  |  |  |  |  |")

    print("""\nYou have to remove,
        one,
        or two
        or three sticks.
        The player who takes the last stick - LOSE""")

def from_15_to_13():
    player_name   = "Dror"
    computer_name = "Moti"
    num_of_sticks = 15
    print("\nHere we have",num_of_sticks,"sticks")
    print("\n")
    line = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    print(line)
    #ad kan 15
    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
    if player_decision == 1:
        num_of_sticks = num_of_sticks - 1
        print("Now we have",num_of_sticks,"sticks")
        del line[num_of_sticks]
        print(line)
        #ad kan 14
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        num_of_sticks = num_of_sticks - computer_decision
        print("Now we have",num_of_sticks,"sticks")
        del line[num_of_sticks]
        print(line)
        #ad kan 13
def from_13_to_9():
    player_name   = "Dror"
    computer_name = "Moti"
    num_of_sticks = 13
    line = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
    if player_decision == 1:
        num_of_sticks = num_of_sticks - 1
        print("Now we have",num_of_sticks,"sticks")
        del line[num_of_sticks]
        print(line)
        #ad kan 12
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
        #num_of_sticks 11
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
        #num_of_sticks 10
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        num_of_sticks = num_of_sticks - computer_decision
        print("Now we have",num_of_sticks,"sticks")
        for i in range (1):
            line.pop()
        print(line)
        
def from_9_to_5():
    player_name   = "Dror"
    computer_name = "Moti"
    line = [1,2,3,4,5,6,7,8,9]
    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
    num_of_sticks = 9
    if player_decision == 1:
        num_of_sticks = num_of_sticks - 1
        print("Now we have",num_of_sticks,"sticks")
        del line[num_of_sticks]
        print(line)
        #ad kan 8
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        num_of_sticks = num_of_sticks - computer_decision
        print("Now we have",num_of_sticks,"sticks")
        for i in range (3):
            line.pop()
        print(line)
        #ad kan 5 
    if player_decision == 2:
        num_of_sticks = num_of_sticks - 2
        print("Now we have",num_of_sticks,"sticks")
        for i in range (2):
            line.pop()
        print(line)
        #ad kan 7
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        num_of_sticks = num_of_sticks - computer_decision
        print("Now we have",num_of_sticks,"sticks")
        for i in range (2):
            line.pop()
        print(line)
        #ad kan 5
    if player_decision == 3:
        num_of_sticks = num_of_sticks - 3
        print("Now we have",num_of_sticks,"sticks")
        for i in range (3):
            line.pop()
        print(line)
        #ad kan 6
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        num_of_sticks = num_of_sticks - computer_decision
        print("Now we have",num_of_sticks,"stick")
        for i in range (1):
            line.pop()
        print(line)
        #ad kan 5
def from_5_to_1():
    player_name   = "Tomer"
    computer_name = "Moti"
    line = [1,2,3,4,5]
    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
    num_of_sticks = 5
    if player_decision == 1:
        num_of_sticks = num_of_sticks - 1
        print("Now we have",num_of_sticks,"sticks")
        del line[num_of_sticks]
        print(line)
        #num_of_sticks 4
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        num_of_sticks = num_of_sticks - computer_decision
        print("Now we have",num_of_sticks,"sticks")
        for i in range (3):
            line.pop()
        print(line)
        print(computer_name," W O N !!!")
    if player_decision == 2:
        num_of_sticks = num_of_sticks - 2
        print("Now we have",num_of_sticks,"sticks")
        for i in range (2):
            line.pop()
        print(line)
        #ad kan 3
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        num_of_sticks = num_of_sticks - computer_decision
        print("Now we have",num_of_sticks,"sticks")
        for i in range (2):
            line.pop()
        print(line)
        print(computer_name," W O N !!!")
    if player_decision == 3:
        num_of_sticks = num_of_sticks - 3
        print("Now we have",num_of_sticks,"sticks")
        for i in range (3):
            line.pop()
        print(line)
        #ad kan 2
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        num_of_sticks = num_of_sticks - computer_decision
        print("Now we have",num_of_sticks,"stick")
        for i in range (1):
            line.pop()
        print(line)
        print(computer_name," W O N !!!") 
                             
        
        
def main():

    oppenning()
    
    from_15_to_13()
    from_13_to_9()
    from_9_to_5()
    from_5_to_1()  

if __name__ == "__main__":
    main()
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# #the next fun from 13 to 9
# def thirteen():
#     player_name   = "Dror"
#     
#         
            
        







