num=4
for i in range(1,num+1):
    print("*",end=" ")
    for j in range(num+1-i):
        print("_",end=" ")
    print("*",end="")
    print()