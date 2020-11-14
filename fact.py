#Take input
num = int(input("Enter a number: "))
factorial=1


#check if number is positive, negative or zero

if num < 0:
	print("negative")
elif num == 0:
	print("Fact(0)=1")
else:
	for i in range(1,num+1):
		factorial = factorial*i
	print("Fact(",num,")=",factorial,sep="")

