#!/usr/bin/env python
# coding: utf-8

# # <span style="color:black">Task 2 : Data Analysis On Global Terrorism  </span> 

# # <span style="color:black">Performed by : K.Shanthan</span>
# 

# # <span style="color:black">Organization : The Spark Foundation </span>
# 

# # <span style="color:black">Problem Statement : </span>

# In[ ]:


###  As a security/defence analyst, find out hot zone of Terrorism ###

###  what the security issues and insights you can derive by EDA  ###


# # <span style="color:black">Importing Libraries : </span>

# In[1]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


# In[2]:


df = pd.read_csv(r"C:\Users\DELL\Desktop\globalterrorismdb_0718dist.csv", encoding="latin-1",low_memory=False)


# # <span style="color:black"> Data Preprocessing </span>
# 

# In[3]:


df.shape


# In[4]:


df.head(5)


# In[5]:


df.columns


# In[6]:


df1=df[["iyear","imonth","iday","country_txt","region_txt","provstate","city","latitude","longitude","summary","attacktype1_txt","targtype1_txt","targsubtype1_txt","gname","motive","weaptype1_txt","weapsubtype1_txt","nkill","nwound","propvalue","propcomment"]]
df1


# In[7]:


df2=df1.rename(columns={"iyear":"year","imonth":"month","iday":"day","country_txt":"country","region_txt":"region","provstate":"state","attacktype1_txt":"attacktype","targtype1_txt":"targettype","targsubtype1_txt":"targetsubtype","gname":"gangname","weaptype1_txt":"weapontype","weapsubtype1_txt":"weapsubtype","nkill":"kill","nwound":"wound","propvalue":"propertyvalue"})
df2


# In[8]:


df2.shape


# In[9]:


df2.describe()


# In[10]:


df2.country.unique()


# In[11]:


df2.attacktype.unique()


# In[12]:


df2.gangname.unique()


# In[13]:


df2.isnull().sum()


# In[14]:


df2.dropna(subset=['state','city','latitude','longitude','summary','attacktype','targettype','targetsubtype','gangname','motive','weapontype','weapsubtype','kill','wound','propertyvalue','propcomment'],inplace=True)


# In[15]:


df2.isnull().sum()


# # <span style="color:black"> Finding Insights </span>
# 

# In[16]:


plt.figure(figsize=(12, 6))

# Create a bar plot
ax = df2['attacktype'].value_counts().plot(kind='bar', color='red')

# Add a title
plt.title('Attacking Methods Used', fontsize=10)

# Add labels to the x and y axes
ax.set_xlabel('Attack Type', fontsize=4)
ax.set_ylabel('Count', fontsize=4)

# Optionally, you can rotate the x-axis labels for better readability (if needed)
plt.xticks(rotation=20)

# Show the plot
plt.tight_layout()
plt.show()


# In[ ]:


# From the above figure Bombing/Explosion Frequently used attacking method


# In[17]:


plt.figure(figsize=(12, 6))

# Custom color palette
custom_palette = ['#FF5733', '#FF9F33', '#FFD433', '#A2FF33', '#33FFBE', '#339DFF', '#333BFF', '#8033FF', '#C133FF']

# Count the occurrences of each target type
target_counts = df2['targettype'].value_counts()

# Create a bar plot with custom colors
ax = target_counts.plot(kind='bar', color=custom_palette)

# Add labels and a title
ax.set_xlabel('Target Type', fontsize=14)
ax.set_ylabel('Count', fontsize=14)
ax.set_title('Target Type Distribution', fontsize=16)

# Rotate x-axis labels for better readability (if needed)
plt.xticks(rotation=45)

# Optionally, you can add additional styling or annotations as needed

# Show the plot
plt.tight_layout()
plt.show()


# In[ ]:


# from the above bar graph private citizens are mostly taregeted


# In[18]:


plt.figure(figsize=(15, 6))

# Custom color palette
custom_palette = plt.cm.viridis(range(len(df2['year'].unique())))

# Count the occurrences of each year
year_counts = df2['year'].value_counts().sort_index()

# Create a bar plot with custom colors
ax = plt.bar(year_counts.index, year_counts.values, color=custom_palette)

# Add labels and a title
plt.xlabel('Year', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.title('Terrorism Incidents by Year', fontsize=16)

# Rotate x-axis labels for better readability (if needed)

plt.xticks(year_counts.index, rotation=45)
# Optionally, you can add additional styling or annotations as needed

# Show the plot
plt.tight_layout()
plt.show()


# In[ ]:


# from the above graph terrorism is raised in betwen 2012 to 2017


# In[19]:


df2[['year','kill']].groupby(['year']).agg('sum')


# In[ ]:


# finding the year and no of Kills


# In[20]:


plt.figure(figsize=(16, 11))

# Get the top 20 countries with the highest terrorist attacks
top_countries = df2['country'].value_counts()[:20]

# Create a bar plot using matplotlib
plt.barh(top_countries.index, top_countries.values, color='blue')

# Add labels and a title
plt.xlabel('Number of Attacks', fontsize=14)
plt.ylabel('Country', fontsize=14)
plt.title('Countries with the Highest Number of Terrorist Attacks', fontsize=16)

# Invert the y-axis to show the highest count at the top
plt.gca().invert_yaxis()

# Show the plot
plt.tight_layout()
plt.show()


# In[ ]:


# Iraq has the Highest no of attacks


# In[21]:


top_states = df2['state'].value_counts()[:20]
plt.figure(figsize=(16,11))

# Generate a list of different colors for each bar
colors = plt.cm.viridis(np.linspace(0, 1, len(top_states)))

# Create a bar plot using matplotlib with different colors
plt.barh(top_states.index, top_states.values, color=colors)

# Add labels and a title
plt.xlabel('Number of Attacks', fontsize=14)
plt.ylabel('State', fontsize=14)  # Changed 'Country' to 'State' in ylabel
plt.title('States with the Highest Number of Terrorist Attacks', fontsize=16)

# Invert the y-axis to show the highest count at the top
plt.gca().invert_yaxis()

# Show the plot
plt.tight_layout()
plt.show()


# In[ ]:


# from the above figure Baghdad has highest no of attacks


# In[22]:


plt.figure(figsize=(11,8))
xyz = df2["region"].value_counts().iloc[:10]

# Create a pie chart
plt.pie(xyz, labels=xyz.index, autopct="%0.2f%%", radius=1.0)

# Set the title
plt.title("Top 10 Regions")

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

# Show the pie chart
plt.show()


# In[ ]:


# from the figure you can find the Top 10 Regions


# In[23]:


df2.columns


# In[30]:


plt.title("weapons used")
df2['weapontype'].value_counts()[:6].plot(kind='bar',color='orange')


# In[ ]:


# From the above figure mostly explosives are used for attacking


# In[44]:


plt.figure(figsize=(11,6))
top_terrorist_organizations = df2["gangname"].value_counts().head(10)

# Create a bar chart
plt.bar(top_terrorist_organizations.index, top_terrorist_organizations.values)

# Add labels and a title
plt.xlabel('Terrorist Organization', fontsize=14)
plt.ylabel('Number of Attacks', fontsize=14)
plt.title('Top 10 Terrorist Organizations', fontsize=16)

# Rotate x-axis labels for better readability (optional)
plt.xticks(rotation=45, ha='right')

# Show the bar chart
plt.tight_layout()
plt.show()


# # <span style="color:black"> Conclusion </span>
# 

# In[ ]:


# The Middle East and North Africa regions are most targetted ones


# In[ ]:


# Mostly weapons used are Explosives


# In[ ]:


# Baghdad state has highest number of attacks


# In[ ]:


# Country Iraq has highest number of attacks


# In[ ]:


# most terrorist activites done in North Africa


# In[ ]:


# THANK YOU

