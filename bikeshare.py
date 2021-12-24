import time
import pandas as pd
import numpy as np

# Line comment for the Github project

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
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
            city_input = input("Enter a City (Chicago, New york city, Washington): " )
            if city_input.lower() not in CITY_DATA.keys():
                print("City not found.")
            else:
                break

    # TO DO: get user input for month (all, january, february, ... , june)
    month_x = {'january' : 1, 'february' : 2, 'march' : 3, 'april' : 4, 'may' : 5, 'june' : 6, 'all' : 'all'}
    while True:
        month_input = input("Choose Month to analyze (January - June, all): ")
        if month_input.lower() not in month_x.keys():
            print("Month not available.")
        else:
            break
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_x = ('monday','tuesday','wednesday','thursday','friday','saturday','sunday', 'all')
    while True:
        day_input = input("Choose a day (Sunday, Monday, ..., all): ")
        if day_input.lower() not in day_x:
            print("Please enter correct day.")
        else:
            break

    city = city_input.lower()
    month = month_input.lower()
    day = day_input.title()

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
    df = pd.read_csv(CITY_DATA[city.lower()])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.strftime("%A")

    # filter by month if applicable
    if month.lower() != 'all':
        # use the index of the months list to get the corresponding int
        # month = ['january', 'february', 'march', 'april', 'may', 'june']
        month_x = {'january' : 1, 'february' : 2, 'march' : 3, 'april' : 4, 'may' : 5, 'june' : 6}
    
        # filter by month to create the new dataframe
        df = df[df.month == month_x[month.lower()]]

    # filter by day of week if applicable
    if day.lower() != 'all':
        # filter by day of week to create the new dataframe
        df = df[df.day_of_week == day.title()]


    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    month_y = {1:'january', 2:'february', 3:'march', 4:'april', 5:'may', 6:'june'}
    print("{} is the most common month.\n".format(month_y[common_month].title()))

    # TO DO: display the most common day of week
    print("{} is the most common day.\n".format(df['day_of_week'].mode()[0]))


    # TO DO: display the most common start hour
    print("The {}th hour is the most common hour of the day.\n".format(df['Start Time'].dt.hour.mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("'{}' is the most commonly used start station.\n".format(df['Start Station'].mode()[0]))


    # TO DO: display most commonly used end station
    print("'{}' is the most commonly used end station.\n".format(df['End Station'].mode()[0]))


    # TO DO: display most frequent combination of start station and end station trip
    end_station = df['End Station'].copy()
    
    df['start_end'] = df['Start Station'].str.cat(end_station, sep = " -> ")

    print("'{}' is the most common trip.\n".format(df['start_end'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = round(df['Trip Duration'].sum()/(60 * 60), 2)
    
    print("Total travel time is {} hours.\n".format(total_travel_time))


    # TO DO: display mean travel time
    avg_travel_time = round(df['Trip Duration'].mean()/(60), 2)
    
    print("Average travel time is {} minutes.\n".format(avg_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    
    print("Breakdown on user type")
    print('-'*23)
    
    i = 0
    while i < len(user_types):
        print(user_types.index[i], "=", user_types[i], "\n")
        i = i + 1

    if 'Gender' in df:
            # TO DO: Display counts of gender
             gender_types = df['Gender'].value_counts()

             print("Gender Count")
             print('-'*12)
             
             i = 0
             
             while i < len(gender_types):
                 print(gender_types.index[i], "=", gender_types[i], "\n")
                 i = i + 1
                 
            # TO DO: Display earliest, most recent, and most common year of birth

             early = int(df['Birth Year'].min())
             late = int(df['Birth Year'].max())
             most = int(df['Birth Year'].mode())
             
             print("Facts about age")
             print('-'*15)
             
             print("The oldest person was born in {} \nThe youngest person was born in {} \nA lot of people were born in {}".format(early, late, most))
    else: 
        print('Gender and Year of Birth can\'t be calculated')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def more_data(df):
    st = 0
    more_data = input('\nWould you like to see more data? Enter yes or no.\n')
    while more_data.lower() == 'yes':
        df_slice = df.iloc[st: st+5]
        print(df_slice)
        st += 5
        more_data = input('\nWould you like to see moreeeeee data? Enter yes or   no.\n')
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        print("Showing information for {}, month set to '{}' and day set to '{}'".format(city.title(),month,day.lower()))

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        more_data(df)
         

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
