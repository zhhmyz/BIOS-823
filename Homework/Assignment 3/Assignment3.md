---
title: "HW3 : Informative visualizations about malaria"
date: 2020-09-19
description: For Assignment 3
---

In this assignment, I will create 3 informative visualizations about malaria data using Python. 

### Source data and code 

- [Malaria](https://github.com/rfordatascience/tidytuesday/tree/master/data/2018/2018-11-13) dataset contains three tables: Malaria incidence and deaths by country, deaths by age across the world and time.
- You can access to the source code for visualizations here: [Github]()

### Informative visualizations

#### 1. Malaria deaths across time in China

I created a lineplot using seaborn to depict the overall death caused by malaria from 1990-2015 in China.  Based in this plot, we can see that as time increases from 1990 to 2015, the overall deaths decrease dramatically. 

![China Deaths](/project/images/China_deaths.png)

Then I am curious about whether this decreasing trend applies to all the age group. So I created a multiple line plot of China malaria deaths grouped by different age groups. Based on this plot, we can see that in group with age 15-49, the deaths decreased dramatically. In 5-14 age group, the death shows a slight decreasing trend. However, in the other three age groups, the death increases over time. Therefore, we may get a conclusion from these two plots that it is the decreasing death in people of 15-49 ages exert a great impact on the overall decreasing trend in China.

![China Deaths](/project/images/china_deaths_age.png)

#### 2.Malaria deaths across the world in 1990 and 2016

I map the malaria deaths data of 1990 and 2016 to the world map to display the worldwide distributions. Areas with more deaths will have a darker blue.

![China Deaths](/project/images/death_world_1990.png)

![China Deaths](/project/images/death_world_2016.png)

Observe the legend, it is obvious to see that the overall death in the world is lower in 2016 than that in 1990. Countries that are influenced by malaria did not change too much. 

In 1990, countries in the  middle and east costal of Africa have higher deaths. However,  this 'large death area' moves to the north of Afria in 2016.

#### 3. Compare malaria incidence in low-income area and lower-middle-income area

An incidence boxplot was created to compare incidences in two areas. 

![China Deaths](/project/images/incidence_boxplot.png)

From the plot, we can find that low income areas have a overall higher malaria incidence compared with the incidence in lower middle income areas.





















