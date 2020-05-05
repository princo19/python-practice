import matplotlib.pyplot as mat
views=[23,45,67,89,100,234,567]
days=range(1,8)
mat.plot(views,days,label="Youtube views",color="r",marker="D",markerfacecolor='g',ls="-.",lw=4)
mat.xlabel("NO. of views")
mat.ylabel("NO. of days")
mat.legend()
mat.title("Youtube Videos")
mat.show()

         
