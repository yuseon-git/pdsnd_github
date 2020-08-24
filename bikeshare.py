import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

Month_list= ['january', 'february', 'march', 'april', 'may', 'june', 'all']
Day_list= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city = str(input("Which city would you like to explore? Choose one from Chicago, New York City and Washington:")).lower()
    while city not in CITY_DATA:
        city = str(input("Oops, that\'s not a valid city name. Choose one from Chicago, New York City and Washington:")).lower()
                  
            
    # TO DO: get user input for month (all, january, february, ... , june)
    month = str(input("\nGive us a name of the months from January to June that you want to look up. Or type \"all\" for all 6 months of a year:")).lower()
    while month not in Month_list:
        month = str(input("Oops, that\'s not a valid month name. Give us a name of the months from January to June or just type type \"all\":")).lower()
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = str(input("\nGive us a name of the days (eg.Saturday) that you want to look up. Or type \"all\" for all days of a week:")).title()      
    while day not in Day_list: 
        day = str(input("Oops, that\'s not a valid day name. Give us a name of the days eg.Saturday that you want to look up. Or type \"all\" for all   days of a week:")) 
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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
                   
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month =  months.index(month)+1          
        df = df[df['month'] == month]   
                   
    if day != 'All':
        df = df[df['day_of_week'] == day.title()]      
                   
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month             
    popular_month = df['month'].mode()[0]

    print ("Guess what? The most popular month in integer (eg. January = 1) is", popular_month,".")
                   
    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day = df['day_of_week'].mode()[0]              
    print ("Guess what? The most popular day is", popular_day,".")
                   
    # TO DO: display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    popular_start_hour = df['start_hour'].mode()[0]
    print ("Guess what? The most popular start hour is", popular_start_hour,".")               
                   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("The most popular start station is ", popular_start_station, ".")
                   
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("And the most popular end station is ", popular_end_station, ".")

    # TO DO: display most frequent combination of start station and end station trip
    df['startendcombi'] = "from "+ df['Start Station'] +" to "+ df['End Station']
    popular_start_end_combi = df['startendcombi'].mode()[0]
    print("\nFinally, the most popular trip based on start station and end station is", popular_start_end_combi,".")
                   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_seconds = df['Trip Duration'].sum()
    total_travel_time = time.strftime("%H:%M:%S", time.gmtime(total_seconds))
                   
    print ("The total travel time has been ",total_travel_time, " (HH:MM:SS).")

    # TO DO: display mean travel time
    mean_seconds = df['Trip Duration'].mean()
    mean_travel_time = time.strftime("%H:%M:%S", time.gmtime(mean_seconds))
    
    print ("The mean travel time is ",mean_travel_time, " (HH:MM:SS).")
                                      
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def rawdata(df):
    
    view_rawdata = input('\nWe hope you enjoyed it so far. Would you like to see the actual raw data? We can show you 5 lines of them. Enter yes or no.\n')
    if view_rawdata.lower() != 'yes':
        print ("Alright! Let\'s move to the next stage then!")
        
    else: 
        print(df.head(5))
        
        view_rawdata_again = input ("Do you want to check the next five lines of the raw data? Enter yes or no.\n")
        if view_rawdata_again.lower() != 'yes':
            print ("Alright! Let\'s move to the next stage then!") 
        else: 
            n=1
            while 5*n+5 <= int(len(df.index)):
                print(df.iloc[5*n:5*n+5])
                n +=1
                view_rawdata_again = input ("Do you want to check the next five lines of the raw data? Enter yes or no.\n")
                if view_rawdata_again.lower() != 'yes':
                    break
    

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print ("Here are the total numbers of each user type:\n",user_type_counts)
    print ("\nAttention: users who did not identify user types were excluded from counting.\n")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats2(df):     
    
    print('\nCalculating more detailed User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of gender
  
    gender_counts = df['Gender'].value_counts()
    print ("Here are the counts for the genders of the users:\n",gender_counts)
    print ("Attention: users who did not identify genders were excluded from counting.\n")
                   
    # TO DO: Display earliest, most recent, and most common year of birth
    
    earliest= df['Birth Year'].min()
    most_recent= df['Birth Year'].max()
    most_common= df['Birth Year'].mode()[0]
   
    print ("Our oldest users were born in ", int(earliest), ", the youngest were born in ", int(most_recent), ". The most frequent year of birth among our users is", int(most_common), ".\n")                
    print ("Attention: users who did not identify birth years were excluded from counting.\n")
                   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        try:
            city, month, day = get_filters()
            df = load_data(city, month, day)

            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)   
            rawdata(df)
                        
            detail = input('\nWould you like to see more detailed data on our users? Enter yes or no.\n')
            if detail.lower() != 'yes':
                break
            else: 
                user_stats(df)
                if city != 'washington': 
                    user_stats2(df)
        
                restart = input('\nWould you like to restart? Enter yes or no.\n')
                if restart.lower() != 'yes':
                    break                        
                  
        except KeyError:
            print("Sorry, something wrong in your inputs. Can you start over again, please?")
                            
if __name__ == "__main__":
	main()
