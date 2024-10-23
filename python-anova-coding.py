#the code!

#import libraries

import numpy as np
import pandas as pd
import scipy.stats as sp
from tabulate import tabulate
from statsmodels.formula.api import ols
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt

#import and show data

data = pd.read_csv('actor_height.csv')
#print(data)

#checking assumptions
#dividing up the data
romance = data[data.loc[:, 'Genre'] == 'Romance']
horror = data[data.loc[:, 'Genre'] == 'Horror']
comedy = data[data.loc[:, 'Genre'] == 'Comedy']
action = data[data.loc[:, 'Genre'] == 'Action']

#finding skewness
rom_skew = sp.skew(romance.loc[:,'Height'])
hor_skew = sp.skew(horror.loc[:,'Height'])
com_skew = sp.skew(comedy.loc[:,'Height'])
act_skew = sp.skew(action.loc[:,'Height'])

skews = [["Romance", rom_skew],["Horror", hor_skew],
         ["Comedy", com_skew],["Action", act_skew]]

#make a table
#print(tabulate(skews, headers=["Genre", "Skewness"], tablefmt="grid"))

#standard deviations
rom_sd = sp.tstd(romance.loc[:,'Height'])
hor_sd = sp.tstd(horror.loc[:,'Height'])
com_sd = sp.tstd(comedy.loc[:,'Height'])
act_sd = sp.tstd(action.loc[:,'Height'])

stds = [["Romance", rom_sd],["Horror", hor_sd],["Comedy", com_sd],["Action", act_sd]]

#make a table
#print(tabulate(stds, headers=["Genre", "Standard Deviations"], tablefmt="grid"))

F_stat, p_val = sp.f_oneway(romance['Height'],horror['Height'],comedy['Height'],action['Height'])
#print("The F-Statistic is " + str(F_stat) + ".")
#print("The p-value is " + str(p_val) + ".")


#model = ols('Height ~ romance, horror, comedy, action', data=heights).fit()
model = ols('Height ~ Genre', data=data).fit()

anova_table = sm.stats.anova_lm(model, typ=2)
#print(anova_table)

#plt.hist(romance.Height, bins = 10, alpha = 0.5, color = "hotpink", label = "Romance")
#plt.hist(horror.Height, bins = 10, alpha = 0.5, color = "darkgray", label = "Horror")
#plt.hist(comedy.Height, bins = 10, alpha = 0.5, color = "blue", label = "Comedy")
#plt.hist(action.Height, bins = 10, alpha = 0.5, color = "green", label = "Action")
sns.kdeplot(romance.Height, label='Romance', color='hotpink', lw=2)
sns.kdeplot(horror.Height, label='Horror', color='black', lw=2)
sns.kdeplot(comedy.Height, label='Comedy', color='blue', lw=2)
sns.kdeplot(action.Height, label='Action', color='green', lw=2)
plt.legend(loc = "upper right")
#plt.show()
plt.savefig('density_plot.png', dpi=300, bbox_inches='tight')