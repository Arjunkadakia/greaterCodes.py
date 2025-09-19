num1=int(input("enter first number"))
num2=int(input("enter second number"))
num3=int(input("enter third number"))
num4=int(input("enter fourth number"))
num5=int(input("enter fifth number"))
print("the numbers are",num1,num2,num3,num4,num5)
if num1>num2 and num1>num3 and num1>num4 and num1>num5:
    print(num1,"is the greatest")
elif num2>num3 and num2>num4 and num2>num5:
    print(num2,"is the greatest")
elif num3>num4 and num3>num5:
    print(num3,"is the greatest")
elif num4>num5:
    print(num4,"is the greatest")
else:
    print(num5,"is the greatest")
if num1<num2 and num1<num3 and num1<num4 and num1<num5:
     print(num1,"is the least")
elif num2<num3 and num2<num4 and num2<num5:
    print(num2,"is the least")
elif num3<num4 and num3<num5:
    print(num3,"is the least")
elif num4<num5:
    print(num4,"is the least")
else:
    print(num5,"is the least")
sum=num1+num2+num3+num4+num5
# print(sum)
if sum%2==0:
    print("the average is",sum/2)
else:
    print("the average is",(sum/2)+0.5)
