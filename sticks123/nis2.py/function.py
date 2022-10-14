import math

def mishvaa_ribuit(a,b,c):

    x_1 = (-b+(math.sqrt(b*b - 4*a*c)))/(2*a)
    x_2 = (-b-(math.sqrt(b*b - 4*a*c)))/(2*a)
    return x_1,x_2

print("The Roots are : ")
print(mishvaa_ribuit(1,0,-9))


# print("x_1 = ",x_1)
# print("x_2 = ",x_2)
# def cube(x):
    
#     volume =int(math.pow(x,3))
#     return volume

# print("The Volume of cube is ",cube(10),"cm^3")