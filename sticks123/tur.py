#דוגמא כיצד ניתן לקצר קוד ע"י שימוש בלולאה פור
#לשירטוט אותו מבנה

#מבוא בסיסי
# import turtle               # allows us to use the turtles library
# tw = turtle.Screen()        # creates a graphics window 
# moti = turtle.Turtle()      # create a turtle named moti 
# moti.color("green")           
# moti.pensize(4)
# moti.speed(1) 

#גירסה ראשונה מסורבלת        
# moti.fd(120)
# moti.rt(90)
# moti.fd(120)
# moti.rt(90)
# moti.fd(120)
# moti.rt(90)
# moti.fd(120)

# #trig 1
# moti.rt(30)
# moti.fd(120)
# moti.rt(120)
# moti.fd(120)

# #trig 2
# moti.lt(30)
# moti.fd(120)
# moti.rt(120)
# moti.fd(120)

# # #trig 3
# moti.lt(30)
# moti.fd(120)
# moti.rt(120)
# moti.fd(120)

# # #trig 4
# moti.lt(30)
# moti.fd(120)
# moti.rt(120)
# moti.fd(120)


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# גירסה קצרה א
# def sq():
#     moti.fd(120)
#     for i in range (4):
#         moti.rt(90)
#         moti.fd(120)     
#     moti.rt(30)
# def triangle():
#     moti.fd(120)
#     moti.rt(120)
#     moti.fd(120)        
#     moti.lt(30) 
              
# def main(): 
       
#     sq()
#     for i in range(1,5):
#         triangle ()
        
# if __name__ == "__main__":
#     main() 
         
#turtle.mainloop()           # prevent the window from closing 



# גירסה קצרה ב
import turtle               # allows us to use the turtles library
tw = turtle.Screen()        # creates a graphics window 
moti = turtle.Turtle()      # create a turtle named moti 
moti.color("green")           
moti.pensize(4)
moti.speed(1) 

def sq():
    for i in range (3):
        moti.fd(120)
        moti.rt(90)
    moti.fd(120)         
def tri1():
    moti.rt(30)
    moti.fd(120)
    moti.rt(120)
    moti.fd(120)
def tri234():
    
    moti.lt(30)
    moti.fd(120)
    moti.rt(120)
    moti.fd(120)              

def main(): 
       
    sq()
    tri1()
    for i in range(3):
        tri234()
        
if __name__ == "__main__":
    main() 
         
turtle.mainloop()           # prevent the window from closing 