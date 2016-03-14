# Write a script called "prob_lending_club.py" that reads in the loan data, cleans it, and loads it into a pandas DataFrame. Use the script to generate and save a boxplot, histogram, and QQ-plot for the values in the "Amount.Requested" column. Be able to describe the result and how it compares with the values from the "Amount.Funded.By.Investors".

import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

# reads in the loan data and loads it into a pandas DataFrame

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

# cleans it

# removes rows with null values
loansData.dropna(inplace=True)


# generate and save a boxplot,
# About boxplots: http://stattrek.com/statistics/charts/boxplot.aspx
loansData.boxplot(column='Amount.Funded.By.Investors', return_type='axes')
plt.savefig("boxplot-amount-funded-by-investors.png")
plt.clf()

loansData.boxplot(column='Amount.Requested', return_type='axes')
plt.savefig("boxplot-amount-requested.png")
plt.clf()

# histogram, and 
# A histogram casts the distribution of data as the possible values and their relative frequency in the given set.
loansData.hist(column='Amount.Funded.By.Investors')
plt.savefig("histogram-amount-funded-by-investors.png")
plt.clf()

loansData.hist(column='Amount.Requested')
plt.savefig("histogram-amount-requested.png")
plt.clf()

# QQ-plot for the values in the "Amount.Requested" column
plt.figure()
graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.savefig("QQ-plot-amount-funded-by-investors.png")
plt.clf()

plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.savefig("QQ-plot-amount-requested.png")
plt.clf()
