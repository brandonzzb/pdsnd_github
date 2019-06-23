# Udacity Programming for Data Science Nanodegree Project 2
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = str(input('Which city would you like to explore, Chicago, New York, or Washington?\n')).lower()
            if city in ['chicago', 'new york', 'washington']:
                break
            else:
                print('Sorry, that\'s not a valid input! Please choose from the three cities of Chicago, New York, or Washington.\n')
        except:
            print('Sorry, please check your input.\n')
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('Which month of data would you like to see, January, February, March, April, May or June? Or if you do not want to filter by any month, please type "All".\n').lower()
            if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
                break
            else:
                print('Sorry, that\'s not a valid input! Please choose from the six months mentioned, or you can choose All.\n')
        except:
            print('Sorry, please check your input.\n')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('\nGreat! Then which day of the week of data would you like to explore, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, or Saturday? Or if you do not want to filter by any day, please type "All".\n').lower()
            if day in ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:
                break
            else:
                print('Sorry, that\'s not a valid input! Please enter one day of week, or you can enter All.\n')
        except:
            print('Sorry, please check your input.\n')

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week, and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()
    print('Most Popular Month:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()
    print('Most Popular Day of Week:', popular_day)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()
    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()
    print('Most Frequent Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()
    print('Most Frequent End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print('Most frequent combination of Start Station and End Station:', popular_start_end_station[0], '&', popular_start_end_station[1])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: ', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Count of user types: ', user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print('Count of genders: ', gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        oldest_birth = df['Birth Year'].min()
        print('Earliest year of birth: ', oldest_birth)

        youngest_birth = df['Birth Year'].max()
        print('Most recent year of birth: ', youngest_birth)

        common_year_birth = df['Birth Year'].mode()
        print('Most common year of birth: ', common_year_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        # ask if users want to see five rows of data display
        user_input = input('\nWould you like to see five rows of data?\nPlease enter Yes or No:\n').lower()
        if user_input in ('yes', 'y'):
            i = 0
            while True:
                print(df.iloc[i:i+5])
                i += 5
                more_data = input('Would you like to see more data? Please enter Yes or No:\n').lower()
                if more_data not in ('yes', 'y'):
                    break
        #ask if users want to restart the query
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
