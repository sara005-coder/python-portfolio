#lock_tools.py check  account if will locked or not 
def is_locked(failed,max_tries=3):

    if (failed>=max_tries):
        """ return true if failed bigger than max_tries or more else return false """
        return True
    else:
        return False 
def tries_left(failed,max_tries=3):
    """ return 0 if the account is locked based on is_locked function else return result of max_tries-failed """
    if is_locked(failed,max_tries=3):
        return 0
    else:
        return  max_tries-failed
def status(failed):
    """ return locked or active n tries left """
    if is_locked(failed,max_tries=3):
        return "locked"
    else:
        return f"active ({tries_left(failed)} tries left) "

print(is_locked(2))
print(is_locked(3))
print(is_locked(3,5))
print(tries_left(1))
print(tries_left(7))
print(status(1))
print(status(4))