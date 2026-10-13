num=int(input("Enter a number : "))

for i in range(1,11):
    print(num,'X',i,'=',num*i)

pass_value = input("Enter password : ")

flag=1
while (flag == 1):
    pass_key=input("Enter correct password : ")
    if(pass_value == pass_key):
        print("Correct password")
        flag=0
    else:
        print("ReEnter password")


list=[1,2,3,4,5]

sum=0
high=list[0]
low=list[0]
for i in range(len(list)):
    sum=sum+list[i]
    if(high<list[i]):
        high=list[i]

    if(low>list[i]):
        low=list[i]

print("Sum of elements :",sum)
print("Highest Number:",high)
print("Lowest Number:",low)

