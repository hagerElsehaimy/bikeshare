import time
import pandas as pd
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from sorted_months_weekdays import Month_Sorted_Month, Weekday_Sorted_Week
from calendar import day_name
from os import system

CITY_DATA = {'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv'}


def get_forward_month_list():
    """
    Fill a list with week months names automatically.

    Returns:
        List of week months names
    """

    now = datetime.now()
    return Month_Sorted_Month([(now + relativedelta(months=month)).strftime('%B') for month in range(12)])[0:6]


def get_forward_day_list():
    """
    Fill a list with week days names automatically.

        Returns:
            List of week days names
        """

    return Weekday_Sorted_Week([day_name[date] for date in range(7)])


def get_city_user_input():
    """
    get User Input for one the city name saved in CITY_DATA
    Returns:
        (str) city name entered by user after validation
    """
    try:
        city = input("Enter city name you wanna get statistics about:").lower()
        while city not in CITY_DATA.keys():
            city = input("Enter a valid input:").lower()
            return city
    except KeyboardInterrupt as error:
        system('clear')
        error.message = "you've quit the program.\nBye!"
        print(error.message)
        exit(0)


def get_month_user_input():
    """
    get User Input for one the month name
       Returns:
           (str) month name entered by user after validation
       """

    month_list = get_forward_month_list()
    month_list.insert(0, "All")
    try:
        month = input("Enter month name from Jan to Jun or type All to skip filtering:").title()
        month_flag = True
        while month_flag:
            if month in month_list:
                month_flag = False
            else:
                month = input("Enter a valid input").title()
        return month
    except KeyboardInterrupt as error:
        system('clear')
        error.message = "you've quit the program.\nBye!"
        print(error.message)
        exit(0)


def get_day_user_input():
    """
    get User Input for one the day name
           Returns:
               (str) day name entered by user after validation
           """
    days_list = get_forward_day_list()
    days_list.insert(0, "All")

    try:
        day_flag = True
        day = input("Enter a valid week day or type all to skip filtering").title()
        while day_flag:
            if day in days_list:
                day_flag = False
            else:
                day = input("Enter a valid input").title()
        return day

    except KeyboardInterrupt as error:
        system('clear')
        error.message = "you've quit the program.\nBye!"
        print(error.message)
        exit(0)


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    It only calls the 3 functions get {cit,month,day} user input.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bike share data!')

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
    df['Stations'] = df['Start Station'] + " " + df['End Station']
    df.columns = [c.replace(' ', '_') for c in df.columns]

    if month != "All":
        df = df[df.Month.eq(month)]
    if day != "All":
        df = df[df.Day.eq(day)]
    return df


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


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')

    start_time = time.time()

    # display most commonly used start station
    print(df.Start_Station.mode())

    # display most commonly used end station
    print(df.End_Station.mode())

    # display most frequent combination of start station and end station trip
    print(df.Stations.mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print(df.Trip_Duration.sum())
    print("time format ", str(timedelta(seconds=int(df.Trip_Duration.sum()))))

    # display mean travel time
    print(df.Trip_Duration.mean())
    print("time format ", str(timedelta(seconds=int(df.Trip_Duration.mean()))))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df.query('User_Type == "Subscriber"').User_Type.count())
    print(df.query('User_Type == "Customer"').User_Type.count())

    # Display counts of gender
    try:
        print(df.query('Gender == "Male"').Gender.count())
        print(df.query('Gender == "Female"').Gender.count())
    except Exception as error:
        error.message = "washington doesn't have gender classification\n "
        print(error.message)

    # Display earliest, most recent, and most common year of birth
    try:
        print(int(df.Birth_Year.min()))
        print(int(df.Birth_Year.max()))
        print(int(df.Birth_Year.mode()))
    except Exception as error:

        error.message = "washington doesn't have DOB "
        print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    """
    Asks if the user would like to see some lines of data from the filtered dataset.
    Displays 5 (show_rows) lines, then asks if they would like to see 5 more.
    Continues asking until they say stop.
    """
    try:
        start, end = 0, 4

        read_chunks = input('\n May you want to have a look on the raw data? Type yes or no').lower()

        while read_chunks == "y":
            print(df.loc[start:end, :])
            read_chunks = input('May you want to have a look on more raw data? Type yes or no').lower()
            start = end + 1
            end += 5
    except KeyboardInterrupt:
        print('Thank you.')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
