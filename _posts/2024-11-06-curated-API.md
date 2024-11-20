---
layout: post
title: "The Wonderful World of Zelda APIs"
author: Gracie Stirk
description: "An analysis on the different races in Hyrule based on the Legend of Zelda OpenSource API."
image: "/assets/images/totk-title-screen.jpg"
---

---
---
### Introduction
The Legend of Zelda series have some of my favorite games of all time. It's been a versatile Nintendo franchise that has persisted for decades, with new games coming out every year or so. As I learn about webscraping and APIs, I thought it would be fun to look at some online datasets about the franchise that fans have curated over the years.

One part of the franchise that I've always enjoyed is how many fun NPCs there are to interact with in every game. Not only are the characters fun to talk to, there are also many different "races" of characters with unique designs and culture. However, not every race is included in each game. The most human-like race, the Hylians, are featured in every game (since that's what race the main character, Link, is), but other races like Mogma or Deku Scrubs don't even make it to some of the later games. I want to see which games have the highest proportion of the different races. Or you could say I'm taking a census of the populations in each version of Hyrule Game.

### Getting the Data
The data I'm going to be using in this sample is from [`The Legend of Zelda API`](https://docs.zelda.fanapis.com). This API is open source and doesn't require an API key to access. In their Fair Use Policy, they say the API is free and open to use.

To start downloading the data, we'll need a few python packages.
```python
import pandas as pd
import requests
import re
import numpy as np
import urllib.parse
```

The API has a few different datasets that we can look at. For this analysis, we'll use the Games and Characters datasets.

There's probably more elegant ways to access the data, but this is how I got the character data:

```python
url = 'https://zelda.fanapis.com/api/characters?limit=100&page='
newurl = ""
all_data = []

for i in range(0,34) :
    newurl = url + str(i)
    r = requests.get(newurl)
    data = r.json()['data']
    all_data.extend(data)
```

This will go through all the pages of the api (there are 33 pages), grab all the data in them, and convert all the information into a single list.

After we do that, we can put it into a pandas DataFrame:

```python
df = pd.DataFrame(all_data)
```
At this point, you can see that it lists the game appearances of each character as a website link to the Game API. To convert it to something we can easily read, we can extract the end of the string and save it as a new column:

```python
df['str'] = df['appearances'].apply(lambda x: x[0] if isinstance(x, list) and len(x) > 0 else None)
df['str'].str.extract(r'([^/]+)$')
```

Now to convert the game IDs into the game titles!

One way to do this is to merge the dataset with the Games dataset on the same site. Each game on the site has a unique ID code.

There aren't as many games as there are characters, so we don't have to do a for loop for to get the games.

```python
urlg = 'https://zelda.fanapis.com/api/games?limit=100'
gr = requests.get(urlg)
gdata = gr.json()['data']
games = pd.DataFrame(gdata)
```

From here, there's a lot of extra information that we don't need, like publisher and release date. We can drop these extra columns with this command:
```python
games.drop(columns=['description','developer','publisher','released_date'],inplace=True)
```

To make sure the merge doesn't have any issues, we'll rename the columns so we don't have a character name column and a game name column:
```python
games.rename(columns={'id':'game_id','name':'title'},inplace=True)
```
Now, we're ready to merge our two datasets together! We'll want a left merge, since we want to keep most of the columns in the original dataset.

```python
newdf = pd.merge(df,games, on='game_id',how='left')
```
Next, we'll drop the extra columns the null values.
```python
characters = newdf.drop(columns=['appearances','description','str','string','id','game_id'])
```
It'll be hard to do an analysis with null values, so we'll just drop them for now.

```python
characters.dropna(inplace=True)
```
I've noticed that there's a lot of races included in the dataset that only show up once or twice (can be found with `characters['title'].value_counts()`). I don't want the analysis to become too cluttered, so I'll just look at some more popular character races.

Since I'm always worried I'm going to save over something important, I'll duplicatae the dataset so I can change some things around.

```python
forchi2 = characters[characters['race'].isin(['Lokomo','Zora','Hylian','Gerudo','Goron','Rito','Korok','Kokiri','Anouki','Kikwi','Sheikah','Hylians','Minish','Deku Scrub','Twili'])]
```
I've also noticed that there's a lot of games included in the dataset. It can be a hot topic in the fandom on what is really a Legend of Zelda game, but I don't think Freshly-Picked Tingle's Rosy Rupeeland with one entry is really going to tell me the information I need. So I'll narrow the game titles down to those that have more than 5 characters listed.

```python
tc = forchi2['title'].value_counts()
tc1 = tc[tc > 5].index
fforchi2 = forchi2[forchi2['title'].isin(tc1)]
```
Now we have a filtered dataset that only has more of the popular races and games.

To look at what's going on here, we can make a table of counts:
```python
pd.crosstab(fforchi2['race'], fforchi2['title'], margins=True, margins_name="Total")
```

There are a lot of zeros all across the board, which isn't unexpected. However, it does mean that it would be inappropriate to perform a Chi-Square test. We can also narrow down the races we include to only the ones that have more than 20 entries.

```python
forchi2 = forchi[forchi['race'].isin(['Zora','Hylian','Gerudo','Goron','Rito','Sheikah'])]
forchi2['title'].value_counts()
tc = forchi2['title'].value_counts()
tc1 = tc[tc > 5].index
fforchi2 = forchi2[forchi2['title'].isin(tc1)]
pd.crosstab(fforchi2['race'], fforchi2['title'], margins=True, margins_name="Total")
```
Now, lets look at some interesting facts we can glean from the marginal and conditional distributions.

- Breath of the Wild has the most characters listed in the dataset. This game has 49.39% of the entries for characters in this table.
- Hylians are the most common race included in the table. They make up 63.78% of the entries in the table.
- The Gerudo are the next most common race coming in at 13.17% of the entries in the table.
- Behind Hylians, Gorons have been in the most games. According to the data, they have appeared in all but three of the mainline Zelda games.
- The game title "The Legend of Zelda" had the fewest characters listed at only 7.

To look even closer, let's look at a pie chart:
```python
fforchi2['race'].value_counts().plot.pie(figsize=(7, 7), autopct='%1.1f%%')

```
(There should be a graph here, but it won't load in)

<figure>

<img src='https://raw.githubusercontent.com/gstirk27/My-Blog/refs/heads/main/assets/images/race-pie-chart.png' alt = "" style = "width: 60%;"/>

</figure>

We can see from here that over all the games, the human-like race has far more characters shown in the games.

```python
fforchi2.reset_index(inplace=True)
fforchi2['title'].value_counts().plot.pie(figsize=(7, 7), autopct='%1.1f%%')
```
(There should be a graph here, but it won't load in)
<figure>
<img src='/assets/images/game-pie-chart.jpg' alt = "" style = "width: 100%;"/>
</figure>

This chart shows how many characters are listed in each game. All of the early games tended to only have a few NPCs each, and then an open-world Zelda game out. In an open-world game, you need a lot more characters to make the environment feel alive and full, so it would make since that Breath of the Wild had more characters.

### Conclusions
Some things I noticed going through this data was that this dataset isn't comprehensive. I remember there being way more characters in certain games compared to the ones listed. So it's more like this a point estimate for the true proportion of characters. I would love to do this analysis again with even more characters listed. I wonder if next time I could scrape data from the Legend of Zelda wikipedia pages somehow.

I've also noticed that the newest Zelda games, Tears of the Kingdom and Echoes of Wisdom are not included on this list. I found in the pages [`release notes`](https://docs.zelda.fanapis.com/blog/v1-release) that it was last updated in 2022, which would explain why there isn't more information included.

I would encourage everyone reading this post to try it for themselves as well!

