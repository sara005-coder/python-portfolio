
# fix_the_policy.py
# Check a new password against an example policy and classify its length.
MIN_LENGTH = 12

username = input("Username: ")
password = input("New password: ")

if len(password) < MIN_LENGTH: # forget a colone : syntax errors 
    print("- Too short.")
elif password == username:
    print("- Same as the username.")

if  len(password) >= 16:# order of statement semantic error 
    strength = "long"
elif len(password) >= MIN_LENGTH:
    strength = "acceptable"
else:
    strength = "short"
    print(f"Length: {len(password)} ({strength})")# forget a )semantic error 