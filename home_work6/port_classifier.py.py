port=int(input("port: "))
if 0>port or port >65535:
    print("incaild port: use a number from 0 to 65535")
if 0<=port<=65535: 
    if 0<=port<=1023:
        print("range: system ")
    elif 1024<port<49151:
        print("range: user ")
    else :
        print("dynamic or private ")
if port == 22:
    print(" service : ssh")
if port==80:
    print(" service : http ")
if port==443:
    print("service: https ")

    
    

