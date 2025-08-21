import matplotlib.pyplot as plt

regions=["NORTH","EAST","SOUTH","WEST"]
revenue=[1000,1500,3000,2500]

plt.pie(revenue, labels=regions, autopct="%1.1f%%", 
        colors=["pink","gold","skyblue","lightgreen"])

plt.title("2025 Revenue")
plt.show()

#no grid and doesn"t need legend