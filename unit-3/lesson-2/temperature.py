# First of all, we import our packages and set our variables:

import requests
import sqlite3 as lite
import datetime
from datetime import timedelta

cities = {
	"Salt_Lake_City" : '40.778996,-111.932630',
	"Denver" : '39.761850,-104.881105',
	"Seattle" : '47.620499,-122.350876',
	"Washington" : '38.904103,-77.017229',
	"Chicago" : '41.837551,-87.681844'
}


apiSource = 'https://api.forecast.io/forecast/'
apiKey = '09beac0d93209c589e132f8932ed5463'

# Create the necessary datetime objects to iterate through the exercise:

# by setting this equal to a variable, we fix the calculation to the point when we started the scrip (rather than have things move around while we're coding.)
end_date = datetime.datetime.now()


# Since we're retrieving the data points one by one, it makes sense to go ahead and load the data into the database as we get it. Since we're only querying one data point (temperature), we have a reasonable expectation of what values we can expect.

#Create and Establish the connection to the database:
#create
con = lite.connect('weather.db')
#connect
cur = con.cursor()

#get the list of keys
cities.keys()

with con:
	cur.execute('DROP TABLE IF EXISTS daily_temp')
	cur.execute('CREATE TABLE daily_temp( day_of_reading INT, Salt_Lake_City REAL, Denver REAL, Seattle REAL, Washington REAL, Chicago REAL);')

# In SQL, a row has to be inserted before it can be updated. In order to keep the code clean, we're going to iterate through the values in the range and insert them into the database without any other values

query_date = end_date - datetime.timedelta(days=30)

with con:
	while query_date < end_date:
		cur.execute("INSERT INTO daily_temp(day_of_reading) VALUES (?)", ( int( query_date.strftime('%s') ) , ) )
		query_date += datetime.timedelta(days=1)

# Now we can loop through our cities and query the API:
for k,v in cities.iteritems():
	query_date = end_date - datetime.timedelta(days=30) #set value each time through the loop of cities
	while query_date < end_date:
		#query for the value - get data for each city
		r = requests.get(apiSource + apiKey + '/' + v + ',' + end_date.strftime('%s'))

		with con:
			#insert the temperature max to the database
			cur.execute('UPDATE daily_temp SET ' + k + ' = ' + str(r.json()['daily']['data'][0]['temperatureMax']) + ' WHERE day_of_reading = ' + query_date.strftime('%s'))

		#increment query_date to the next day for next operation of loop
		query_date += datetime.timedelta(days=1) #increment query_date to the next day

con.close() # a good practice to close connection to database

# Build the API call by combining the string elements in Python for your first city. You can use the datetime.datetime.now() function from the datetime package for the current datetime. You can use the datetime.timedelta() function to subtract or add time to a date. In this case, we'll be subtracting 30 days from the current date to get our start date and then iterating through until the present day. We do that like this start_date = datetime.datetime.now() - datetime.timedelta(days=30). This will subtract 30 days from the current day.

#API call pattern https://api.forecast.io/forecast/APIKEY/LATITUDE,LONGITUDE,TIME

# start_date = datetime.datetime.now() - datetime.timedelta(days=30)


# Test the call for your first city and make sure you have it formatted properly. You can start by just printing out the URL and pasting it into your browser before you use the requests package to do the call for you. This can help you troubleshoot any errors (though you can use the text and status_code attributes to also troubleshoot any errors)


# Once you have the URL formatted properly, issue the request from your code and inspect the result. 

# r = requests.get(apiSource + apiKey + '/' + str(cities['Salt Lake City']) + ',' + start_date.strftime('%s'))

# How many levels does the data have? Which field do we want to save to get the daily maximum temperature?
# r.json().keys()
# It has 8 levels, a.k.a. keys

# Based on the data sample, create the table in a SQLite database called "weather.db".



# Write a script that takes each city and queries every day for the past 30 days (Hint: You can use the datetime.timedelta(days=1) to increment the value by day)


# Save the max temperature values to the table, keyed on the date. You can leave the date in Unix time or convert to a string.