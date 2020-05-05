import matplotlib.pyplot as plt
x=[1,3,5,7]
y=[10,12,14,16]
x2=[2,4,6,8]
y2=[9,11,13,15]
plt.bar(x,y,label='BARS',color='c')
plt.bar(x2,y2,label="BARS2",color='r')
plt.xlabel('mine')
plt.ylabel('your')
plt.legend()
plt.title("Interesting bars")
plt.show()
