#access_chesk.py compare between the mfa_of and failed _attempt if fales or true 

MAX_FAILED=5
role=input("enter the role ")
mfa_input=input("enter your choice ")
failed_attempt=int(input("enter the number of failed "))
mfa_ok=(mfa_input=="yes")
is_privileged=(role=="admin" or role=="root")
can_log_in=(mfa_ok and failed_attempt<MAX_FAILED)
print(f"MFA_OK:{mfa_ok}")
print(f"privileged role : {is_privileged}")
print(f"can log in {can_log_in}")
