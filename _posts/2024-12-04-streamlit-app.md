---
layout: post
title: "Exploring Data With Streamlit"
author: Gracie Stirk
description: "Looking through the data of the previous post (getting data through an API) in a streamlit app"
image: "/assets/images/totk-finale.jpg"
---

---
---
### Introduction

One of my favorite video game series has been the Legend of Zelda series. It's a fantasy series that depicts many NPCs (non-playable characters) with different races and cultures. I thought it would be interesting to look at the demographics of each race in Hyrule (the fantasy kingdom where the games take place) to see which races make up the majority and how those majorities change between the different games. 

In my last [post](https://gstirk27.github.io/My-Blog/2024/11/06/curated-API.html), I got some data from [`the Legend of Zelda API`](https://docs.zelda.fanapis.com/) and used some Exploratory Data Analysis techniques to find out if there are any particularly interesting insights that I could glean from the data. In this post, we will look further into these insights using a streamlit app. The app I made for this post can be found [here](https://hyrule-census.streamlit.app/) and the code I used for this app can be found in [this](https://github.com/gstirk27/Z_streamlit/tree/main) GitHub repository.

### The App

When I was writing up the code for the previous post, I found it difficult to determine the best way to visually represent the data. With the streamlit app, it's a lot easier to try a lot of iterations of the same visuals to see if there's anything interesting going on.

I like to visualize proportions in table of counts, since I feel like they're easy to interpret. However, the dataset I'm working with is quite large and has many different categories. The first important feature I added to the app was the ability to filter out games or fantasy races where there are only a few entries across the whole dataset. 

<figure>

<img src='https://raw.githubusercontent.com/gstirk27/My-Blog/refs/heads/main/assets/images/sidebar.png' alt = "" style = "width: 50%;"/>

</figure>

Through the sidebar in the app, you can narrow the table down to only the games with a lot of NPCs or just the fantasy races that feature most prominently in the Legend of Zelda franchise. This cuts down on a lot of the clutter.

The rest of the app is divided into 3 parts. The first tab is the main table of counts that shows all of the game titles and race names as specified from the sidebar. Unfortunately, the app won't show the entire table at once, but you can still scroll through it.

<figure>

<img src='https://raw.githubusercontent.com/gstirk27/My-Blog/refs/heads/main/assets/images/table-counts-main.png' alt = "" style = "width: 65%;"/>

</figure>

Below the table are pie charts that show the marginal distributions for how many characters are in each game and how many characters are in each race.

The second and third tabs expand into conditional distributions. In the Game tab, you can specify which games in the franchise you would like to look at. This is an easy way to see the proportion of each race in a variety of the franchise's games. In the Race tab, you can look at a variety of races and see which games they feature most prominently in.

Below the table of counts in each tab are pie charts that visualize what each table is saying.

### Insights

One thing to note about the data is that it isn't a comprehensive list of every Legend of Zelda NPC as I initially hoped when putting all of this together. The website I got the data from didn't specify exactly how they collected all of their information, but I would assume that they only included characters with significant dialogue or side quests in their study. I was able to decypher this from the Game tab in the app. I know from experience that there are more than four Korok characters in Breath of the Wild, and I would guess that there are more than 64 characters in Ocarina of Time, one of the most beloved and analyzed games in this series. I also know there's at least one Sheikah character in Skyward Sword (a recurring character in many of the games, Impa), whom isn't listed in the table.

<figure>

<img src='https://raw.githubusercontent.com/gstirk27/My-Blog/refs/heads/main/assets/images/insights-table.png' alt = "" style = "width: 65%;"/>

</figure>

I was also fascinated to see that "Humans" are the second most common race in Hyrule (following Hylians, which are pretty much humans, but have curved ears like elves). This surprised me, since humans aren't even featured in every game. They don't appear at all in Breath of the Wild, which is the game that has the most NPCs.

<figure>

<img src='https://raw.githubusercontent.com/gstirk27/My-Blog/refs/heads/main/assets/images/hylians-and-humans.png' alt = "" style = "width: 65%;"/>

</figure>

### Conclusion

In this post, we've gone over different features I've made in a streamlit app that will help anyone with analyzing the dataset I gathered in my last post about the game franchise the Legend of Zelda and the different fantasy races featured in each game. 

There are many things to learn about through this dataset that I didn't have time to cover, so I would encourage everyone reading this to try the app out for themselves!