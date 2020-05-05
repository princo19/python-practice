import matplotlib.pyplot as mat
x=[1,2,3]
y=[4,5,6]
x2=[7,8,9]
y2=[10,12,13]
mat.pie(x,y,label="first",color='r',ls="-.",lw=4)
mat.pie(x2,y2,label="second",color="b",ls="--",lw=6)
mat.xlabel("cost")
mat.ylabel("speed")
mat.legend();
mat.title("interesting graph")
mat.show()
