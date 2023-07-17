# Visualizing Google Trends Data Over Time

This code allows you to retrieve Google Trends data for specific search terms over a specified time period, and then plot this data to visualize how the search interest for these terms has changed over time.
This code utilizes the `pytrends` package, a Python interface for Google Trends. It consists of two functions: `getdata()` and `plot()`. 

The `getdata()` function takes in two parameters: a `search_term` (or a list of terms) and a `time_period`, and returns a pandas DataFrame showing the interest over time for the search term(s) in the specified time period. The Google Trends interest over time is a measure of the volume of searches for the term(s) relative to the total number of searches done on Google over that time. 

The `plot()` function takes in the DataFrame returned by `getdata()` and a list of columns to plot. It then plots the Google Trends interest over time data for the specified columns. 