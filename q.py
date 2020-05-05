l1=[1,2,3,4,5,6]
l2=[2,3,4,5,6,7]
l3=l1+l2
print(str(l3))

for i in l2:
    l1.append(i)
print(str(l1))
l=[y for x in[l1,l2] for y in x]
print(str(l))

           
