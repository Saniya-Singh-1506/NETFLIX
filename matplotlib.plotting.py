import matplotlib.pyplot as plt

months=["jan","feb","march","april"]
sales=[1000,2000,1400,2500]

plt.plot(months,sales,color="magenta",linestyle="--",linewidth=2,marker="o"
         ,label="2025 sales")

plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Report")

plt.grid("color=gray",linestyle=":",linewidth=1)

plt.legend() #label set kiya h woh show krega as a small rectangular box
plt.show()