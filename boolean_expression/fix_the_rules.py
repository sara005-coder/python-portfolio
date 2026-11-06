#fix_the_rules.py
#this program checks a connection against three rules
role = input("Role: ") 
#runtime error becouse this is integer and input print string 
port = input("Port: ")
#semantic error = isteadof  == 
is_admin = role == "admin"
#syntax error =< is invalid 
is_system_port = port <= 1023
is_web_port = port == 80 or 443# semantic error port=80 or port==443
print(f"Admin: {is_admin}")
print(f"System port: {is_system_port}")
print(f"Web port: {is_web_port}")
