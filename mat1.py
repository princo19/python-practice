import matplotlib.pyplot as mat
x=[1,2,3]
y=[2,4,7]
x2=[2,3,4]
y2=[4,5,6]
mat.plot(x,y,label='First')
mat.plot(x2,y2,label='Second')
mat.xlabel('cost')
mat.ylabel('speed')
mat.title("interesting \n graph")
mat.legend()
mat.show()
