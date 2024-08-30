import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"

# PASS

def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
 
    time = datetime.fromisoformat(iso_string)
    return(time.strftime("%A %d %B %Y"))

# PASS


def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    
    temp_in_celsius = ((float(temp_in_fahrenheit) - 32) * 5 / 9)
    temp_in_celsius_rounded = round(temp_in_celsius, 1)

    return temp_in_celsius_rounded
    
# PASS

def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    sum_weather = 0
    
    for item in weather_data:
        if type(item) is str:
            sum_weather += float(item)
        else:
            sum_weather += item

    len_weather = len(weather_data)
    mean = sum_weather / len_weather
    return mean

  # PASS  

def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

        Args:
            csv_file: a string representing the file path to a csv file.
        Returns:
            A list of lists, where each sublist is a (non-empty) line in the csv file.
    """

    weather_list = []

    with open(csv_file) as csv_file:
        reader = csv.reader(csv_file)
        next(reader) #skip headers (first row)
        
        for row in reader:
            if row:
                date = row[0]
                minimum_temp = float(row[1])
                maximum_temp = float(row[2])


                converted_list = [date, minimum_temp, maximum_temp]
                weather_list.append(converted_list)

        return weather_list

    # PASS


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """

    for index, temperature in enumerate(weather_data):

        if weather_data:

            for index, min_temperature in enumerate(weather_data):
                min_temperature = min(weather_data)
                min_index_number = len(weather_data) - 1
                reverse_weather_data = weather_data[::-1]
                min_index_reverse = reverse_weather_data.index(min_temperature)
                min_index = min_index_number - min_index_reverse
                return float(min_temperature), (min_index)
            
    else:
        return()


        

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
   
    if weather_data:
        max_temp = max(weather_data)
        max_index_number = len(weather_data) - 1
        reverse_weather_data = weather_data[::-1]
        max_index_reverse = reverse_weather_data.index(max_temp)
        max_index = max_index_number - max_index_reverse
        return float(max_temp), (max_index)

    else:  
        return()

    

def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    # Number of days in overview
    number_of_days = len(weather_data)
    
    # Minimum teperature and day/date
    min_temp_list = []

    for item in weather_data:
        minimum_temperature = item[1]
        min_temp_list.append(minimum_temperature)

    if minimum_temperature:
        summary_min_temp = (find_min(min_temp_list)[0])

    min_temp_in_c = convert_f_to_c(summary_min_temp)

    for item in weather_data:
        day = item[0]
        minimum_temperature = item[1]
        if summary_min_temp == minimum_temperature:
            matched_day = day

    minimum_temp_day = convert_date(matched_day)


 # Maximum teperature and day/date 
    max_temp_list = []

    for item in weather_data:
        maximum_temperature = item[2]
        max_temp_list.append(maximum_temperature)

    if maximum_temperature:
        summary_max_temp = (find_max(max_temp_list)[0])

    max_temp_in_c = convert_f_to_c(summary_max_temp)

    for item in weather_data:
        day = item[0]
        maximum_temperature = item[2]
        if summary_max_temp == maximum_temperature:
            matched_day = day
       
    maximum_temp_day = convert_date(matched_day)
   

# Average weekly low
    average_minimum_list = []

    for item in weather_data:
        minimum_temperature = item[1]
        average_minimum_list.append(minimum_temperature)
   
    if minimum_temperature:
        average_low = (calculate_mean(average_minimum_list))

    mean_min_temp_in_c = convert_f_to_c(average_low)

 

# Average weekly high
    average_maximum_list = []

    for item in weather_data:
        maximum_temperature = item[2]
        average_maximum_list.append(maximum_temperature)
   
    if maximum_temperature:
        average_high = (calculate_mean(average_maximum_list))

    mean_max_temp_in_c = convert_f_to_c(average_high)

    # Summary text
    day_overview = (f"{number_of_days} Day Overview")
    day_low_overview = (f"  The lowest temperature will be {min_temp_in_c}{DEGREE_SYMBOL}, and will occur on {minimum_temp_day}.")
    day_high_overview = (f"  The highest temperature will be {max_temp_in_c}{DEGREE_SYMBOL}, and will occur on {maximum_temp_day}.")
    average_low_overview = (f"  The average low this week is {mean_min_temp_in_c}{DEGREE_SYMBOL}.")
    average_high_overview = (f"  The average high this week is {mean_max_temp_in_c}{DEGREE_SYMBOL}.")

    return (day_overview + '\n' + day_low_overview + '\n' + day_high_overview + '\n' + average_low_overview + '\n' + average_high_overview + '\n')



def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    daily_summary_output = ""

    for item in weather_data:
        iso_date = item[0]
        day = convert_date(iso_date)

        minimum_temp = item[1]
        minimum_temp_in_c = convert_f_to_c(minimum_temp)
        daily_minimum_temp = f"{minimum_temp_in_c}{DEGREE_SYMBOL}"

        maximum_temp = item[2]
        maximum_temp_in_c = convert_f_to_c(maximum_temp)
        daily_maximum_temp = f"{maximum_temp_in_c}{DEGREE_SYMBOL}"

        daily_summary = (f"---- {day} ----")
        min_temp_day_summary = (f"  Minimum Temperature: {daily_minimum_temp}")
        max_temp_day_summary = (f"  Maximum Temperature: {daily_maximum_temp}")

        daily_summary_output = daily_summary_output + daily_summary + '\n' + min_temp_day_summary + '\n' + max_temp_day_summary + '\n\n'
    
    return daily_summary_output


        

    

        
    
        
