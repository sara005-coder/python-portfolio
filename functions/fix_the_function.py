#fix_the_function 
#print_header()# the bug is call the function above the function it canot see it  is not define name error runtime


def print_header():
    """ disaplay the report header """
    print("="*30)
    print("LOGIN REPPORT")
    print("="*30)

print_header()

#fix_the_function2(lies12 to 20)
def lock_minutes(failed,minutes=15):
    """ return failed * minute if failed >=,else 0."""
    if failed >=3:
        total = failed*minutes 
    return 0

def login_line(username,failed):
    """ return one line of the report """
    minutes=lock_minutes(failed)
    return f"{username}:{ failed} failed , locked{minutes} min "
print(login_line(username="sara",failed=4))# user is not define runtime error 
login_line("omar",1)
