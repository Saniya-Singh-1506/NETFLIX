import matplotlib.pyplot as plt

hours_studie=[2,4,6,8,10,14]
marks_scores=[50,60,70,80,90,100]

plt.scatter(hours_studie,marks_scores,color="blue",marker='o',label="2025 STUDENTS")
plt.grid(True)
plt.xlabel("STUDYING HOURS")
plt.ylabel("MARKS SCORED")
plt.title("RELATION B/W MARKS AND HOURS")
plt.legend()

plt.show()