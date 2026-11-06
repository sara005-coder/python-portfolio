#login_report.py ask thye username and the number of failed and count attempt of failed 
MAX_LOGIN_ATTEMPTAS=5
username=input("what is your name")
number_of_failed=int(input("what is the number "))
attempt_left=MAX_LOGIN_ATTEMPTAS-number_of_failed
print("="*30)
print("LOGIN REPORT")
print("="*30)
line1=f"user:\t{username} "
line2=f"failed : \t{number_of_failed}"
line3=f"attempt left :\t {attempt_left}"
print(line1)
print(line2)
print(line3)