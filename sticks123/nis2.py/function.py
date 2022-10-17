import math

def mishvaa_ribuit(a,b,c):

    x_1 = (-b+(math.sqrt(b*b - 4*a*c)))/(2*a)
    x_2 = (-b-(math.sqrt(b*b - 4*a*c)))/(2*a)
    return x_1,x_2

print("The Roots are : ")
x_1,x_2=mishvaa_ribuit(1,0,-9)
# print(mishvaa_ribuit(1,0,-9))


print("x_1 = ",x_1)
print("x_2 = ",x_2)

"""
הדגמה להחלפת ערך בין שני משתנים
"""
p_1 = "d"
p_2 = "m"

current_player = input("who's turn? ")
if current_player == "m":
    next_player = "d"
else:
    next_player = "m"
    
print ("The current playe is: ", current_player)
print("The Next player is: ", next_player)
print("End of the turn")
temp_player = current_player
current_player = next_player
next_player = temp_player

print ("The current playe is: ", current_player)
print("The Next player is: ", next_player)


# def cube(x):
    
#     volume =int(math.pow(x,3))
#     return volume

# print("The Volume of cube is ",cube(10),"cm^3")