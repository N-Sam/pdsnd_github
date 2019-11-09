import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
   
    print('Hello! Let\'s explore some US bikeshare data!')
    print("")

    print('pleas enter the city name to explore its bike share data, Make your choice from [chicago, new york city, washington] !')
    city_names = ['chicago','new york city','washington']
    user_choice = str(input()).lower()
    print("")
    try:
        while True:
            if user_choice not in city_names:
                print("Please chose the city names in this list [chicago, new york city, washington]")
                user_choice = str(input()).lower()
            else:
                print("Thanks you have chosen to explore {} bike share data".format(user_choice))
                city = user_choice
                break
        else:
            print("Sorry your choice is not in the list")
    except Exception as e:
        print("Exception ".format(e))

    print("")
    print('Please enter the month name of your interest to explore, Enter all to see for all month in range')
    months = ['january', 'february','march','april','may','june','all']
    user_choice_month = str(input()).lower()
    print("") #printing blank space
    try:
        while True:
            if user_choice_month not in months:
                print("Please provide a valid month chose from these options [january, february,march,april,may,june,all] ")
                user_choice_month = str(input()).lower()
            else:
                print("Thanks your month of interest was {} ".format(user_choice_month))
                month = user_choice_month
                break
        else:
            print(" There is no data for that month ")

    except Exception as e:
        print("Exception: ".format(e))

    print("") #printing blank space
    print("Enter a particular day of the week of your interest Or all, to see for all days ")
    days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
    user_choice_day = str(input()).lower()
    print("") #printing blank space
    try:
        while True:
            if user_choice_day not in days:
                print("Please enter a valid week day or all")
                user_choice_day = str(input()).lower()
            else:
                print("Yor have chosen {} as your day of interest".format(user_choice_day))
                day = user_choice_day
                break
        else:
            print("Day choice not valid check spellings!")

    except Exception as e:
        print("Exception: ".format(e))
   
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time']) #coverting string dates to datetime format

    df['month'] = df['Start Time'].dt.month #extracting month from start time and creating column month
    df['week_day'] = df['Start Time'].dt.weekday_name # extracting weekday and creating column week_daycleary

    if month != 'all':
        months = ['january', 'february','march','april','may','june']
        month = months.index(month)+1 #creating corespondence in month index to its numeric value/order of occurrence
        df = df[df['month']== month] #filtering by user prefered month

    if day != 'all':

        df = df[df['week_day']== day.title()] #filtering by user prefered day

    user_confirmation = input("\n Do you want to see some raw data ? Enter Yes or No \n") # asking for user confimation to see data
    n = 5

    if user_confirmation.lower() == 'yes':
        print(df.head())
        while True:
            user_confirmation = input("\n Do you want to see more  row? Enter yes or no \n")
            if user_confirmation.lower() == 'yes':
                n += 5
                print(df.head(n))
            else:
                break

    return df


def time_stats(df):
   
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    most_common_month = df['month'].mode()[0]
    #converting month index to coresponding month name
    if most_common_month == 1:
        most_common_month = 'January'
        print("The most common month is {}".format(most_common_month))
    if most_common_month == 2:
        most_common_month = 'February'
        print("The most common month is {}".format(most_common_month))
    if most_common_month == 3:
        most_common_month = 'March'
        print("The most common month is {}".format(most_common_month))
    if most_common_month == 4:
        most_common_month = 'April'
        print("The most common month is {}".format(most_common_month))
    if most_common_month == 5:
        most_common_month = 'May'
        print("The most common month is {}".format(most_common_month))
    if most_common_month == 6:
        most_common_month = 'June'
        print("The most common month is {}".format(most_common_month))


    most_common_day_of_week = df['week_day'].mode()[0]
    print("The most common day of week is {}".format(most_common_day_of_week))


    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print("The most common hour is {}".format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()


    most_common_start_station = df['Start Station'].mode()[0]
    print("The most common start station is {}".format(most_common_start_station))


    most_common_end_station = df['End Station'].mode()[0]
    print("The most common end station is {}".format(most_common_end_station))


    df['most_common_route_comination'] = df['Start Station']+" "+ df['End Station']
    most_common_route_combination = df['most_common_route_comination'].mode()[0]
    print("The most common route combination is {}".format(most_common_route_combination))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
   
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time was {}".format(total_travel_time))


    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is {}".format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()


    user_type_count = df['User Type'].value_counts()
    print(user_type_count)


    gender_count = df['Gender'].value_counts()
    print(gender_count)


    earliest = df['Birth Year'].min()
    print("The earliest year of birth is {}".format(earliest))
    print("")
    most_recent = df['Birth Year'].max()
    print("The most recent year of birth is {}".format(most_recent))
    print("")
    most_common = df['Birth Year'].mode()[0]
    print("The most common year of birth is {}".format(most_common))
    print("")
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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
