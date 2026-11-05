#fix_the_record.py
#this program prints a short record about netowrk device 
device_name="edge-router"
# the mistake here is begin the variable with number syntax error the correct is backup
backup_ip="192.0.2.1"
# the mistake is use reversed word (class) syntax error 
device_type ="router "
# twenty two not integer runtime error 
port=int("22")
# the variable is not define mistake with name runtime 
print("device:",device_name)#
print("backup ip ",backup_ip)
print("type: ", device_type)
print("port:",port )
# python repport the syntax error first because it checks 
#runtime error only appeare later while the program is running 