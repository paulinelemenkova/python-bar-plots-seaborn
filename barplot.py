#!/usr/bin/env python
# coding: utf-8
"""Bar Plots with Python and Seaborn

Author:  Polina Lemenkova
ORCID:   https://orcid.org/0000-0002-5759-1089
Archive: https://doi.org/10.13140/RG.2.2.22754.79046
License: MIT

See README.md for details.
"""
import os

import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt

os.chdir(os.path.dirname(os.path.abspath(__file__)))
df = pd.read_csv("Tab-Morph.csv")
sb.set_style("whitegrid")
sb.set_context('paper')

# define variables and plotting
fig = plt.figure(figsize=(10.0, 6.0), dpi=300)
fig.suptitle("Bar plots for the Mariana Trench geology: \nSediment thickness (left) and distance from igneous volcanic areas (right)",
             fontsize=10)
# subplot 1
ax1 = fig.add_subplot(1, 2, 1)
sb.catplot(x="profile", y="sedim_thick", data=df,
           kind="bar", palette='tab20b', ax=ax1
           )
# subplot 2
ax2 = fig.add_subplot(1, 2, 2)
sb.catplot(x="profile", y="igneous_volc", data=df,
           kind="bar", palette='tab20c', ax=ax2
           )

# printing and saving a file
plt.tight_layout()
plt.savefig('plot_Barplot.png', dpi=300)
plt.show()
