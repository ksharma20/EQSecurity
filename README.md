# EQSecurity
Web app to fetch and display data from nseIndia (csv files)

## Task 

### NSE stock price web application

#### Acquire Data:
1. Programatically fetch “Securities available for Equity segment (.csv)” file From the URL: https://www.nseindia.com/market-data/securities-available-for-trading
2. Programatically get the latest “bhavcopy” csv file from the following URL - https://www.nseindia.com/all-reports
3. Construct a (relational) database with normalized tables & insert both the data files into it
4. (Optional) In addition to step 2, programmatically get bhavcopies of the last 30 days instead of just the latest one.

#### Api + UI:
1. Create an API endpoint to get all the data inserted above for a given stock symbol
2. Create a web form which takes in the stock symbol as input and shows all the data that was inserted above in the “Acquire data” step. You may or may not use the API endpoint to do this step.
3. (Optional) You can show datewise data as per the step 4 of "Acquire Data" above

##### Prefered tools: Django and django-rest-framework, but any other web frameworks are fine too

#### Rules of the game:

- Code must be written in python. You are free to use google. You can use any open source tools /libraries to complete this task as required.

- The assignment has to be completed today. After the assignment is complete, send us the github link to the code and then demo your solution to us. Code quality matters to us.
