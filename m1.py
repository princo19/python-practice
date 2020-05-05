from pylab import *
x=linspace(-3,3,30)
#y=x**2
#plot(x,y,"r.")
#show()

plot(x,sin(x),label="sinx")
plot(x,cos(x),"r-",label="cosx")
plot(x,-sin(x),"b.",label="-sinx")
legend()
show()

