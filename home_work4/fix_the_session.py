#fix_the_session.py
#this programreport auser session time 
# username = input("Username: ")
#total_seconds = input("Session length in seconds: ")
#inutes = total_seconds / 60
#seconds = total_seconds % 60
#print("=" * 30)
#print("User: {username}")
#rint("Session: " + minutes + " min " + str(seconds) + " s")
#print("=" * 30)
username = input("enter the name of user :  ")
total_secound =int(input("session length in secound : "))
minute=total_secound//60
secound=total_secound % 60
print("="*30)
print(f"user : {username} ")
print("session : " +" minute  " +   "min" +   str(secound) +  " s")
print("="*30)


