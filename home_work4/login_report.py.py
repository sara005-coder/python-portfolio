MAX_LOGIN_ATTEMPTAS=5
username=input("what is your name")
number_of_failed=int(input("what is the number "))
print(username)
print(number_of_failed)
attempt_left=MAX_LOGIN_ATTEMPTAS-number_of_failed
print("="*30)
print("LOGIN REPORT")
print("="*30)
line1=f" user:\t{usrename} "
lin2=f"failed : {number_of_failed}"
line3=f"attempt left : {attempt_left}"