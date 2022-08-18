#דוגמא כיצד ניתן לקצר קוד ע"י שימוש בלולאה פור
#לשירטוט אותו מבנה

#מבוא בסיסי
import turtle               # allows us to use the turtles library
tw = turtle.Screen()        # creates a graphics window 
moti = turtle.Turtle()      # create a turtle named moti 
moti.color("green")           
moti.pensize(4) 

#גירסה ראשונה מסורבלת        
moti.fd(120)
moti.rt(90)
moti.fd(120)
moti.rt(90)
moti.fd(120)
moti.rt(90)
moti.fd(120)
#trig 1
moti.rt(30)
moti.fd(120)
moti.rt(120)
moti.fd(120)
moti.rt(120)
moti.fd(120)
#trig 2
moti.lt(30)
moti.fd(120)
moti.lt(120)
moti.fd(120)
moti.lt(120)
moti.fd(120)

moti.rt(90)
moti.fd(120)

#trig 3
moti.rt(30)
moti.fd(120)
moti.rt(120)
moti.fd(120)
moti.rt(120)
moti.fd(120)

moti.rt(180)
moti.fd(120)

#trig 4
moti.rt(30)
moti.fd(120)
moti.rt(120)
moti.fd(120)
moti.rt(120)
moti.fd(120)


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#גירסה קצרה
# def sq():
#     moti.fd(120)
#     i=0
#     for i in range (1,4):
#         moti.rt(90)
#         moti.fd(120)
#         i=i+1        
#     moti.rt(30)
# def tri1():
#     moti.fd(120)
#     moti.rt(120)
#     moti.fd(120)        
#     moti.lt(30)               
# def main():    
#     sq()
#     for i in range(1,5):
#         tri1()
# if __name__ == "__main__":
#     main()      
turtle.mainloop()           # prevent the window from closing 