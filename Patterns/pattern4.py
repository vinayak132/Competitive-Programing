num = 5
for i in range(1,num+1):
    odd=1
    for j in range(i):
        if (j%2==0):
            print(odd,end=" ")
            odd += 2
        else:
            print("*", end=" ")
    print()
