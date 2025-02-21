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

#3
year=int(input("enter a year: "))
if (year%4==0 and year%100!=0) or year%400==0:
       print("leap year")
else:
       print("not leap year")
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
