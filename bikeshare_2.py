import time
import pandas as pd
import numpy as np
from datetime import datetime
from dateutil.relativedelta import relativedelta
from sorted_months_weekdays import Month_Sorted_Month, Weekday_Sorted_Week
from calendar import day_name

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv'}


def get_forward_month_list():
    now = datetime.now()
    return Month_Sorted_Month([(now + relativedelta(months=month)).strftime('%B') for month in range(12)])[0:6]


def get_city_user_input():
    city = input("Enter city name you wanna get statistics about:").lower()
    while city not in CITY_DATA.keys():
        city = input("Enter a valid input:").lower()
    return city


def get_month_user_input():

    month_list = get_forward_month_list()
    month_list.insert(0, "All")

    month = input("Enter month name from Jan to Jun or type All to skip filtiration:").title()

    month_flag = True
    while month_flag:
        if month in month_list:
            month_flag = False
        else:
            month = input("Enter a valid input").title()
    return month


def get_day_user_input():
    days_list = Weekday_Sorted_Week([day_name[date] for date in range(7)])
    days_list.insert(0, "All")

    day_flag = True
    day = input("Enter a valid week day or type all to skip filtiration").title()
    while day_flag:
        if day in days_list:
            day_flag = False
        else:
            day = input("Enter a valid input").title()
    return day


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = get_city_user_input()

    # get user input for month (all, january, february, ... , june)

    month = get_month_user_input()

    # get user input for day of week (all, monday, tuesday, ... sunday)

    day = get_day_user_input()

    print('-'*40)

    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'], format="%Y-%m-%d %H:%M:%S")
    df['Month'] = df['Start Time'].dt.strftime('%B')
    df['Day'] = df['Start Time'].dt.strftime('%A')
    df['Hour'] = df['Start Time'].dt.strftime('%H')

    if month != "All":
        df = df[df.Month.eq(month)]
    if day != "All":
        df = df[df.Day.eq(day)]
    return df
#
#
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print(df.Month.mode())

    # display the most common day of week
    print(df.Day.mode())

    # display the  most common start hour
    print(df.Hour.mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#
#
# def station_stats(df):
#     """Displays statistics on the most popular stations and trip."""
#
#     print('\nCalculating The Most Popular Stations and Trip...\n')
#     start_time = time.time()
#
#     # display most commonly used start station
#
#
#     # display most commonly used end station
#
#
#     # display most frequent combination of start station and end station trip
#
#
#     print("\nThis took %s seconds." % (time.time() - start_time))
#     print('-'*40)
#
#
# def trip_duration_stats(df):
#     """Displays statistics on the total and average trip duration."""
#
#     print('\nCalculating Trip Duration...\n')
#     start_time = time.time()
#
#     # display total travel time
#
#
#     # display mean travel time
#
#
#     print("\nThis took %s seconds." % (time.time() - start_time))
#     print('-'*40)
#
#
# def user_stats(df):
#     """Displays statistics on bikeshare users."""
#
#     print('\nCalculating User Stats...\n')
#     start_time = time.time()
#
#     # Display counts of user types
#
#
#     # Display counts of gender
#
#
#     # Display earliest, most recent, and most common year of birth
#
#
#     print("\nThis took %s seconds." % (time.time() - start_time))
#     print('-'*40)
#
#
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(df)
        time_stats(df)
        # station_stats(df)
        # trip_duration_stats(df)
        # user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
