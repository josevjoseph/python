import math
# main
p=float(input("enter the principle amount: "))
y=int(input("enter the no. of years: "))
r=int(input("enter interest rate: "))
ip=p
print("year \t starting balance \t interest \t\t ending balance")
for i in range(1,y+1):
    a=p*(r/100)
    b=a+p
    print(i,"\t",round(p,2),"\t\t",round(a,2),"\t\t  ",round(b,2))
    p=b
print("ending balance: $",round(p,2))
print("total interest: $",round(p-ip,2))
    
   
