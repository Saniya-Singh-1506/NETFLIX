import matplotlib.pyplot as plt
x=[10,20,30,40,50,60]
y=[2,4,8,4,10,1]
plt.subplot(1,2,1)
plt.plot(x,y)
plt.title("LINE GRAPH")
 
plt.subplot(1,2,2)
plt.bar(x,y)
plt.title("BAR GRAPH")

        
plt.tight_layout()
plt.show()