MAX_FAILED=5
KNOW_USER="analyst"
STORED_PASSOWRD="Blue#Faclon72"
username=input("username: ")
failed_attempt=int(input("failed attempt : "))
password=input("password: ")
if failed_attempt>MAX_FAILED:
    print("loked")
elif username!=KNOW_USER:
    print("unknownuser")
elif password!=STORED_PASSOWRD:
    print("wrong password ",MAX_FAILED-failed_attempt)
else : 
    print("access granteed ")
    