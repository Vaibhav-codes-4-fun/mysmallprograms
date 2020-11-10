n= int(input("Enter number greater than 1"))
count=0

for i in range(1,n+1):
        if(n==2):
                print("Number is neither prime nor composite")
                break
        if(n%i==0):
                count=count+1
if(count>2):
        print("Number is not prime")
if(count==2):
        print("Number is prime")
