n=int(input("enter the value for a:"))
r=0
while(n>0):
    s=n%10
    r=r*10+s
    n=n//10
print(r)
    
