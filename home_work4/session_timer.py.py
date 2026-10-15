#write programs that read input and calculate and report 
session_length_in_secound=int(input("enter the session with secound "))#this session with secound and i convert it to integer becuase the input store the input like a string 
minute =session_length_in_secound//60# convert the session from secound to minute tharough //60
print(minute)
remaind_division=session_length_in_secound%60#remainfrom the secound 
print(remaind_division)
massege=f"{session_length_in_secound} secound will be a minute {minute} and the remain is {remaind_division}"# i use the f string to connect with the variable without use a + or and 
print(massege)
# 905 secound the output is 15 minute and 5 secound remained and 905 secound will be a minute 15 and the remain is 5
# 60 secound the out put is 1 minue and zero secound 60 secound will be a minute 1 and the remain is 0
# 59 secound is 1 minute and 59 remained 59 secound will be a minute 0 and the remain is 59
