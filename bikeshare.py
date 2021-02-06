import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

print('Hello! Let\'s explore some US bikeshare data!')


def get_filters():
    cities = ['chicago', 'new york city', 'washington']
    Months = ['all', 'jan', 'feb', 'mar', 'apr', 'may', 'jun']
    Days = ['all', 'sat', 'sun', 'mon', 'tue', 'wed', 'thu', 'fri']

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input(
        'Would you like to see the data for the following Cities?\n Choose from the list [chicago, new york city, washington] ').lower()
    if city in cities:
        print(f' Your choice is:  >>> {city}')
    while city not in cities:
        print(input('Wrong Choice, Please Try again....'))
        city = input(
            'Please choose correctly from the list:\n[chicago, new york city, washington] ').lower()

    # get user input for month (all, january, february, ... , june)
    month = input(
        'Which month? choose from the list\n[all, jan, feb, mar, apr, may, jun] ').lower()
    if month in Months:
        print(f' Your choice is:  >>> {month}')
    while month not in Months:
        print(input('Wrong Choice, Please Try again....'))
        month = input(
            'Please choose correctly from the list:\n[all, jan, feb, mar, apr, may, jun] ').lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input(
        'Which Day? choose day from the list:\n[all, sat, sun, mon, tue, wed, thu, fri] ').lower()
    if day in Days:
        print(f' Your choice is:  >>> {day}')
    while day not in Days:
        print(input('Wrong Choice, Please Try again....'))
        day = input(
            'Please choose from the list:\n[all, sat, sun, mon, tue, wed, thu, fri] ').lower()

    print('#' * 40)
    return city, month, day


def load_data(city, month, day):

    df = pd.read_csv(CITY_DATA[city])
    # Convert date from str to date time:
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # Extarct month from Date:
    df['month'] = df['Start Time'].dt.month
    # Extarct Days from Date:
    df['day_name'] = df['Start Time'].dt.day_name()
    # Extract hours from Date:
    df['hour'] = df['Start Time'].dt.hour
    # Filterate Month and Day:
    if month != 'all':
        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']
        month = months.index(month)+1
        df = df[df['month'] == month]

    elif day != 'all':
        df = df[df['day_name'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month:
    print('Most common Month: {}'.format(df['month'].mode()[0]))

    # display the most common day of week
    print('Most common day is: {}'.format(df['day_name'].mode()[0]))

    # display the most common start hour
    print('Most common Hour is: {}'.format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Most common used Start Station is: {}'.format(
        df['Start Station'].mode()[0]))

    # display most commonly used end station
    print('Most common used End Station is: {}'.format(
        df['End Station'].mode()[0]))

    # display most frequent combination of start station and end station trip

    df['freq_combination'] = df['Start Station'] + ' To: ' + df['End Station']
    print('Most frequent combination of Start Station & End Station\nFrom: {}'.format(
        df['freq_combination'].value_counts().tail(1)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time is : {}'.format(df['Trip Duration'].sum()))

    # display mean travel time
    print('Avarage travel Time is: {}'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df['User Type'].value_counts())

    # Display counts of gender
    if city != 'washington':
        print(df['Gender'].value_counts())

        # Display earliest, most recent, and most common year of birth
        print('The Most recent year: {}'.format(int(df['Birth Year'].max())))
        print('The Earliest year: {}'.format(int(df['Birth Year'].min())))
        print('The Most common year of birth: {}'.format(
            int(df['Birth Year'].mode()[0])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def Display_raw_data(df):
    """Displays raw data for the data set."""
    raw_data = input(
        'Would you like to show some random samples of raw data?? yes/no ')
    start_loc = 0
    while raw_data == 'yes':
        print(df.iloc[start_loc : start_loc + 5 , : ])
        start_loc += 5
        raw_data = input('Would you like to show more?? yes/no')
        while raw_data == 'no':
            break

    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        Display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
