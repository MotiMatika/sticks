# print("hello Moti, how are you?")
# print("hello Moti, how are you?")
# print("hello Moti, how are you?")
# print("hello Moti, how are you?")
# print("hello Moti, how are you?")
# print("hello Moti, how are you?")
# print("hello Moti, how are you?")
# print("hello Moti, how are you?")
# print("hello Moti, how are you?")


# name1 = "Shahar"
# name2 = "Moti"
# HELLO_WORD = "hello "
# QUESTION = ", how are you?"

# for i in range(0,10):
#     print(HELLO_WORD + name1 + QUESTION)
#     for j in range(0,5):
#         print(HELLO_WORD + name2 + QUESTION)

def choice_1():
    print("Player chose 1 stick")
    
def choice_2():
    print("Player chose 2 sticks")
    
def choice_3():
    print("Player chose 3 sticks")  
   
   
   
def main():    
    player_decision = int(input("\n" + "Moti" + ",how many sticks do you want to remove ?" ))
        
    if player_decision == 1:
        choice_1()
        
    elif player_decision == 2:
        choice_2()
        
    elif player_decision == 3:
        choice_3()

if __name__ == "__main__":
    main()
