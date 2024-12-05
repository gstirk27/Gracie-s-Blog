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

<img src='https://raw.githubusercontent.com/gstirk27/My-Blog/refs/heads/main/assets/images/sidebar.png' alt = "" style = "width: 100%;"/>

</figure>

Through the sidebar in the app, you can narrow the table down to only the games with a lot of NPCs or just the fantasy races that feature most prominently in the Legend of Zelda franchise.