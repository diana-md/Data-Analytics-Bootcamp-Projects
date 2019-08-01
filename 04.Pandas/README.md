# Academy of Pi 
##### Description

In this project I used Pandas Python library to aggregate and analyze the district-wide standardized test results in order to help a school board make strategic decisions regarding future school budgets and priorities. 

##### Given Data

- every student’s math and reading score
- various information on the schools in the district 

##### Data frames created using Pandas

- **District Summary**: Created a high level snapshot (in table form) of the district's key metrics, including:
  - Total Schools
  - Total Students
  - Total Budget
  - Average Math Score
  - Average Reading Score
  - % Passing Math
  - % Passing Reading
  - Overall Passing Rate (Average of the above two)

- **School Summary**: Created an overview table that summarizes key metrics about each school, including:
  - School Name
  - School Type
  - Total Students
  - Total School Budget
  - Per Student Budget
  - Average Math Score
  - Average Reading Score
  - % Passing Math
  - % Passing Reading
  - Overall Passing Rate (Average of the above two)
  
 - **Top Performing Schools** (By Passing Rate): Created a table that highlights the top 5 performing schools based on Overall Passing Rate. Include:
    - School Name
    - School Type
    - Total Students
    - Total School Budget
    - Per Student Budget
    - Average Math Score
    - Average Reading Score
    - % Passing Math
    - % Passing Reading
    - Overall Passing Rate (Average of the above two)
  
- **Bottom Performing Schools** (By Passing Rate): Created a table that highlights the bottom 5 performing schools based on Overall Passing Rate. Include all of the same metrics as above.

- **Math Scores by Grade**: Created a table that lists the average Math Score for students of each grade level (9th, 10th, 11th, 12th) at each school.

- **Reading Scores by Grade**: Created a table that lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) at each school.

- **Scores by School Spending** : Created a table that breaks down school performances based on average Spending Ranges (Per Student). Used 4 reasonable bins to group school spending. Include in the table each of the following:
  - Average Math Score
  - Average Reading Score
  - % Passing Math
  - % Passing Reading
  - Overall Passing Rate (Average of the above two)

- **Scores by School Size** : Repeated the above breakdown, but this time schools were grouped based on a reasonable approximation of school size (Small, Medium, Large).

- **Scores by School Type** : Repeat the above breakdown, but this time schools were grouped based on school type (Charter vs. District).

Please see Jupyter notebook for analysis and findings. 
