a=['5','6','2','12','1','8','90']
b=[]
for i in a:
    if(len(a)>5 and i%2==0):
        a=i+10
        b.append(a)
a=b
print(a)
