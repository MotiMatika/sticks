import math

def mishva_ribuit(a,b,c):

    x_1 = (-b+(math.sqrt(b*b - 4*a*c)))/(2*a)
    x_2 = (-b-(math.sqrt(b*b - 4*a*c)))/(2*a)
    return x_1,x_2

print("The Roots are : ")
print(mishva_ribuit(1,0,-9))


# def cube(x):
    
#     volume =int(math.pow(x,3))
#     return volume

# print("The Volume of cube is ",cube(10),"cm^3")