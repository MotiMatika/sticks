import random as rd
#def from_13_to_rrrr(player_name,computer_name):
print("Now we have 13 sticks")
line = [1,2,3,4,5,6,7,8,9,10,11,12,13]
print(line)
num_of_sticks = rd(1,3)
print("you decided to remove",num_of_sticks)
num_of_sticks = 13-num_of_sticks
print("Now we have",num_of_sticks,"sticks")
    # for i in range (3):
    #     line.pop()
    # print(line)
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