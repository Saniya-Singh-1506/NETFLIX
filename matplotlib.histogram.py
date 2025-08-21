import matplotlib.pyplot as plt

scores=[23,44,56,54,67,89,90,100,28,55,67,89,46,86,90,100,
        25,98,1,2,6,11,15,35,33,39]

plt.hist(scores,bins=5,color="purple",edgecolor="black")
plt.xlabel("TOTAL SCORE")
plt.ylabel("STUDENTS")

plt.plot("STUDENTS 2025")

plt.show()

#bin5: divide in 5 groups