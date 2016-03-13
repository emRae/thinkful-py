 # Write a script called "prob.py" that outputs frequencies, as well as creates and saves a boxplot, a histogram, and a QQ-plot for the data in this lesson. Make sure your plots have names that are reasonably descriptive.

# for frequencies
import collections

# for QQ-plots
import numpy as np 
import scipy.stats as stats

# for bloxplot & QQ-plots
import matplotlib.pyplot as plt

# that outputs frequencies
testlist = [1, 4, 5, 6, 9, 9, 9]
# Counter creates a dictionary with the key being this list number, the value being the times the number is in the list
c = collections.Counter(testlist)

# calculate the number of instances in the list
count_sum = sum(c.values())

for k,v in c.items():
  print("The frequency of number " + str(k) + " is " + str(float(v) / count_sum))


# as well as creates and saves a boxplot
x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
plt.boxplot(x)
plt.savefig("boxplot.png")

# clear the boxplot figure so we can create just a histogram figure
plt.clf()

# a histogram
plt.hist(x, histtype='bar')
plt.savefig("histogram.png")

# clear the histogram figure so we can create just a QQ-plot
plt.clf()

# and a QQ-plot

plt.figure()
test_data = np.random.normal(size=1000)   
graph1 = stats.probplot(test_data, dist="norm", plot=plt)
plt.savefig("QQ-plot-normal-random-function.png")

# clear the normal random function QQ-plot figure so we can create just the uniform random function QQ-plot figure
plt.clf()

plt.figure()
test_data2 = np.random.uniform(size=1000)   
graph2 = stats.probplot(test_data2, dist="norm", plot=plt)
plt.savefig("QQ-plot-uniform-random-function.png")

