num=int(input("Enter the Number:"))
org_num=num
d=0
while(num>0):
    d=d+1
    num=num//10
num=org_num
sum=0
while(num>0):
    r=num%10
    sum+=r**d
    num//=10
if(org_num==sum):
    print(f"{org_num} is a Armstrong Number")
else:
    print(f"{org_num} is not a Armstrong Number")