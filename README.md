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


## Solution

### Pages

![image](https://user-images.githubusercontent.com/72795959/174955094-80659b3c-4d82-4c48-861a-aae8a98c773b.png)

Searching And AutoComplete suggestion !
![image](https://user-images.githubusercontent.com/72795959/174955171-b9d436b0-4344-4498-b4ac-f8b728e6f22d.png)

Data for a Stock symbol (eg sbin) !. Gathered from full bhavcopy (.csv) & securities available for equity (.csv)
![image](https://user-images.githubusercontent.com/72795959/174955430-700418d8-7769-4dad-b4ea-add56b9346b2.png)

__*Refresh* Button on Top Fetch data from *nseIndia* and stores it in our *Database*__ !
![image](https://user-images.githubusercontent.com/72795959/174955847-a313669c-05b4-4049-add1-273e1c1f262f.png)



### Login Detail for Admin panel 
to access database at */admin*

*username* : ksharma20

*password* : EquitySecurityApp

![image](https://user-images.githubusercontent.com/72795959/174958271-83e67178-8526-46e9-bb14-9720dd9a0153.png)

### Fetching & Storing Data
![image](https://user-images.githubusercontent.com/72795959/174956046-736da782-38e9-435c-affb-c666f9eaf37e.png)


### Database Models (Relational created from csv's)

**Eqsecurity**

![image](https://user-images.githubusercontent.com/72795959/174956234-c2b688ae-2975-49cb-86be-4cb6ab21f11e.png)

**Bhavcopy**

![image](https://user-images.githubusercontent.com/72795959/174956322-93f2c1fa-99ee-41c5-800a-43b7cc6ae4ba.png)


### Apis
![image](https://user-images.githubusercontent.com/72795959/174957721-92a53402-65b2-4c14-8732-f7be5dc1da09.png)



### This solution is able to 
- fetch data *(/apis/refresh/)*
- store it in database
- Accessing data from apis (*/apis/stock/<<!symbol>>/* & */apis/bhav/<<!symbol>>/*)
- Web search form with auto suggestion 
- Details of the stock symbol (with bhav)
