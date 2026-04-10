import random as r
from datetime import datetime,timedelta
score=0
start_time=datetime.now()
end_time=(start_time + timedelta(seconds=5))#game run for 5seconds after start
print("----🎲 SMART DICE ROLLER 🎲----")
print("Rules 📝 \n1.Game run for 10 seconds.\n2.Dice would roll randomly each time you choose Y.\n3.When outcomes are 1 or 6 then playing time increase by +1sec.")
while datetime.now()<end_time:
    user=input("Do you want to roll dice (Y/N) ? : ")
    if user.lower()=="y":
        dice_roll=r.randint(1,6)
        print(f"{dice_roll} came!")
        if dice_roll==1 or dice_roll==6:#bonous 1seconds play for dice no. 1 or 6
            end_time=end_time + timedelta(seconds=1)
            score+=dice_roll
            print("+1sec 🕐\n")
        else:
            score+=dice_roll
    else:
        break
print("\n")
print(f"Total score : {score}\nTotal time taken in seconds : {(end_time-start_time).seconds}\nGame start time : {start_time.time()}\nGame end time : {end_time.time()}")