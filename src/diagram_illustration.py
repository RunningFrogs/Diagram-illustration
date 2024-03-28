import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# Create boxplot and heatmap with random values
data_boxplot = [np.random.normal(0, std, 100) for std in range(1, 4)]
outliers = np.random.uniform(low=-9, high=9, size=(10, 3))
data_boxplot_with_outliers = [np.concatenate([data, outlier], axis=0) for data, outlier in zip(data_boxplot, outliers.T)]

data_heatmap = np.random.rand(10, 10)

category_1 = np.random.rand(10)
category_2 = np.random.rand(10)

plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.boxplot(data_boxplot_with_outliers, patch_artist=True)
plt.title('Boxplot')

plt.subplot(1, 3, 2)
sns.heatmap(data_heatmap, annot=True, cmap='coolwarm')
plt.title('Heatmap')

# Create bar graph with random values
ind = np.arange(len(category_1))
width = 0.35

plt.subplot(1, 3, 3)
p1 = plt.bar(ind, category_1, width, color='b')
p2 = plt.bar(ind, category_2, width, bottom=category_1, color='r')
plt.title('Gestapeltes Säulendiagramm')

plt.tight_layout()
plt.savefig('../diagrams/diagrams.png')
