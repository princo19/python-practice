import matplotlib.pyplot as mat
import numpy as np
import math
x=np.arange(0,math.pi*2,0.05)
y=np.cos(x)
mat.plot(x,y)
mat.xlabel("angle")
mat.ylabel("cos")
mat.title("cos graph") 
mat.show()
