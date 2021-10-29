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

df.to_csv("WildfiresCleaned.csv", index=False) #write to new csv file 