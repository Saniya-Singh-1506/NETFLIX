import matplotlib.pyplot as plt

plt.scatter([2,4,6],[60,80,100],color="purple",marker='o',label="SEC-A") #sectionA
plt.scatter([2,4,6],[40,60,80],color="orange",marker="o",label="SEC-B") #sectionB

plt.xlabel("HOURS STUDIES")
plt.ylabel("MARKS SCORED")

plt.title("COMPARISION BETWEEN SEC-A AND SEC-B")
plt.grid("True")
plt.legend()
plt.show()

