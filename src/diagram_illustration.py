import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data_boxplot = [np.random.normal(0, std, 100) for std in range(1, 4)]
outliers = np.random.uniform(low=-9, high=9, size=(10, 3))
data_boxplot_with_outliers = [np.concatenate([data, outlier], axis=0) for data, outlier in zip(data_boxplot, outliers.T)]

data_heatmap = np.random.rand(10, 10)

category_1 = np.random.rand(10)
category_2 = np.random.rand(10)

plt.figure(figsize=(5, 5))
plt.boxplot(data_boxplot_with_outliers, patch_artist=True)
plt.title('Boxplot')
boxplot_filename = '../diagrams/boxplot.png'
plt.savefig(boxplot_filename)
plt.close()

plt.figure(figsize=(8, 6))
sns.heatmap(data_heatmap, annot=True, cmap='coolwarm')
plt.title('Heatmap')
heatmap_filename = '../diagrams/heatmap.png'
plt.savefig(heatmap_filename)
plt.close()

plt.figure(figsize=(10, 5))
ind = np.arange(len(category_1))
width = 0.35
plt.bar(ind, category_1, width, label='Kategorie 1', color='b')
plt.bar(ind, category_2, width, bottom=category_1, label='Kategorie 2', color='r')
plt.title('Balkendiagramm')
barchart_filename = ('../diagrams/bar_chart.png')
plt.savefig(barchart_filename)
plt.close()