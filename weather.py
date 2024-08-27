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
    # from datetime import datetime
 
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

    # working
    # number_of_days = len(load_data_from_csv("tests/data/example_one.csv"))
    formatted_list = []

    date = convert_date("tests/data/example_one.csv")
    print(date)

    minimum_temp = find_min
    maximum_temp = find_max




    lowest_temperature = find_min("min_temperature")
    # if type(weather_data) is str:
    #     float (lowest_temperature)
    

    print (lowest_temperature)

    # working
    #  print (f"{number_of_days} Day Overview")



    # print (f"The lowest temperature will be {lowest_temperature}")


# # Number of days - based on length of list

#     print (f"The lowest temperature will be {find_min_variable}°, and will occur on {corresponding_date}")
# # find_min returns temp + index
# # if nested list, index for li

#     print (f"The highest temperature will be {find_max_variable}°, and will occur on {corresponding_date}")
#     print (f"The average low this week is {average_low}°C")
#     print (f"The average high this week is {average_high}°C")




def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    

        
    print (convert_date("weather_data"))
        
