#!/usr/bin/env python
# coding: utf-8

# In[87]:


import pandas as pd


# In[88]:


import seaborn as sns


# In[109]:


# get access to the data
# Malaria deaths by country for all ages across the world and time.

url_1 = 'https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2018/2018-11-13/malaria_deaths.csv'
df_death = pd.read_csv(url_1)
df_death.columns = ['Entity', 'Code', 'Year', 'Deaths']


# In[90]:


# Malaria incidence by country for all ages across the world across time

url_2 = 'https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2018/2018-11-13/malaria_inc.csv'
df_inc = pd.read_csv(url_2)
df_inc.columns = ['Entity', 'Code', 'Year', 'Incidence']
df_inc.head(5)


# In[125]:


# Malaria deaths by age across the world and time.

url_3 = 'https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2018/2018-11-13/malaria_deaths_age.csv'
df_death_age = pd.read_csv(url_3)
df_death_age.head(5)


# In[92]:


# first plot


# In[93]:


df_china = df_death_age.loc[df_death_age['entity'] == 'China']


# In[94]:


# China malaria deaths by age across time
with plt.xkcd():
    g = sns.lineplot(data=df_china, x='year', y='deaths', hue='age_group')
    g.set_title('China malaria deaths by age across time')
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


# In[95]:


df_china2 = df_death.loc[df_death['Entity'] == 'China']
df_china2.columns = ['Entity', 'Code', 'Year', 'Deaths']


# In[96]:


with plt.xkcd():
    g = sns.lineplot(data=df_china2, x='Year', y='Deaths')
    g.set_title('China malaria deaths across time')


# In[97]:


# second plot


# In[98]:


df_inc_country = df_inc.loc[df_inc['Entity'].isin(['Low income','Lower middle income'])]
df_inc_country.columns = ['Entity', 'Code', 'Year', 'Incidence']


# In[99]:


df_inc_country = df_inc_country.loc[:,['Entity', 'Incidence']]


# In[100]:


ax = sns.boxplot(x="Entity", y="Incidence", data=df_inc_country, palette="Set3").set_title("Incidence boxplot")


# In[101]:


# third plot


# In[102]:


df_death_country = df_death.loc[df_death['Entity'].isin(['Afghanistan','Congo','India','Southeast Asia', 'Sudan'])]


# In[103]:


df_death_country.columns = ['Entity', 'Code', 'Year', 'Death']
df_death_country = df_death_country.loc[:,['Entity', 'Year', 'Death']]


# In[104]:


df_death_country = df_death_country.loc[df_death_country['Year'] == 2015]
df_death_country


# In[105]:


sns.catplot(x='Entity', y='Death', kind="bar", data=df_death_country).fig.suptitle("Histogram of death across countries")


# In[118]:


# death over the world in 1990 and 2016
df_death_1990 = df_death.loc[df_death['Year'] == 1990]
df_death_2016 = df_death.loc[df_death['Year'] == 2016]


# In[119]:


import plotly.graph_objects as go
import pandas as pd

fig = go.Figure(data=go.Choropleth(
    locations = df_death_1990['Code'],
    z = df_death_1990['Deaths'],
    text = df_death_1990['Entity'],
    colorscale = 'Blues',
    autocolorscale=False,
    reversescale=False,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    #colorbar_tickprefix = '$',
    colorbar_title = 'Malaria deaths per 100,000 people',
))

fig.update_layout(
    title_text='Malaria deaths across the world in 1990',
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    )
)

fig.show()


# In[120]:


fig = go.Figure(data=go.Choropleth(
    locations = df_death_2016['Code'],
    z = df_death_2016['Deaths'],
    text = df_death_2016['Entity'],
    colorscale = 'Blues',
    autocolorscale=False,
    reversescale=False,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    #colorbar_tickprefix = '$',
    colorbar_title = 'Malaria deaths per 100,000 people',
))

fig.update_layout(
    title_text='Malaria deaths across the world in 2016',
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    )
)

fig.show()

