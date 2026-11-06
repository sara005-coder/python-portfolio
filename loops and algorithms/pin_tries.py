# pin_tries.py check pin tries  as long as tries less thsn MAX TRIES run the code  increase one to tries in all input 
MAX_TRIES=3
CORRECT_PIN="2580"
tries=0
# as long as tries less thsn MAX TRIES run the code 
while tries<MAX_TRIES:
    pin=input("pin: ")
    # increase one to tries in all input 
    tries+=1
    if pin==CORRECT_PIN:
        print("Access granted")
        break
    else:
        print(f"wrong PIN .tries left: {MAX_TRIES-tries}")
    if tries==MAX_TRIES:
        print("card blocked")
