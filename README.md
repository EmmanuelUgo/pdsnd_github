### Date created
23/12/2021

### Project Title
Bikeshare Project

### Description
This basic project is a requirement needed to obtain a certifcate in the Programming for Data Science course offered by Udacity. It is an interactive python project where the user has to pick a particular city and some descriptive statstical information would appear on screen. It is really a nice project to really understand the programming in python. Topics like data type, loops, error handling, function, methods and many others were fully covered during the course of this project.

### Files used
The following files were used;
- chicago.csv
- new_york_city.csv
- washington.csv

### Libraries Used  
The following libraries were used:
- numpy
- pandas
- time

### Functions Used
The following functions were created:
#### get_filter()
This prompts the user to type in a city, month and day of the week they would like to analyze. Error handling is really an important factor to consider when writing this function to account for case sensitive inputs (for example: Chicago, ChiCago, CHICAGO, e.t.c). Users can choose **all** for the month and day if the want every detail about the city.
#### load_data()
This function takes the inputs from the `get_filter()` function as filter the data based on that.
#### time_stats()
This tells information about the most common month, day and hour based on the information produced by the `load_data()` function.
#### station_stats()
This tells the most common start and end station and also it shows the most common trip (That is a combination of both the start and end trip)
#### trip_duration()
This tells some information about the trip people made
#### user_stats()
This shows us the year the oldest and young people was born and also the most popular year of birth for that period.
#### more_data()
It asks the user if they would like to see the raw data
#### main()
It couples the previous functions together to give it an interactive feel.

### Credits
1. https://stackoverflow.com/questions/52938818/how-to-display-increment-raw-data-using-iloc-depending-on-user-input

2. https://www.w3schools.com/python/python_conditions.asp

3. https://www.geeksforgeeks.org/python-pandas-series-str-cat-to-concatenate-string/

