import matplotlib.pyplot as mat
x=[45,21,34,56,78,98]
y=["java","python","c++","c","swift","php"]
mat.pie(x,labels=y,autopct='%1.1f%%')
mat.show()
