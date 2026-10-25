score=0
failed_attempt=int(input("failed attempts in the last hours"))
login_hours=int(input("login hours :"))
new_device=input("yes or no :")

if failed_attempt>3:
    score+=40
if login_hours<6:
    score+=30
if new_device=="yes":
    score+=30
if score==0:
    print("risk score :(low)")
elif score ==40:
    print("risk score: (medium) ")
elif score==60:
    print("risk score : (medium )")
elif score==70:
    print("risk score : (high ) ")
elif score ==100:
    print("risk score :(high)  ")
