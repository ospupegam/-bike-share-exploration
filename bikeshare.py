# Reference:
# https://www.hackerearth.com/practice/python/getting-started/input-and-output/tutorial/
# https://www.datacamp.com/community/tutorials/exception-handling-python
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
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
    cit = ('chicago', 'new york city', 'washington')
    while True:
        try:
            city = input('Would you like to see data for : chicago, new york city, washington ? \n> ').lower()
            if city in cit:
                break
        except KeyboardInterrupt:
            print ('Caught KeyboardInterrupt')
        else: 
            print('Sorry, Enter Correctly as from list ')
    
    # TO DO: get user input for month (all, january, february, ... , june
    while True:
        try:
            month = input(' Which month : January, February, March, April, May, or June? \n> {} \n>'.format(months)).lower()
            if month in months:
                break
        except KeyboardInterrupt:
            print ('Caught KeyboardInterrupt')
        else: 
            print('Sorry, Enter Correctly as from list ')
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? \n> {} \n>'.format(days)).lower()
            if day in days:
                break
        except KeyboardInterrupt:
            print ('Caught KeyboardInterrupt')
        else: 
            print('Sorry, Enter Correctly as from list ')
    
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
    city=str(city) 
    df = pd.read_csv(CITY_DATA[city])
    # TO DO: load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # TO DO:convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # TO DO:extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    # TO DO:filter by month if applicable
    if month != 'all':
        # TO DO: use the index of the months list to get the corresponding int
        month = months.index(month) + 1
    
        # TO DO:filter by month to create the new dataframe
        df = df[df['month'] == month]
        
    # TO DO:filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df =  df[df['day_of_week'] == day.title()]
        

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df.month.mode()[0]
    print('Most Popular Start Month:', popular_month)
    
    # TO DO: display the most common day of week
    popular_day = df.day_of_week.mode()[0]
    print('Most Popular Start Day:', popular_day)
    
    # TO DO: display the most common start hour
    popular_hour = df.hour.mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
    commonly_start_station= df['Start Station'].mode()[0]
    
    # TO DO: display most commonly used end station
    commonly_end_station= df['End Station'].mode()[0]
    
    # TO DO: display most frequent combination of start station and end station trip
    print('< Most Commonly Start Station : {}>\n< Most Commonly End Station :{}> \n'.format(commonly_start_station,commonly_end_station))
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(' < Total Travel Time : {} > \n'.format(total_travel_time))
    
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(' < Mean Travel Time : {} > \n'.format(mean_travel_time))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    count_user_types = df['User Type'].value_counts()
    print(' < Counts of user Types : {} > \n'.format(count_user_types))
    try:
        # TO DO: Display counts of gender
        count_gender = df['Gender'].value_counts()
        print(' < Counts of Gender : {} > \n'.format(count_gender))
        
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]
  
        print(' < Earliest Year Birth : {} > \n < Most Recent Year Birth : {} > \n < Most Common Year Birth : {} > \n '.format(earliest_year,most_recent_year,most_common_year))
    
    except KeyError:
        print ('no Gender')
    else:
               print('Sorry , there is no Gender column.')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Displays 5 rows of data to users."""
    while True:
        try:
            view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
            if view_data == 'yes':
                break
        except KeyboardInterrupt:
            print ('Caught KeyboardInterrupt')
        else: 
            print('Sorry, Enter Correctly as from list ')
    start_loc = 0
    if view_data != 'yes':
        return
    else:
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_display = input('Do you wish to continue?: Enter yes or no\n').lower()   
        if view_display != 'yes':
            return
        else:
            print(df.iloc[start_loc:start_loc+5])

    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        


if __name__ == "__main__":
	main()
