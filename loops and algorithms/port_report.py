#  port_repote.py check port between start and end port 
start_port=int(input("start port: "))
end_port=int(input("end port: "))
port_checked=0
for port in range(start_port,end_port+1):
    if 0<=port<=1023:
        print(f"{port}: system ")
    elif 1024<=port<=49151:
        print(f"{port}: user ")
    else : 
        print(f"{port}: dynamic")
        port_checked+=1
print(f"ports checked {port_checked}")# use the IANA ranges 
    

