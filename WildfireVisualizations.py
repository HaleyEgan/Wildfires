#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 10:28:51 2021

@author: haleyegan
"""
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("WildfiresCleaned.csv") #read csv file as df 
df.head()


#histograms of fires over years 
sns.set(style="darkgrid")
sns.histplot(data=df, x="Year", kde = True, bins = 20)
plt.show()

#name columns for axis
year = df["Year"]
fires = df["Fires"]
acres = df["Acres"]
sqMiles = df["Sq Miles"]

#build line chart for wildfires over years 
fig, ax1 = plt.subplots(figsize=(8, 6))
ax1.set_ylabel('Total Fires')
ax1.set_xlabel('Year')
ax1.set_title('Wildfires Over Time')
ax1.plot(year, fires)

#line chart for acres burnt over years
fig, ax2 = plt.subplots(figsize=(8,6))
ax2.set_ylabel('Total Acres Burnt')
ax2.set_xlabel('Year')
ax2.set_title('Acres Burnt Over Time')
ax2.plot(year, acres)

#line chart for sq miles burnt over years
fig, ax3 = plt.subplots(figsize=(8,6))
ax3.set_ylabel('Total Sq Miles Burnt')
ax3.set_xlabel('Year')
ax3.set_title('Square Miles Burnt Over Time')
ax3.plot(year, sqMiles)

#stacked line chart
plt.stackplot(year, fires, sqMiles, labels=['Fires','Sq Miles'])
plt.legend(loc='upper left')

