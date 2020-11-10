import sys
import math
def calculator():
        print("\nSelect operation -\n\t1.Add\n\t2.Subtract\n\t3.Multiply\n\t4.Divide\n\t5.Sin\n\t6.Cos\n\t7.Tan\n")   
        option= int(input("Enter your choice: ")) 
        if option == 1:
                n1 = float(input("\nEnter first number: ")) 
                n2 = float(input("Enter second number: ")) 
                print(n1, "+", n2, "=",n1+n2) 
        elif option == 2:
                n1 = float(input("\nEnter first number: ")) 
                n2 = float(input("Enter second number: ")) 
                print(n1, "-", n2, "=",n1-n2) 
        elif option == 3:
                n1 = float(input("\nEnter first number: ")) 
                n2 = float(input("Enter second number: ")) 
                print(n1, "*", n2, "=",n1*n2) 
        elif (option == 4):
                n1 = float(input("\nEnter first number: ")) 
                n2 = float(input("Enter second number: ")) 
                if(n2==0):
                        print("\nNot possible coz denominator is 0.");
                else:
                        print(n1, "/", n2, "=",n1/n2)
        elif (option == 5):
                num=float(input("Enter a number (in degree) : "));
                print("\nSin(",num,")=",math.sin(math.radians(num)));
        elif option == 6:
                num=float(input("Enter a number (in degree) : "));
                print("\nCos(",num,")=",math.cos(math.radians(num)));
        elif option == 7:
                num=float(input("Enter a number (in degree) : "));
                print("\nTan(",num,")=",math.tan(math.radians(num)));
        else: 
            print("Invalid option !!!!!") 
def reverse(num):
    a=num;
    rev=0;
    while(num!=0):
        rem=num%10;
        rev=rev*10+rem;
        num=num//10;
    print("Reverse of",a,"is :", rev);
def is_prime(num):
    count=0;
    if(num==0 or num==1):
            return 0;
    elif(num==2):
            return 1;
    elif(num>2):
        for i in range(2,num):
           if (num % i) == 0:
                   return 0;
        return 1;
def month_name(num):
    count=0;
    List1=['January','February','March','April','May','June','July','August','September','October','November','December'];
    for i in range (1,13):
        if(i==num):
            print(List1[i-1])
    if(num>12):
        print("Month number exists b/w 1-12 ONLYYY!!!!");
def sorted():
        List1=List2=[];
        flag=0;
        print("Enter 3 numbers:");
        for i in range(0,3):
                n=int(input());
                List1.append(n);
        print("Entered numbers: ",List1);
        if (List1[0]<=List1[1]<=List1[2] or List1[0]>=List1[1]>=List1[2]):
                return True;
        else:
                return False;
while(1):
        print("\n\n1.Calculator using Functions(7 Operations).\n2.Reverse of given integer number using function.\n3.Function is_prime() that returns 1 if the argument passed to it as a prime number and 0 otherwise.\n4.Function that accepts an integer between 1 to 12 to represent the month number and displays the corresponding month of the year\n5.Function that accepts three integers and returns True if they are sorted and false if they are not sorted.\n6.Exit\n");
        option=int(input("Enter option:"));
        if(option==1):
                calculator();
        elif(option==2):
                num=int(input("\nEnter an +ve integer : "));
                if(num<0):
                        print("Enter a +ve number");
                else:
                        reverse(num);
        elif(option==3):
                num=int(input("Enter a number: "));
                if(is_prime(num)):
                        print(num,"is a Prime number");
                else:
                        if(num==0 or num==1):
                                print(num,"is neither prime nor composite.");
                        else:
                                print(num,"is a Composite number");
        elif(option==4):
                num=int(input("Enter a number b/w 1-12: \n"));
                month_name(num);
        elif(option==5):
                if((sorted())):
                        print("\nSorted");
                else:
                        print("\nNot sorted");
        elif(option==6):
                sys.exit("You have exited")
        else:
                print("Enter a CORRECT OPTION !!) ");
