
![Divvy bikeshare](https://user-images.githubusercontent.com/103776681/169701283-31863917-0778-4933-a262-d2a80732e068.png)
# DIVVY BIKESHARE

The title of this project is _DIVVY BIKESHARE PROJECT_. It was created April 11, 2022. This README.md file was created April 22, 2022. This project is actually one the projects I wrote under the **Acces Bank**-sponsored _data analysis nanodegree_ course on [udacity](https://www.udacity.com/). Divvy is a bike sharing system in the US that allows users to rent bicycles for travel and return to other stations near their destinations or to the start stations, if they were going for just a ride. There is a dock system in each bicycle that allows a user to unlock and return it. Click [here](https://en.wikipedia.org/wiki/Divvy) to learn more about Divvy bike share system.


## Description
This project explores data for three cities in the US: 
- Chicago 
- New York City 
- Washington, DC 

This project is a python program that answers interesting questions about the Divvy US bike sharing system:

### Popular times of travel (i.e., occurs most often in the start time)

- most common month
- most common day of week
- most common hour of day

### Popular stations and trip

- most common start station
- most common end station
- most common trip from start to end (i.e., most frequent combination of start station and end station)

### Trip duration

- total travel time
- average travel time

### User info

- counts of each user type
- counts of each gender (only available for NYC and Chicago)
- earliest, most recent, most common year of birth (only available for NYC and Chicago)

It gets valid user inputs and uses them as filters for city, month, and day, to display information and statistics about the bikeshare system. It also displays raw data to the user, if interested.

### Results

| cities | most popular month | most popular day | most popular hour |
| ------ | ------ | ------ | ------ |
| chicago | 6 | Tuesday | 17 |
| new york city | 6 | Wednesday | 17 |
| washington | 6 | Wednesday | 8 |


| cities | most common start station | most common end station | most common combination of start and end station |
| ------ | ------ | ------ | ------ |
| chicago | Streeter Dr & Grand Ave | Streeter Dr & Grand Ave | Lake Shore Dr & Monroe St-Streeter Dr & Grand Ave |
| new york city | Pershing Square North | Pershing Square North | E 7 St & Avenue A-Cooper Square & E 7 St |
| washington | Columbus Circle / Union Station | Columbus Circle / Union Station | Jefferson Dr & 14th St SW-Jefferson Dr & 14th St SW |


| cities | mean travel time | total travel time |
| ------ | ------ | ------ |
| chicago | 78019 hours 56 minutes 27 seconds | 936 |
| new york city | 74973 hours 40 minutes 48 seconds | 900 |
| washington | 103106 hours 39 minutes 45 seconds | 1237 |


| cities | user type stats | gender stats | earliest birth year | latest birth year | most common birth year |
| ------ | ------ | ------ | ------ | ------ | ------ |
| chicago | Subscriber    238889  Customer       61110  Dependent          1 | Male      181190  Female     57758 | 1899 | 2016 |1989 |
| new york city | Subscriber    269149  Customer       30159 | Male      204008  Female     66783 | 1885 | 2001 | 1989 |
| washington | Subscriber    220786  Customer       79214 | Nil | Nil | Nil | Nil |


## Files used
The data used for this project is provided by [Motivate](https://www.motivateco.com/). The files used can be found in the [.gitignore](https://github.com/ndoladimeji/pdsnd_github/blob/44ad803be3153b09f507c7ca74e0563d56a30d3f/.gitignore) file. Visit [Chicago](https://www.divvybikes.com/system-data), [New York City](https://www.citibikenyc.com/system-data), [Washington](https://www.capitalbikeshare.com/system-data) to see the raw data.


## Contributors
List of contributors can be found [here](https://github.com/ndoladimeji/bikeshare_project/settings/access).


## Credits
Some of the resource sites consulted include: 
- [geeksforgeeks](https://www.geeksforgeeks.org/taking-input-in-python/amp/)
- [knowledgehut](https://www.knowledgehut.com/blog/programming/run-python-scripts)
- [stackoverflow](https://stackoverflow.com/questions/1016814/what-to-do-with-unexpected-indent-in-python)
- [stackoverflow](https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response)
- [arrowhitech](https://www.arrowhitech.com/typeerror-nonetype-object-is-not-iterable/)
- [smallbusiness.chron](https://smallbusiness.chron.com/making-raw-input-lowercase-python-31840.html)
- [learnandlearn](https://learnandlearn.com/python-programming/python-reference/find-calculate-mode-python-using-mode-function)
- [stackoverflow](https://stackoverflow.com/questions/63229237/finding-the-most-frequent-combination-in-dataframe)
- [marsja.se](https://www.marsja.se/pandas-count-occurrences-in-column-unique-values/)



