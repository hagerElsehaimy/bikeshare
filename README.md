# bikeshare

Overview

In this project, Python is used to explore data related to bike share systems for three major cities in the United States — Chicago, New York City, and Washington.

The source code takes in raw input from the user to create an interactive experience.
According to the input the code will import the data and will provide information by computing descriptive statistics.

Files used:
    bikeshare_2.py

Used Software:
    python3 and pandas insalled on Anaconda.
    pycharm
    terminal
    Git

Helpful links:
    https://pandas.pydata.org/pandas-docs/version/0.21.1/generated/pandas.DataFrame.mode.html
    https://stackoverflow.com/questions/36341484/get-day-name-from-weekday-int
    https://www.programiz.com/python-programming/methods/list/insert
    https://stackoverflow.com/questions/41476150/removing-space-from-dataframe-columns-in-pandas
    https://www.geeksforgeeks.org/python-filtering-data-with-pandas-query-method/
    https://www.askpython.com/python/examples/convert-seconds-hours-minutes
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html

How it works:

There are four questions that will change the answers:

    Would you like to see data for Chicago, New York, or Washington?
    Would you like to filter the data by month, day, or not at all?
    (If they chose month) Which month - January, February, March, April, May, or June?
    (If they chose day) Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?
    May you want to have a look on the raw data? Type yes or no
    Would you like to restart or quit?

The answers to the questions above will determine the city and timeframe on which you'll do data analysis. After filtering the dataset, users will see the statistical result of the data, and choose to start again or exit.

The Datasets:

Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

    Start Time
    End Time
    Trip Duration in seconds
    Start Station
    End Station
    User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:
    Gender
    Birth Year

Statistics Computed:

The code helps user to tell about bike share use in Chicago, New York City and Washington by computing a variety of descriptive statistics. In this project, the code output will provide the following information:

Popular times of travel (i.e., occurs most often in the start time):
    most common month
    most common day of week
    most common hour of day

Popular stations and trip:
    most common start station
    most common end station
    most frequent combination of start station and end station)

Trip duration:
    total travel time
    average travel time

User info:
    counts of each user type
    counts of each gender (only available for NYC and Chicago)
    earliest, most recent, most common year of birth (only available for NYC and Chicago)
