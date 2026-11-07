#password_check.py check the password if such as username reject it 
def long_enough(password,minimum=8):
    """ return true if long of password was bigger than or equal 8 else false """
    if len(password)>=minimum:
        return True
    else:
        return False
def differs_from_username(password,username):
    """ return true if password not equal username else return false """
    if password!=username:
        return True
    else:
        return False 
def password_ok(password,username):
    """ check the first function and second function if return true rturn true else false and print reject """
    if long_enough(password,minimum=8) and differs_from_username(password,username):
        return True 
    else:
        return False

username=input("username: ")
password=input("password ")
if password_ok(password,username):
    print("password accept")
else:
    print("password reject ")
