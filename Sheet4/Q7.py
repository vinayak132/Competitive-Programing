n=5
for i in range(1,n+1):
	if(i==1 or i==n):
		for j in range(1,n+1):
			print("*", end=" ")
		print()
	else:
		for j in range(1,3):
			print("*", end=" ")
		print()
