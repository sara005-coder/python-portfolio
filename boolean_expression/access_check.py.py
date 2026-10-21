MAX_FAILED=5
role=input("enter the role ")
MFA=input("enter your choice ")
failed_attempt=int(input("enter the number of failed "))
mfa_ok=(role=="adminr" or role=="root")
can_log_in=(mfa_ok and failed_attempt<MAX_FAILED)
print(f"{mfa_ok} \n {can_log_in }")
