#BAR CHARTS: USED FOR CATEGORY COMPARISION AND DATA ANALYTICS

import matplotlib.pyplot as plt

product=["A","B","C","D","E","F","G","H"]
sales=[1000,800,1500,600,2900
        ,1500,900,2500]

plt.bar(product,sales,color="pink",label="Sales 2025")
plt.xlabel("Productss")
plt.ylabel("Saless")
plt.title("Marketing Details")
plt.legend()
plt.grid(color="purple", linewidth=0.1,linestyle=":")

plt.show()
