# kaggle visualization course
# univariate plotting
# Author: Tyler Weihing
# Date: 6/20/2019

import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------------------------
# import data:
reviews = pd.read_csv("../datasets/winemag-data_first150k.csv", index_col=0)

# -----------------------------------------------------
#                 Categorical Charts
# -----------------------------------------------------

# -----------------------------------------------------
# Bar charts:

# absolute # of wines by province
#reviews['province'].value_counts().head(10).plot.bar()

# relative proportions of wines by province
#(reviews['province'].value_counts().head(10) / len(reviews)).plot.bar()

# wine review scores
#reviews['points'].value_counts().sort_index().plot.bar()

# -----------------------------------------------------
# line charts:
#reviews['points'].value_counts().sort_index().plot.line()

# -----------------------------------------------------
# area charts:
#reviews['points'].value_counts().sort_index().plot.area()

# -----------------------------------------------------
#                    Interval Data
# -----------------------------------------------------

# -----------------------------------------------------
# Histogram
#reviews[reviews['price'] < 200]['price'].plot.hist()
reviews['points'].plot.hist()

# skewed hist
#reviews['price'].plot.hist()

# -----------------------------------------------------
#                   Some Outputs
# -----------------------------------------------------

# -----------------------------------------------------
# look at some things:

#print(reviews.head())
plt.show()