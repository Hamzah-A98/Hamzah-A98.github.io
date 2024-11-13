import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stat

# repeatedly sample from some population, calculate the mean and store it in a list
list_of_means = []
iterations = 10000

for j in range(iterations):
  sample = np.random.chisquare(df=10, size=100)
  sample_mean = np.mean(sample)
  list_of_means.append(sample_mean)

plt.figure(figsize=(10,10))
sns.set_style('darkgrid')
sns.histplot(list_of_means)
plt.title(f'Mean of all means: {np.round(np.mean(list_of_means),3)}')