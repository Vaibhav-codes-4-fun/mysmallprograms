n1=float(input("Enter a number"))
n2=float(input("Enter another number"))
n=0
a=int(input("Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division, 5 for power,6 for quitting:"))
if(a==1):
        print("Additon of numbers is", n1+n2)
elif(a==2):
         print("Subtraction of numbers is",n1-n2)
elif(a==3):
         print("Multiplication of numbers is",n1*n2)
elif(a==4):
        print("Division of numbers is",n1/n2)
elif(a==5):
        print("n2 raised to n1 is",n1**n2)
elif(a==6):
        print("Thank you") 
