#1
a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
if (a>b)and(a>c):
    print("a is greater")
elif (b>a)and(b>c):
    print("b is greater")
else:
    print("c is greater")
#O(1)

#2
num=int(input("enter a number: "))
if (num>90) or (num==100):
    print("Grade A")
elif (num>80) or (num==89):
    print("Grade B")
elif (num>70) or (num==79):
    print("Grade C")
else:
    print("fail")
O(1)
#3
year=int(input("enter a year: "))
if (year%4==0 and year%100!=0) or year%400==0:
       print("leap year")
else:
       print("not leap year")
#O(1)
#4
char=str(input("Enter a Character:")).lower()
if char in "aeiou":
    print("It is Vowel")
elif char in "bcdfghjklmnpqrstvwxyz":
    print("It is Consonent")
else:
    print("Enter valid Characters")
#5
a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
if (a+b>c) and (b+c>a) and (a+c>b):
    print("valid traingle")
else:
    print("not valid")
#O(1)
#Check given number is Prime or not
n=int(input("enter a number"))
prime=True
if n==0 or n==1:
    print("either prime nor composite")
elif n>1:
   for i in range(2,n):
     if n%i==0:
        prime=False
        break
   if prime:
    print("it is a prime number")
   else:
    print("not prime")
#O(1)
#Factorial of a given number
n=int(input("enter a number:"))
i=1
while n>0:
    i=i*n
    n=n-1
print(i)
O(1)

#Number divisible by 3 and 5
n=int(input("enter a number:"))
if n==0:
    print("zero error")
for i in range(1,n+1):
    if i%3==0 or i%5==0:
        print(i)
O(1)
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
#O(n)
    num=int(input("enter a number: "))
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
#O(1)
n=int(input("enter a number: "))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if n==sum:
    print("perfect number")
else:
    print("not perfect number")
#O(1)
#GCD
a=int(input("enter a number:"))
b=int(input("enter a number:"))
while b:
    temp=a%b
    a=b
    b=temp
gcd=a
print("gcd of a number:",gcd)
#O(n)

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
print("LCM of two numbers is:", LCM)
#O(1)
