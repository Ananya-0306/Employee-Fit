from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sn
import pylab as pl

# reading the data from csv into a dataframe
df = pd.read_csv ('wic.csv')

# using the inbuild library - corr() to create a correlation matrix 
# this will help study the importance of each feature compared to the other
corrMatrix = df.corr()

# plot the heat map obtained 
plt.figure(figsize=(8,8))
sn.heatmap(corrMatrix, annot=True)
plt.title("Heatmap for India Combined Data")
plt.show()
