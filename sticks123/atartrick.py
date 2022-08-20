
#the next fun from 13 to 9
def thirteen():
    player_name   = "Dror"
    computer_name = "Moti"
    line = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
    num_of_sticks = 13
    if player_decision == 1:
        num_of_sticks = num_of_sticks - 1
        print("Now we have",num_of_sticks,"sticks")
        del line[num_of_sticks]
        print(line)
        #num_of_sticks 12
        print(computer_name,"is removing 3 sticks")
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
        print(computer_name,"is removing 2 sticks")
        for i in range (2):
            line.pop()
        print(line)
    if player_decision == 3:
        num_of_sticks = num_of_sticks - 1
        print("Now we have",num_of_sticks,"sticks")
        for i in range (3):
            line.pop()
        print(line)
        #num_of_sticks 9
        print(computer_name,"is removing 1 stick")
        for i in range (1):
            line.pop()
        print(line)    
        #num_of_sticks 9
        
        
#the next fun from 9 to 5
        
def nine():
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
        #num_of_sticks 8
        print(computer_name,"is removing 3 sticks")
        for i in range (3):
            line.pop()
        print(line)
            #num_of_sticks 5
    #the next fun from 5 to 1 
def five():
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
        print(computer_name,"is removing 3 sticks")
        num_of_sticks = num_of_sticks - 3
        for i in range (3):
            line.pop()
        print(line)
        print(computer_name," W O N !!!")
            
        






def main():
    print("\nS T I C K S")

    print("\n|  |  |  |  |  |  |  |  |  |  |")

    print("""\nYou have to remove,
        one,
        or two
        or three sticks.
        The player who takes the last stick - LOSE""")

    player_name   = "Tomer"
    computer_name = "Moti"
    num_of_sticks = 15
    print("\nHere we have",num_of_sticks,"sticks")
    print("\n")
    line = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    print(line)


    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
    if player_decision == 1:
        num_of_sticks = num_of_sticks - 1
        #num_of_sticks 14
        print("Now we have",num_of_sticks,"sticks")
        del line[num_of_sticks]
        print(line)
        print(computer_name,"is removing one stick")
        num_of_sticks = num_of_sticks - 1
        del line[num_of_sticks]
        print(line)
    
        #num_of_sticks 13
        thirteen()
        nine()
        five()

if __name__ == "__main__":
    main()
            
            
        













