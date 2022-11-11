# -*- coding: utf-8 -*-

"""
This program takes cause of deaths data from around the world and produces plots 
for certain countries which can be used to compare and analyse the data.
"""

#Importing required packages
import matplotlib.pyplot as plt
import pandas as pd

#Reading the file to the dataframe 'world'
world = pd.read_csv("E:/Herts/ADS1/Assignment 1/ADS1_Assignment_Visualisation/cause_of_deaths.csv")

#Creating seperate dataframes for each country and creating a new row for total deaths each year
uk = world.iloc[5790:5820]
uk["Total"] = uk.sum(axis=1) - uk["Year"]
germany = world.iloc[2010:2040]
germany["Total"] = germany.sum(axis=1) - germany["Year"]
france = world.iloc[1890:1920]
france["Total"] = france.sum(axis=1)-france["Year"]
italy = world.iloc[2610:2640]
italy["Total"] = italy.sum(axis=1)-italy["Year"]

def lineplot_different_countries(y_axis, x_axis):
    """
    
        This function creates line plots for cardiovascular disease deaths for the countries 
        UK, Germany,Francy, and Italy with x and y axis given through arguments.
        Graphs are also saved as images to local directory

    Parameters
    ----------
    y_axis : string
        Variable to be used as the y axis. This will speify which column
        to use from the dataframe.
    x_axis : string
        Variable to be used as the x axis. This will speify which column
        to use from the dataframe.

    Returns
    -------
    None.

    """

    plt.figure()
    plt.plot(uk[y_axis], uk[x_axis])
    plt.plot(germany[y_axis], germany[x_axis])
    plt.plot(france[y_axis], france[x_axis])
    plt.plot(italy[y_axis], italy[x_axis])
    plt.xlim(1990,2019)
    plt.xlabel("Year")
    plt.ylabel("Cardiovascular Deaths")
    plt.legend(["UK", "DE", "FR", "IT"])
    plt.savefig("line1.png", dpi=300, bbox_inches='tight')
    plt.show()

def line_plot_different_diseases_uk(y_axis, reason_1, reason_2, reason_3):
    """
    
    This function takes number of deaths from multiple causes of death in the uk and 
    creates a lineplot of them against year. Graphs are also saved as images to local directory.

    Parameters
    ----------
    y_axis : string
        Variable to be used as the y axis. This will speify which column
        to use from the dataframe..
    reason_1 : string
        Cause of death that will be used in the plot.
    reason_2 : string
        Cause of death that will be used in the plot.
    reason_3 : string
        Cause of death that will be used in the plot.

    Returns
    -------
    None.

    """


    plt.figure()
    plt.plot(uk[y_axis],uk[reason_1])
    plt.plot(uk[y_axis],uk[reason_2])
    plt.plot(uk[y_axis],uk[reason_3])
    plt.xlabel("Year")
    plt.xlim(1990,2019)
    plt.ylabel("Deaths in UK")
    plt.legend(["Alcohol abuse", "Violence", "Drowning"])
    plt.savefig("line2.png", dpi=300, bbox_inches='tight')
    plt.show()

def box_plot(data):
    """
    
    This function creates box plots for cardiovascular disease deaths for certain countries.
    Graphs are also saved as images to local directory

    Parameters
    ----------
    data : list
        List containing causes of death from different countries

    Returns
    -------
    None.

    """

    plt.figure()
    plt.boxplot([data[0] , data[1] , data[2], data[3]], labels=["UK", "DE", "FR", "IT"])
    plt.ylabel("Cardiovascular Deaths")
    plt.savefig("box.png", dpi=300, bbox_inches='tight')
    plt.show()

def bar_chart(cause):
    """
    This function creates bar charts for a certain cuntries where cause of death 
    is given as argument. Graph is also saved as images to local directory

    Parameters
    ----------
    cause : string
        Cardiovascular deaths per total deaths

    Returns
    -------
    None.

    """

    plt.figure()
    plt.hist(uk[cause], label = "UK", density=True, alpha=0.7)
    plt.hist(germany[cause], label = "DE", density=True, alpha=0.7)
    plt.hist(france[cause], label = "FR", density=True, alpha=0.7)
    plt.hist(italy[cause], label = "IT", density=True, alpha=0.7)
    plt.legend()
    plt.xlabel("CVD per Total Deaths")
    plt.savefig("bar.png", dpi=300, bbox_inches='tight')
    plt.show()


#creating a new array to pass to box plot function
cause = "Cardiovascular Diseases"
data = [uk[cause], germany[cause],france[cause],italy[cause]]

#Creating new row Cardiovascular Diseases deaths per total deaths for each country
uk["cvd per total deaths"] = uk["Cardiovascular Diseases"]/uk["Total"]
germany["cvd per total deaths"] = germany["Cardiovascular Diseases"]/germany["Total"]
france["cvd per total deaths"] = france["Cardiovascular Diseases"]/france["Total"]
italy["cvd per total deaths"] = italy["Cardiovascular Diseases"]/italy["Total"]

#Calling functions to create plots
lineplot_different_countries("Year", "Cardiovascular Diseases")
line_plot_different_diseases_uk("Year", "Alcohol Use Disorders", "Interpersonal Violence", "Drowning")
box_plot(data)
bar_chart("cvd per total deaths")