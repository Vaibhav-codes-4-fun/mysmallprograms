"""a= int(input("Enter number\n"))
print(factorial(a))
n=int(input("Enter a number"))
sum=0
order=len(str(n))
copy_n=n
while(n>0):
  digit=n%10
  sum+=digit**order
  n=n//10

if sum==copy_n:
        print("Armstrong Number")
else:
        print("Not an Armstrong Number") 
"""
def fact(number):
  if number<0:
    print("Enter valid number")
  if number==0 or number==1:
    return 1
  else:
    return number*fact(number-1)    
a = int(input("Enter number"))
print(fact(a))
