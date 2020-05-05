a = []
c= []

a= int(input("Enter total numbers of the first list : "))

#take inputs from the user for the first list
for i in range(1,a+1):
  no = int(input("Enter : "))
  a.append(no)
  
#get total count for the second list
b= eval(input("Enter total numbers of the second list : "))

#take inputs from the user for the second list
for i in range(1,b+1):
  d= eval(input("Enter : "))
  c.append(d)
  
#print first and second list
print("First list : ",a)
print("Second list : ",c)

#append both list
final_list = a+c
#sort the final list
final_list.sort()

#print the final sorted list
print("Final list : ",final_list)
