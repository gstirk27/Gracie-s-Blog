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

Now to convert the game ids into the game titles!