import time
import pandas as pd
import numpy as np
#creating a dictionary containing the data files for the three cities
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
print("Hello! Let's explore some US bikeshare data!")
#Getting user input to use as filters to display data 
#While loop is being used to get a valid user input for city, month, and day
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
#Creating an empty list for city to avoid it being referenced before being defined
#You will see this over and over again throughout the program
    city = ''
    while city not in CITY_DATA.keys():
        print("\nplease enter the city you want to see data for (chicago, new york city, or washington).")
        print("please enter the city name in full.")
        print("You can use either upper or lower case for your inputs in this program.")
#Using the lower() function to standardize user inputs
#You will see this occur throughout the program
        city = input().lower()     
        if city not in CITY_DATA.keys():
            print("\nSorry, I didn't understand that. Enter a valid city name.")
            print("\nTry again.")
#Returning user inputs to increase interactio
#You will continue to see this under the get_filters() function

            
    print("\nYou have selected {} as your city".format(city.title()))
#Creating a dictionary for available months
#Including 'all' for no filters
   
    MONTH_DATA = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 6, 'june': 6, 'all': 0}  
    month = ''
    while month not in MONTH_DATA:
        print("\nplease enter the month you want to see data for (january, february,....june) or enter 'all' to apply no filter")
        month = input().lower()      
        if month not in MONTH_DATA.keys():
            print("Sorry, I didn't understand that. Enter a valid month name or enter 'all' to apply no filter")
            print("try again")
    print("\n You have chosen month as {}".format(month.title()))
#Creating a list of available days
#Including 'all' for no filter
    DAYS = ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
   
    day = ''
    while day not in DAYS:

        day = input("\nplease enter the day you want to see data for (sunday, monday,....saturday) or enter 'all' to apply no filter.").lower()
        if day not in DAYS:
            print("Sorry, I didn't understand that. Enter a valid day name")
            print("try again")
    print("\n You have chosen day as {}".format(day.title()))
    print("\n You want to see data for city:{}, month(s):{}, day(s):{}".format(city.title(), month.title(), day.title()))
    print('-'*80)
#returning city, month and day    
    return city, month, day
          



 



#Defining a function to load data based on user inputs
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
    print("\nLoading your data now......")
#Getting the data frame from the source files    
    df = pd.read_csv(CITY_DATA[city])
#Converting 'Start Time' column to date_time format
    df['Start Time'] = pd.to_datetime(df['Start Time'])
#Extracting month from the converted 'Start Time' column    
    df['month'] = df['Start Time'].dt.month
#Extracting day    
    df['day_of_week'] = df['Start Time'].dt.weekday_name
#using an if statement to apply month filters
#Simlar thing applies to day filters
    
    if month != 'all':
        months = ['january','february','march','april','may','june']
#Using the index() method to get corresponding numbers for the months        
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
#Using title() method to ensure the input for day correspond with those in the source data files     
        df = df[df['day_of_week'] == day.title()]
#returning the data frame   
    return df    

#Defining function to calculate required statistics
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
#Asigning a variable to the present time. Employing time() method
#This will be used in calculating the time spent on generating the statistics
#You will see this occur throughout the program    
    start_time = time.time()
#Using mode() method to generate most popular month, day and hour    
    most_popular_month = df['month'].mode()[0]
    print("\nMost popular month of travel is {} (january = 1, february = 2,....june = 6)".format(most_popular_month))
    most_popular_day = df['day_of_week'].mode()[0]
    print("\nMost popular day of travel is {}".format(most_popular_day))
#Exrating hour from the converted 'Start time' column    
    df['hour'] = df['Start Time'].dt.hour
    most_popular_hour = df['hour'].mode()[0]
    print("\nMost popular hour of travel is {}".format(most_popular_hour))
    print("\nThis took {} seconds".format(time.time() - start_time))
    print('-'*40)











#Defining a function to calculate station related statistics
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
#Using mode() to get the most common start and end station 
#also to get the most common combination of start and end station


    most_common_start_station = df['Start Station'].mode()[0]
    print("Most common start station is {}".format(most_common_start_station))
    most_common_end_station = df['End Station'].mode()[0]
    print("\nMost common end station is {}".format(most_common_end_station))
#Using str.cat() to concatenate the start and end station
#Then using mode() to find the most common combination
    
    df['Start to End'] = df['Start Station'].str.cat(df['End Station'], sep = '-')
    most_common_match = df['Start to End'].mode()[0]
    print("\nMost common combination of start and end station trip is {}".format(most_common_match))
    print("\nThis took {} seconds".format(time.time() - start_time))
    print('-'*40)








#Defining function to generate trip duration related statistics
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
#Using sum() method to calculate the total travel time    
    total_travel_time = df['Trip Duration'].sum()
#Using divmod to convert the second to minute    
    minute, second = divmod(total_travel_time, 60)
#Converting minute to hour    
    hour, minute = divmod(minute, 60)

    print('The total trip duration is {} hour(s) {} minutes and {} seconds'.format(hour, minute, second)) 
#Using mean() method to calculate the mean travel time
#Using 'round' to round the figure off
   
    mean_travel_time = round(df['Trip Duration'].mean()) 
#Converting second to minute    
    mins, sec = divmod(mean_travel_time, 60)
#Using if statement to convert to hour    
    if mins > 60:
        hrs, mins = divmod(mins, 60)
        print("The average trip duration is {} hour(s), {} minutes, {} seconds".format(hrs, mins, sec))
    else:
        print("The average trip duration is {} minutes, {} seconds".format(mins, sec))           
    print("\nThis took {} seconds".format(time.time() - start_time))
    print('-'*40)          




#Defining function to calculate user statistics
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
#Using value_counts() to generate user type and gender counts    
    user_type_stats = df['User Type'].value_counts()
    print('\nThe stats of users are:\n\n {}'.format(user_type_stats))
#Using try and except to display gender and birth year info in cities where applicable    
    try:
        gender_stats = df['Gender'].value_counts()
        print("\nThe user stats by gender are\n\n{}".format(gender_stats))
    except:
        print("\nThere is no 'Gender' column in this file")
    try:
#Using min(), max(), and mode() to find earliest, latest and most common birth year respectively       
        earliest_birth_year = int(df['Birth Year'].min())
        latest_birth_year = int(df['Birth Year'].max())
        most_common_birth_year = int(df['Birth Year'].mode()[0])
        print("\nThe earliest birth year is {}.\n\nThe latest birth year is {}.\n\nThe most common birth year is {}".format(earliest_birth_year, latest_birth_year, most_common_birth_year))
    except:
        print("\nThere are no birth year info in this file.")
    print("\nThis took {} seconds".format(time.time() - start_time))
    print('-'*40)
    
    
#Defining function to display raw data to the user    
def display_data(df):
#Creating a list of possible responses    
    possible_response = ['yes','no']
    raw_data = ''
#Setting a variable 'counter' to zero to track the number of raw data displayed at once    
    counter = 0
#Using a while loop to get valid user input    
    while raw_data not in possible_response:
        print("\nDo you want to view the raw data?")
        print("\nEnter 'yes' or 'no'.")
#Getting user response to view raw data or not        
        raw_data = input().lower()
#Using if statement to display raw data to user    
        if raw_data == 'yes':
            
            print(df.head())
        elif raw_data not in possible_response:
            
            print("\nSorry, I didn't understand that.\nEnter a valid input.")
            print("\nTry again....")
#Emloying another while loop to display more rows of raw data            
    while raw_data == 'yes':
        print("\nDo you want to view more raw data?")
        print("\nEnter 'yes' or 'no'.")
        counter += 5
        raw_data = input().lower()
        if raw_data == 'yes':
            print(df[counter:counter+5])
        elif raw_data != 'yes':
            break
    print('-'*40) 







#Defining a main function that calls all other functions in the program
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
          
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

#Getting user input to restart or not        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
	
