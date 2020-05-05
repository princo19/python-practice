a=eval(input("enter the value of a:"))
if(a%5==0 and a%10==0):
    print("Number divisibvle by 5 and 10")
elif(a%5==0 or a%10==0):
    print("Number divisible by 5 or 10")
else:
    print("Not divisible")
