
def yair(y):
    y=y-2
    return y


def moti(num):  # מה הפונקציה מקבלת
    # m=m+4
    # return m
    
    # moti קורא לפונקציה יאיר
    # yair_result = yair(num)  
    # result = yair_result + 4
    # return result  # מה הפונקציה מחזירה
    
    return num + 4
    

def main():
    # print(moti(6)+yair(8))
    # print(moti(6))  # מה נותנים לפונקציה
    # moti_result = moti(6)
    # print(moti_result)
     
     # main קוראת לפונקציה yair ונותנת את הערך לפונקציה moti
    yair_result = yair(9)
    moti_result = moti(yair_result)
    print(moti_result)






main()