num = 5
for i in range(num):
    for j in range(num):
        if(j == 0 or j == num - 1):
            print("*", end=" ")
        else:
            print("_", end=" ")
    print()
