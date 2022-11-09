# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 23:22:08 2022

@author: rak29
"""

#Trial


import matplotlib.pyplot as plt
import pandas as pd


world = pd.read_csv("E:/Herts/ADS1/Assignment 1/alpha/cause_of_deaths.csv")

required_region = ["United Kingdom"]

plt.figure()
uk = world.iloc[5790:5820]
uk["Total"] = uk.sum(axis=1)-uk["Year"]

germany = world.iloc[2010:2040]
germany["Total"] = germany.sum(axis=1)-germany["Year"]

france = world.iloc[1890:1920]
france["Total"] = france.sum(axis=1)-france["Year"]

italy = world.iloc[2610:2640]
italy["Total"] = italy.sum(axis=1)-italy["Year"]

#print(uk)

plt.plot(uk["Year"], uk["Cardiovascular Diseases"])
plt.plot(germany["Year"], germany["Cardiovascular Diseases"])
plt.plot(france["Year"], france["Cardiovascular Diseases"])
plt.plot(italy["Year"], italy["Cardiovascular Diseases"])
plt.xlim(1990,2019)
plt.show()

"""
plt.figure()
plt.hist(uk["Cardiovascular Diseases"],density=True,alpha=0.8,label="UK")
plt.hist(germany["Cardiovascular Diseases"],density=True,alpha=0.8,label="GER")
plt.hist(france["Cardiovascular Diseases"],density=True,alpha=0.8,label="FR")
plt.hist(italy["Cardiovascular Diseases"],density=True,alpha=0.8,label="IT")
plt.show()
"""
data = [uk["Cardiovascular Diseases"], germany["Cardiovascular Diseases"],france["Cardiovascular Diseases"],italy["Cardiovascular Diseases"]]
dlabel = ["UK","GER"]

plt.figure()
plt.boxplot([data[0] , data[1] , data[2], data[3]],labels=["UK","GER","FR","IT"])
plt.ylabel("Deaths")
#plt.savefig("C:/Users/ra22aan/OneDrive - University of Hertfordshire/Applied DS Lab/Week 3/Annual Return qstn 1c.png")
plt.show()


print(uk["Total"])


uk["cvd per total deaths"] = uk["Cardiovascular Diseases"]/uk["Total"]
germany["cvd per total deaths"] = germany["Cardiovascular Diseases"]/germany["Total"]
france["cvd per total deaths"] = france["Cardiovascular Diseases"]/france["Total"]
italy["cvd per total deaths"] = italy["Cardiovascular Diseases"]/italy["Total"]


plt.figure()
plt.hist(uk["cvd per total deaths"],density=True,alpha=0.8,label="UK")
plt.hist(germany["cvd per total deaths"],density=True,alpha=0.8,label="GER")
plt.hist(france["cvd per total deaths"],density=True,alpha=0.8,label="FR")
plt.hist(italy["cvd per total deaths"],density=True,alpha=0.8,label="IT")
plt.show()