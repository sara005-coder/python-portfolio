#security_toolkit.py
MIN_LENGTH=8
def border(width):
    """ prints + then width+2 dashes then + """
    print("+" + (width+2)*"-" + "+")
def show_box(text):
    """ print text inside a box border """
    border(len(text))
    print("| "+text+ "| ")
def show_menu():
    show_box("SECURITY TOOLKIT ")
    print("1.check port")
    print("2.check password")
    print("3.checck pin")
    print("q.quit")

def port_range(port):
    if port<0 or port>65535:# the number from IANA
        return "invalid "
    elif  port<=1023:
            return "system"
    elif port<=4915:
            return "user"
    else : return "dynamic "
     
def check_port():
     """ ask port then show port ,range in box """
port= int(input("port?"))
rng=port_range(port)
show_box(f"port {port} : {rng} ")

def passowrd_proplem(password,username):
    """ two proplem 1.too short at least (8)2.same username"""
    if len(password)<8:
         return " too short "
    if password==username:
         return " same a user name "
    

def check_password():
     """ ask user name and passsword """
     username=input("username : ")
     password=input("password : ")
     proplem=passowrd_proplem(username,password)
     if proplem :
          print(f" rejected : {proplem }")
     else:
          print(f"accepted")

def days_to_guess(digits,per_second):
     """ calculates whole to try evre pin """
     return 10**digits//per_second //86400
def check_pin():
     """ ask pin digits and guess per second show digits days """
     digits=int(input("pin duguts: "))
     per_second=int(input("guesses per second : "))
     days=days_to_guess(digits,per_second)
     show_box(f"{digits} digits : {days} days ")

show_menu()
checks_done=0
while (True):
          choice=input("choice 1,2,3,4")
          if choice=='1':
               check_port()
               checks_done+=1
          elif choice=='2' :
               check_password()
               checks_done+=1
          elif choice=='3':
               check_pin()
               checks_done+=1
          elif choice=='q':
               show_box(f" check done: {checks_done}")
               break
          else:
               print("unknown choice")

               
               
