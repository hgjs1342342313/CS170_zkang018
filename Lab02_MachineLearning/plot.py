import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt('CS170_Spring_2022_Small_data__38.txt')
x1 = np.zeros(0)
x2 = np.zeros(0)
y1 = np.zeros(0)
y2 = np.zeros(0)
for i in data:
    if i[0] == 1:
        x1 = np.append(x1, i[3])
        y1 = np.append(y1, i[7])
    else:
        x2 = np.append(x2, i[3])
        y2 = np.append(y2, i[7])
plt.scatter(x1, y1, color='red')
plt.scatter(x2, y2, color='blue')
plt.title("small personal dataset")
plt.xlabel("Feature 3")
plt.ylabel("Feature 7")
plt.show()