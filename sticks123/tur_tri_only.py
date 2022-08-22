#דוגמא כיצד ניתן לקצר קוד ע"י שימוש בלולאה פור
#לשירטוט אותו מבנה

#מבוא בסיסי
import turtle               # allows us to use the turtles library
tw = turtle.Screen()        # creates a graphics window 
moti = turtle.Turtle()      # create a turtle named moti 
moti.color("green")           
moti.pensize(4) 


def tri1():
    for i in range(2):
        moti.fd(120)
        moti.rt(120)
    moti.fd(120)
print(tri1())

              
def main():    
   for i in range(3):
       tri1() 
if __name__ == "__main__":
    main()      
turtle.mainloop()           # prevent the window from closing 