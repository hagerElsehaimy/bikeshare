import time
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from sorted_months_weekdays import Month_Sorted_Month, Weekday_Sorted_Week
import calendar
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_forward_month_list():
    now = datetime.now()
    return Month_Sorted_Month([(now + relativedelta(months=month)).strftime('%b') for month in range(12)])[0:6]

def get_city_user_input():
    city = input("Enter city name to analyze:").lower()
    while city not in CITY_DATA.keys():
        city = input("Enter a valid input:").lower()
    return city

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
    month_list = get_forward_month_list()
    month_list.insert(0, "all")

    month_flag = True

    while month_flag:
        month_no = int(input("Enter month number from 1 to 6 or type  0 for all to analyze based on time frame:"))
        try:
            if month_list[month_no] in month_list:
                month_flag = False
        except:
            print("Enter a valid input")
    # get user input for day of week (all, monday, tuesday, ... sunday)
    date = datetime.strptime('05 11 2020','%d %m %Y')
    dates_list = []

    for day in range(7):
        date += timedelta(days=1)
        print(date)
        dates_list.append(date.weekday())
    days_list = Weekday_Sorted_Week([calendar.day_name[date] for date in dates_list])
    day_no = None

    print(dates_list)
    print(days_list)
    print('-'*40)

    return city, month_list[month_no], days_list[day_no]


# def load_data(city, month, day):
#     """
#     Loads data for the specified city and filters by month and day if applicable.
#
#     Args:
#         (str) city - name of the city to analyze
#         (str) month - name of the month to filter by, or "all" to apply no month filter
#         (str) day - name of the day of week to filter by, or "all" to apply no day filter
#     Returns:
#         df - Pandas DataFrame containing city data filtered by month and day
#     """
#
#
#     return df
#
#
# def time_stats(df):
#     """Displays statistics on the most frequent times of travel."""
#
#     print('\nCalculating The Most Frequent Times of Travel...\n')
#     start_time = time.time()
#
#     # display the most common month
#
#
#     # display the most common day of week
#
#
#     # display the most common start hour
#
#
#     print("\nThis took %s seconds." % (time.time() - start_time))
#     print('-'*40)
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
# def main():
#     while True:
#         city, month, day = get_filters()
#         df = load_data(city, month, day)
#
#         time_stats(df)
#         station_stats(df)
#         trip_duration_stats(df)
#         user_stats(df)
#
#         restart = input('\nWould you like to restart? Enter yes or no.\n')
#         if restart.lower() != 'yes':
#             break
#
#
# if __name__ == "__main__":
# 	main()
get_filters()