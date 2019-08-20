# Prospecting_Location_For_New_Business

This application helps businesses in the auto and dry cleanign industry to visualize the denstity of similar businesses in Canada. It could potentially be used to help business owners choose a location for their new business in areas that are not saturated.

This project demostrates the ability to perform ETL (Extract Transform Load). The tools used were Jupyter Notebooks and different Python libraries such as requests, pandas, json, sqlalchemy.

Steps that were taken:
1. Extract:
  - We scraped Top 100 Largest Population Cities from [Wikipedia](https://en.wikipedia.org/wiki/List_of_the_100_largest_population_centres_in_Canada). We used pandas.read_html() function to scrape the table containing information about the cities.
  - For each city, we used the [Yelp API](https://www.yelp.com/developers/documentation/v3) and made requests to find the latitude and longitude for 50 businesses in the city. We used to requests python library to access the API and the json python library to read the api response.  


Our initial proposal is [here](https://docs.google.com/document/d/1eQVnBs8iHBTcIBRyi2aOYskhF_fh90I5vC6YzCPAb3Y/edit?usp=sharing).

2. Transformation:

  Web Scraping
  - For the web scraping of the Wikipedia, we captured the table of interest then we renamed the columns of the data frame, the initial scrape returned numbers instead of column names.
Additionally, we iloc on rows number 1 and above since the column names from the table in the web were all showing in row 0.
  - The next bit of cleanup involved dropping columns that had population totals per city for the previous years. Our aim was to show the most current population totals.
  - To provide an additional set of data in a new column we had to convert values in the columns “Land area(km2, 2011)” and "Population(2016)" from string to numeric values. Those two columns came in with string values after our web scrape. With the values converted we were able to create a “Population_Density_km2” column by dividing the “Land area(km2, 2011)”into "Population(2016)" column.
  - With all our information now stored in a Panda data frame we created an SQL lite databased and converted the data frame in to a table.

  API Calls
  - After completing API calls to YELP we transformed our responses in to a Pandas data frame. To create our Pandas data frame we first created a dictionary naming keys that would hold the data from the json that we wanted to collect.
  - We explored the Jason to identify the location of the values we needed.
  - Then the values for the dictionary were appended by looping through the json. 
  - Once our loop was finished our dictionary had all the values we needed. We converted the dictionary in to a Pandas data frame.
  - The data frame was then  transformed in to a table and stored in an SQL lite data frame.


3. Load:

  - For the load part of the project we prepared the data by getting in to Pandas data frames, these made it simple to load each data frame as a table in to a SQL lite database.
  - Given the nature of the data we collected loading it in to a structured database made sense.  With this database we can now obtain answer to queries using simple code, we are able to join the two tables to provide a more complete answers to future user’s queries. 

