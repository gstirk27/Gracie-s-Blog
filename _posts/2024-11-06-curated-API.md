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