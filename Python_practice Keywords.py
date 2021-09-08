print("Hi, I am Anji")
Num1=25
Num2=65
print(Num1+Num2)

####################################################

#python is case sensitive language
Anji_64=67.5
anji_64=2.5
print(Anji_64+anji_64)

#####################################################

number=int(input("Enter any number:"))
sum=0
for i in range(1,number):
    sum=sum+i
print(sum+number)

######################################################

Number=int(input("Enter the number:"))
if Number==0:
    print("You entered Zero")
elif Number%2==0:
    print("Your given number is Even") 
else:
    print("Your given number is Odd")
    
