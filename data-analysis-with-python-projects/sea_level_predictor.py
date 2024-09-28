#Sea Level Predictor

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = pd.Series([i for i in range(1880,2051)])
    y = res.intercept + res.slope * x
    plt.plot(x , y , 'o', label= "1880-2050 predict")

    # Create second line of best fit
    new_df = df[df['Year'] >= 2000]
    res1 = linregress(new_df['Year'], new_df['CSIRO Adjusted Sea Level'])
    x1 = pd.Series([i for i in range(2000,2051)])
    y1 = res1.intercept + res1.slope * x1
    plt.plot(x1 , y1 , 'r', label= "2000-2050 predict")

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
