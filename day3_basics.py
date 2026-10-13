num=int(input("Enter the Number: "))

if(num%2 == 0):
    print("Even")
else:
    print("Odd")

marks=int(input("Enter marks between 0 and 100 :"))

if(marks>90):
    print("A")
elif(marks>75):
    print("B")
elif(marks>50):
    print("C")
elif(marks<50):
    print("Fail")
else:
    pass

num1=float(input("Enter number_1 : "))
num2=float(input("Enter number_2 : "))

op=input("choose a operator(+,-,*,/) : ")

if(op =='+'):
    print(num1+num2)
elif(op =='-'):
    print(num1-num2)
elif(op =='*'):
    print(num1*num2)
elif(op == "/"):
    print(num1/num2)
else:
    print("wrong operator choosen")
