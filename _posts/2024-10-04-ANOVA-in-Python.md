---
layout: post
title: "A New Way to do ANOVA"
author: Gracie Stirk
description: A step by step guide to starting an ANOVA analysis in Python
image: "/assets/images/pretty-trees.jpg"
---

--- 
---
### ANOVA in Python
[ANOVA](https://researchmethod.net/anova/) is a catchy name for ANalysis Of VAriance. It's a useful tool for analyzing multiple means at the same time, specifically three or more means. This blog post is going to assume that the reader has a basic understanding of hypothesis testing and the python language.

For now, we'll do a one-way ANOVA. Let's say I want to see if actors in certain genres of film have different heights on average. Maybe I want to see if action heros are typically portrayed by taller actors on average. For the purpose of this post, I made up some data around this, which can be found [here.](https://raw.githubusercontent.com/gstirk27/My-Blog/refs/heads/main/actor_height.csv)

## Getting Started

The first step in this process will be to import the python libraries we need.

```python
import numpy as np
import pandas as pd
import scipy.stats as sp
from tabulate import tabulate
from statsmodels.formula.api import ols
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt
```

We'll primarily be using [scipy.stats](https://docs.scipy.org/doc/scipy/reference/stats.html) for its useful functions relating to ANOVA and variance.

Next, we read in the dataset:

```python
data = pd.read_csv('actor_height.csv')
print(data)
```

For this analysis, we'll be using the genre of film the actor stars in as our explanatory variable and we'll be using the height (in inches) of the actor as our response variable.

It's good practice to make sure that it's appropriate to do this analysis, so lets make sure that each group is approximately normal.

## Checking Assumptions

First we'll sort the data into four different groups.

```python
romance = data[data.loc[:, 'Genre'] == 'Romance']
horror = data[data.loc[:, 'Genre'] == 'Horror']
comedy = data[data.loc[:, 'Genre'] == 'Comedy']
action = data[data.loc[:, 'Genre'] == 'Action']
```

Next we'll check the skewness with a function in scipy.stats.

```python
rom_skew = sp.skew(romance.loc[:,'Height'])
hor_skew = sp.skew(horror.loc[:,'Height'])
com_skew = sp.skew(comedy.loc[:,'Height'])
act_skew = sp.skew(action.loc[:,'Height'])
```

This is some code that will put the skewness of each genre in a table:
```python
skews = [["Romance", rom_skew],["Horror", hor_skew],["Comedy", com_skew],["Action", act_skew]]

print(tabulate(skews, headers=["Genre", "Skewness"], tablefmt="grid"))
```
The table will look something like this:

| Genre      | Skewness   |
| ---------- | ---------- |
| Romance    | -0.207165  |
| Horror     | 0.262525   |
| Comedy     | -0.304662  |
| Action     | -0.0616975 |

There are [many different methods](https://datatab.net/tutorial/test-of-normality) to check if data is approximately normal, but checking if the skewness is between -0.5 and +0.5 is the technique I'm most familiar with. We can see from the above table that all of the genres are approximately normal. None of them are particularly left or right-skewed. 

We also need to check the standard deviations to make sure they're approximately equal.

We can use a similar technique to what we did with skewness. The library scipy.stats can calculate a sample standard deviation for each category.

```python
rom_sd = sp.tstd(romance.loc[:,'Height'])
hor_sd = sp.tstd(horror.loc[:,'Height'])
com_sd = sp.tstd(comedy.loc[:,'Height'])
act_sd = sp.tstd(action.loc[:,'Height'])
```

And we can look at the results in another table:

```python
stds = [["Romance", rom_sd],["Horror", hor_sd],["Comedy", com_sd],["Action", act_sd]]

print(tabulate(stds, headers=["Genre", "Standard Deviations"], tablefmt="grid"))
```

That code will yield this table:

| Genre      | Std Dev    |
| ---------- | ---------- |
| Romance    | 2.73264    |
| Horror     | 1.60773    |
| Comedy     | 3.06791    |
| Action     | 1.89804    |

The general rule I've learned to check this assumption is that the maximum standard deviation should not be more than 2x the smallest standard deviation. The horror genre has a standard deviation of 1.61, and then comedy genre has a standard deviation of 3.07, so that assumption is met as well!

So now we can move on to the fun stuff!

## The Fun Stuff

The first thing we should do is check to see if we need to reject our null hypothesis! Our null hypothesis is that the mean heights for all actors is the same across all genres, and our alternative hypothesis is that at least one is different.

The scipy.stats library has a function built in to do a one-way ANOVA analysis that we can use this way to get the F-statistic and the p-value.

```python
F_stat, p_val = sp.f_oneway(romance['Height'],horror['Height'],comedy['Height'],action['Height'])

```
This will give us a F-statistic of 3.911 and a p-value of 0.0128. If we use a significance level of 0.05, we can reject the null hypothesis and conclude that at least one of the mean heights is different than the others.

We can also get these values in an ANOVA table by using the ols function in the statsmodels library.

```python
model = ols('Height ~ Genre', data=data).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)
```
This will yield something like this table:

|            | sum_sq     | df         | F          | PR(>F)     |
| ---------- | ---------- | ---------- | ---------- | ---------- |   
| Genre      | 66.300703  | 3.0        | 3.910869   | 0.012838   |
| Residual   | 339.058672 | 60.0       | NaN        | NaN        |

This table tells us that the Genre has a statistically significant effect on the height of the actor.

## Looking a Little Closer

Let's see if we can dig a bit deeper to see what else is going on here.

We can create density plots of each of the heights to see if we can find any trends using the seaborn library.

```python
sns.kdeplot(romance.Height, label='Romance', color='hotpink', lw=2)
sns.kdeplot(horror.Height, label='Horror', color='black', lw=2)
sns.kdeplot(comedy.Height, label='Comedy', color='blue', lw=2)
sns.kdeplot(action.Height, label='Action', color='green', lw=2)
plt.legend(loc = "upper right")
plt.show()
```
This should yield us this graph:
![the density plot](https://github.com/gstirk27/My-Blog/blob/768cb2285ae53545975c8e3ed49dcad3ec55a0a7/assets/images/density_plot.png)

There's a lot of overlap, so it's hard to say for sure if one genre attracts taller actors to their movies.

Next, we can look at the confidence intervals.



## Conclusion

I hope you enjoyed this short tutorial for getting started with doing ANOVA in Python! I'm still learning about different functions in Python, so it was a bit basic today. We could keep going to determine which mean or means are different than the others, but I'll leave that for a future post! Thanks for coming with me on this Data Science journey!