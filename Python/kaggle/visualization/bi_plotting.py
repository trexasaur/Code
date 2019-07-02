# kaggle visualization course
# bivariate plotting
# Author: Tyler Weihing
# Date: 6/20/2019

import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------------------------
#                    daters
# -----------------------------------------------------


# -----------------------------------------------------
# import data:
reviews = pd.read_csv("../datasets/winemag-data_first150k.csv", index_col=0)

# -----------------------------------------------------
# scatter plot:
#reviews[reviews['price'] < 100].sample(100).plot.scatter(x='price', y='points')

# -----------------------------------------------------
# hex plot
#reviews[reviews['price'] < 100].plot.hexbin(x='price', y='points', gridsize=15)

# -----------------------------------------------------
# subset:
# pivot_subset = reviews.pivot(index='points', columns='variety')
# print(pivot_subset)

points_subset = reviews[(reviews['points'] <= 84) & (reviews['points'] >= 80)]
points_and_variety_ss = points_subset[points_subset['variety'].isin([
    'Bordeaux-style Red Blend', 'Cabernet Sauvignon', 'Chardonnay', 'Pinot Noir', 'Red Blend'
])]

my_subset = pivot_table(points_and_variety_ss, )

#points_subset['variety'].value_counts().sort_index().plot.line()

# -----------------------------------------------------
# outputs:
print(points_and_variety_ss.head())
plt.show()