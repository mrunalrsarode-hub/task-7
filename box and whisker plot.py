import matplotlib.pyplot as plt
import numpy as np

# Dataset
marks = [45, 50, 52, 48, 47, 49, 51, 53, 46, 200]

# Box Plot
plt.boxplot(marks)
plt.title("Box and Whisker Plot")
plt.ylabel("Marks")
plt.show()

# Quartiles
Q1 = np.percentile(marks, 25)
Q2 = np.percentile(marks, 50)
Q3 = np.percentile(marks, 75)

print("Q1 =", Q1)
print("Median(Q2) =", Q2)
print("Q3 =", Q3)

# Tukey Method
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print("Lower Bound =", lower_bound)
print("Upper Bound =", upper_bound)

# Detect Outliers
outliers = []

for x in marks:
    if x < lower_bound or x > upper_bound:
        outliers.append(x)

print("Outliers =", outliers)