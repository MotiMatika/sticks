def oppenning():
    print("\nS T I C K S")

    print("\n|  |  |  |  |  |  |  |  |  |  |")

    print("""\nYou have to remove,
        one,
        or two
        or three sticks.
        The player who takes the last stick - LOSES""")
def from_15_to_13(player_name,computer_name,num_of_sticks,line):#הפונקציה מקבלת מהמיין את המשתנים
    print("\nHere we have",num_of_sticks,"sticks\n")
    print(line)
    # player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
    # if player_decision == 1:
    num_of_sticks = num_of_sticks - 1
    print("Now we have",num_of_sticks,"sticks")
    del line[num_of_sticks]
    print(line)
    computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
    num_of_sticks = num_of_sticks - computer_decision
    print("Now we have",num_of_sticks,"sticks")
    del line[num_of_sticks]
    print(line)
    return line
def from_13_to_9(player_name,computer_name,num_of_sticks,line):
    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
    if player_decision == 1:
        num_of_sticks = num_of_sticks - 1
        print("Now we have",num_of_sticks,"sticks")
        del line[num_of_sticks]
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
        print("Now we have",num_of_sticks,"sticks")
        for i in range (1):
            line.pop()
        print(line)
    return line
def from_9_to_5(player_name,computer_name,num_of_sticks,line):
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
    return line
def from_5_to_1(player_name,computer_name,num_of_sticks,line):
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
        
    return line    

def start(player_name,computer_name,num_of_sticks,line):
    player_decision = int(input("\n" + player_name + ",how many sticks do you want to remove ? " ))
    if player_decision == 1:
        from_15_to_13(player_name,computer_name,num_of_sticks,line)
        from_13_to_9(player_name,computer_name,num_of_sticks,line)
        from_9_to_5(player_name,computer_name,num_of_sticks,line)
        from_5_to_1(player_name,computer_name,num_of_sticks,line)  
              
    elif player_decision == 3: 
        num_of_sticks = num_of_sticks - player_decision
        for i in range (3):
            line.pop()
        print("Now we have",num_of_sticks,"sticks")
        print(line) #ad kan 12
        computer_decision = int(input("\n" + computer_name + ",how many sticks do you want to remove ? " ))
        num_of_sticks = num_of_sticks - computer_decision
        for i in range (3):
                line.pop()
        print("Now we have",num_of_sticks,"sticks")
        print(line) #ad kan 9
        from_9_to_5(player_name,computer_name,num_of_sticks,line)
        from_5_to_1(player_name,computer_name,num_of_sticks,line)   






def main():
    oppenning()
    #השמות בסיסיות
    player_name   = "Dror"
    computer_name = "Moti"
    line = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    num_of_sticks = len(line)
    start(player_name,computer_name,num_of_sticks,line)
    line = from_15_to_13(player_name,computer_name,num_of_sticks,line)#הפונקציה מתעדכנת ברשימה
    num_of_sticks = len(line) #המשתנה מתעדכן באורך הרשימה החדשה
    
    line = from_13_to_9(player_name,computer_name,num_of_sticks,line)
    num_of_sticks = len (line)
    
    line = from_9_to_5(player_name,computer_name,num_of_sticks,line)
    
    num_of_sticks = len(line)
    from_5_to_1(player_name,computer_name,num_of_sticks,line)  

if __name__ == "__main__":
   main()    