num=int(input("Enter a number: "))
sum=0
if(num <= 0):
    print("Please enter a positive number")
else:
    for i in range(1, num + 1):
        sum=sum+i
    print(sum)
