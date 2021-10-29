#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Wildfire Data Cleaner
"""
import pandas as pd

df = pd.read_csv("Wildfires.csv") #read in original csv file 
df.head() #look at data 

#sort by year in ascending order 
df = df.sort_values(by=['Year']) #sort by year from oldest to newest 
df.head() #look at data 

#convert acres column to a float 
df.astype({'Acres':'float64'}).dtypes

#new column for square miles
df["Sq Miles"] = df["Acres"] * 0.0015625
df.head() #look at data

df.to_csv("WildfiresCleaned.csv", index=False) #write to new csv file 