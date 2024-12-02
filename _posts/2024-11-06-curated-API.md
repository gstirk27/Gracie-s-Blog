---
layout: post
title: "Taking a Census of Hyrule"
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

The code for this post can be found in [this](https://github.com/gstirk27/ds_blog_code/blob/main/post-2-code.ipynb) GitHub repository.

The main Python packages we'll need are the pandas, requests, re, and urllib.parse libraries

The API has a few different datasets that we can look at. For this analysis, we'll use the Games and Characters datasets.

To access all the different pages of the API (which only includes about 50 entries per page), I used the requests library and a for loop to get all the data entries. From there, I put it into a pandas DataFrame.

### Cleaning the Data

Cleaning the data took a little work, since it listed the character's game appearances as id codes for the game that align with their internal database of the games. I extracted the code and compared it with the id codes in the Games datasets to convert the "appearances" column into game titles that we can actually read.

I also dropped the null values in the dataset to make the analysis go easier.

Looking through the data, I noticed that there's a lot of races included in the dataset that only show up once or twice (can be found with `characters['title'].value_counts()`). To avoid some clutter, I narrowed the results down to just the races that have more than 20 entries in the dataset.

I've also noticed that there's a lot of games included in the dataset. It can be a hot topic in the fandom on what is really a Legend of Zelda game, but I don't think Freshly-Picked Tingle's Rosy Rupeeland with one entry is really going to tell me the information I need. So I'll narrow the game titles down to those that have more than 5 characters listed.

<figure>

<img src='https://raw.githubusercontent.com/gstirk27/My-Blog/refs/heads/main/assets/images/table_counts.png' alt = "" style = "width: 100%;"/>

</figure>

There are a lot of zeros all across the board, which isn't unexpected. However, it does mean that it would be inappropriate to perform a Chi-Square test. 

### Things of Interest
Now, lets look at some interesting facts we can glean from the marginal and conditional distributions.

- Breath of the Wild has the most characters listed in the dataset. This game has 49.39% of the entries for characters in this table.
- Hylians are the most common race included in the table. They make up 63.78% of the entries in the table.
- The Gerudo are the next most common race coming in at 13.17% of the entries in the table.
- Behind Hylians, Gorons have been in the most games. According to the data, they have appeared in all but three of the mainline Zelda games.
- The game title "The Legend of Zelda" had the fewest characters listed at only 7.

To look even closer, let's look at a pie chart:

<figure>

<img src='https://raw.githubusercontent.com/gstirk27/My-Blog/refs/heads/main/assets/images/race-pie-chart.jpg' alt = "" style = "width: 60%;"/>

</figure>

We can see from here that over all the games, the human-like race has far more characters shown in the games.

<figure>

<img src='https://raw.githubusercontent.com/gstirk27/My-Blog/refs/heads/main/assets/images/game-pie-chart.jpg' alt = "" style = "width: 100%;"/>

</figure>

This chart shows how many characters are listed in each game. All of the early games tended to only have a few NPCs each, and then an open-world Zelda game out. In an open-world game, you need a lot more characters to make the environment feel alive and full, so it would make since that Breath of the Wild had more characters.

### Conclusions
Some things I noticed going through this data was that this dataset isn't comprehensive. I remember there being way more characters in certain games compared to the ones listed. So it's more like this a point estimate for the true proportion of characters. I would love to do this analysis again with even more characters listed. I wonder if next time I could scrape data from the Legend of Zelda wikipedia pages somehow.

I've also noticed that the newest Zelda games, Tears of the Kingdom and Echoes of Wisdom are not included on this list. I found in the pages [`release notes`](https://docs.zelda.fanapis.com/blog/v1-release) that it was last updated in 2022, which would explain why there isn't more information included.

I would encourage everyone reading this post to try it for themselves as well!

