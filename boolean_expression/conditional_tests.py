user= "analyst"
role="viewer"
failed=3
port=22
test1= user=="analyst"
test2=role=="viewer"
test3=failed==3
test4=port==22
print(test1,"\n",test2,"\n",test3,"\n",test4)
print(user=="analyst")
print(port>failed)
print(port>=failed)
print(role!="admine")
print(role=="viewer")
print(failed>port)
print(user!="analyst")
print(failed>=port)
print(role=="sara ")
print(port<=failed)


