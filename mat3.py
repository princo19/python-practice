import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7]
y=[2,3,4,5,6,7,8]
plt.hist(x,y,label='BARS',color='c',rwidth=0.7,ls='-')
#plt.hist(x2,y2,label="BARS2",color='r')
plt.xlabel('mine')
plt.ylabel('your')
plt.legend()
plt.title("Interesting bars")
plt.savefig("d:/pika.pdf",format="pdf")
plt.show()
