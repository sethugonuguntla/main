num=int(input("enter a number: "))
while True:
    if num==1:
        num=int(input("enter a number: "))
        print(num**2,"square:")
    elif num==2:
        num=int(input("enter a number: "))
        print(num**3,"cube:")
    elif num==3:
        break
    else:
        print("invalid input")
    num=int(input("enter a number: "))
  palindrome
num=int(input("enter a number: "))
temp=num
rev=0
while temp>0:
    rem=temp%10
    rev=rev*10+rem
    temp=temp//10
if num==rev:
    print("palindrome")
else:
    print("not palindrome")
#perfect number
n=int(input("enter a number: "))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if n==sum:
    print("perfect number")
else:
    print("not perfect number")
#GCD
a=int(input("enter a number:"))
b=int(input("enter a number:"))
while b:
    temp=a%b
    a=b
    b=temp
gcd=a
print("gcd of a number:",gcd)

# LCM 
x = int(input("Enter the first number:"))
y = int(input("Enter the second number"))
if x > y:
    big = x
else:
    big = y
while True:
    if (big % x == 0) and (big % y == 0):
        LCM = big
        break
    big = big + 1
print("LCM of two numbers is:", LCM)
