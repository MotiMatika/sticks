#מבוא בסיסי
import turtle               # allows us to use the turtles library
tw = turtle.Screen()        # creates a graphics window 
moti = turtle.Turtle()      # create a turtle named moti 
moti.color("green")           
moti.pensize(4)

def sq1():
    moti.fd(120)
    for i in range (3):
        moti.rt(90)
        moti.fd(120)
def sq2():
    moti.rt(90)
    moti.fd(60)
    moti.rt(135)
    for i in range(3):
        moti.fd(84.85281374)
        moti.lt(90)
    moti.fd(84.85281374)
def sq3():
    moti.lt(90)
    moti.fd(42.42640687)
    moti.lt(45)
    for i in range(3):
        moti.fd(60)
        moti.lt(90)
    moti.fd(60)    
        
def main():
        
    sq1()
    sq2()
    sq3()

if __name__ == "__main__":
    
    main()      
turtle.mainloop()   