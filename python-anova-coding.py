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
#plt.savefig('density_plot.png', dpi=300, bbox_inches='tight')

#mean
mean_rom = romance['Height'].mean()
mean_hor = horror['Height'].mean()
mean_com = comedy['Height'].mean()
mean_act = action['Height'].mean()

#standard error
se_rom = romance['Height'].std() / np.sqrt(len(romance['Height']))
se_hor = horror['Height'].std() / np.sqrt(len(horror['Height']))
se_com = comedy['Height'].std() / np.sqrt(len(comedy['Height']))
se_act = action['Height'].std() / np.sqrt(len(action['Height']))

confidence_level = 0.95

#degrees of freedom
df_rom = len(romance['Height']) - 1
df_hor = len(horror['Height']) - 1
df_com = len(comedy['Height']) - 1
df_act = len(action['Height']) - 1

ci_rom = se_rom * 1.96  # For 95% CI
ci_hor = se_hor * 1.96
ci_com = se_com * 1.96
ci_act = se_act * 1.96

lower_rom = mean_rom - ci_rom
upper_rom = mean_rom + ci_rom
print("Romance CI: ", lower_rom, upper_rom)

lower_hor = mean_hor - ci_hor
upper_hor = mean_hor + ci_hor
print("Horror CI: ", lower_hor, upper_hor)

lower_com = mean_com - ci_com
upper_com = mean_com + ci_com
print("Comedy CI: ", lower_com, upper_com)

lower_act = mean_act - ci_act
upper_act = mean_act + ci_act
print("Action CI: ", lower_act, upper_act)