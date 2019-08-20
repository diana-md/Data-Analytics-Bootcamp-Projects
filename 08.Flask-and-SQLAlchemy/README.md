In this project I used Python SQLAlchemy to analyze and perform data exploration of a .sqlite file containing climate data in Hawaii Islands and I created a Flask API to return the findings. 

SQLAlchemy was used to connet to the .sqlite file and to reflect the tables in the database into Python classes. 

##### Precipitation Analysis 
In order to perform Precipitation Analysis, the following steps were taken:
- Designed a query to retrieve the last 12 months of precipitation data.
- Selected only the date and prcp values.
- Loaded the query results into a Pandas DataFrame and set the index to the date column.
- Sorted the DataFrame values by date.
- Plotted the results using the DataFrame plot method.
- Use Pandas to print the summary statistics for the precipitation data.

![](Media/precipitation.png)

##### Station Analysis 
In order to perform Station Analysis, the following steps were taken:
- Designed a query to calculate the total number of stations.
- Designed a query to find the most active stations by:
- Listing the stations and observation counts in descending order.
- Finding the station having the highest number of observations
- Designed a query to retrieve the last 12 months of temperature observation data (tobs) by:
- Filtering by the station with the highest number of observations.
- Plotting the results as a histogram with bins=12.

![](station-histogram.png)

##### Flask Application

I used Python and Flask to build an API to easily access the results found by querying the data. The following routes were created:

```/```
- Home page.
- Listed all routes that are available.

```/api/v1.0/precipitation```

- Converted the query results to a Dictionary using date as the key and prcp as the value.
- Returned the JSON representation of your dictionary.

```/api/v1.0/stations```
- Returned a JSON list of stations from the dataset.

```/api/v1.0/tobs```
- queried for the dates and temperature observations from a year from the last data point.
- Returned a JSON list of Temperature Observations (tobs) for the previous year.

```/api/v1.0/<start> and /api/v1.0/<start>/<end>```
- Returned a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
- When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
- When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
