import random as r 
from datetime import datetime,timedelta
choice=1
otp=""
while choice==1:
    for i in range(6):#Generate 6-digit Random otp
        otp+=str(r.randint(0,9))
    start_time=datetime.now()
    valid_time=start_time+timedelta(seconds=30)
    print(f"Your OTP is : {otp} . Submmit this otp under {(valid_time-start_time).seconds}sec.\nTime generated : {(start_time).time()}\n\n")
    try:
        user_input=int(input("Enter the 6-digit OTP :  "))
        print("\n")
        print("-"*25)
        if str(user_input)==otp and datetime.now()<valid_time:#valid for only 30 sec
            print("Authentication successfull ✅")
            print("-"*25)
            break
        elif str(user_input)!=otp and datetime.now()<valid_time:
            print("Invalid OTP ⚠️")
            print("-"*25)
            choice=int(input("Press 1 : send OTP\nPress 2 : Exit "))
            if choice==1:
                otp=""#reset the otp
            elif choice==2:
                break
            else:
                print("Invalid Input ")
                break
            print("\n")
        elif str(user_input)==otp and datetime.now()>valid_time:
            print("Session Expired ⏳")
            print("-"*25)
            choice=int(input("Press 1 : send OTP\nPress 2 : Exit "))
            if choice==1:
                otp=""#reset the otp
            elif choice==2:
                break
            else:
                print("Invalid Input ")
                break
            print("\n")
        elif str(user_input)!=otp and datetime.now()>valid_time:
            print("Authentication Failed 😓")
            print("-"*25)
            choice=int(input("Press 1 : send OTP\nPress 2 : Exit "))
            if choice==1:
                otp=""#reset the otp
            elif choice==2:
                break
            else:
                print("Invalid Input ")
                break
            print("\n")
    except ValueError:
        print("Invalid User Input ! ")
        choice=int(input("Press 1 : send OTP\nPress 2 : Exit "))
        if choice==1:
            otp=""#reset the otp
        elif choice==2:
            break
        else:
            print("Invalid Input ")
            break
        
        print("\n")
    


