y=[]
marks=0
for i in range(3):
    print("enter the marks:")
    y.append(int(input()))
    marks+=y[i]
if(marks>=90):
        print("grade a")
elif(marks>=80 and marks<=89):
        print("grade b")
elif(marks>=70 and marks<=79):
        print("grade c")
else:
        print("grade d")
