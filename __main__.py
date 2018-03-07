from data_model import Airlines
import requests

import wizzair_scraper as ws
import ryanair_scraper as rs
import data_model as dm
import pprint
import My_Alchemy 
from flask import Flask
import time
import datetime
from datetime import timedelta

# DATABASE = VacationAlchemy()

app = Flask(__name__)
pp = pprint.PrettyPrinter(indent=4)

now = datetime.datetime.now()
today =  now.date()
final_date = today + timedelta(days=10)

def main_scrape(scraper, my_city, date_from, date_to): 
	# wizz_scraper = ws.WizzairScraper() # = ws

	
	def get_my_destinations(my_city):
		all_dest = scraper.get_destination_map()
		return all_dest[my_city]

	my_dest = get_my_destinations (my_city)
	print(my_dest)

	a=[]
	for y in my_dest:
		c = dm.Connection(source_airport=my_city, dest_airport=y)
		time.sleep(3)
		# print(c)
		all_flights = scraper.get_time_table(c, date_from, date_to)
		# print(all_flights)
		# time.sleep(3)
		for x in  all_flights:
			print(my_city, y, x)
			my_data = scraper.flight_info(my_city, y, x)
			# print(my_city, y, x)
			if my_data: a.append(my_data)
			time.sleep(7)
						
	# print (a)
	return a	
	

def get_scraper(airline_type): 
	''' factory pattern
	'''
	if airline_type == Airlines.WIZZ:
		return ws.WizzairScraper()
	elif airline_type == Airlines.RYAN:
		return rs.RyanairScraper()

SCRAPERS = [ 
	# ws.WizzairScraper(), 
	get_scraper(Airlines.WIZZ),
	get_scraper(Airlines.RYAN)
	]

def scrape(city, date_from, date_to):
	flights = []
	for scraper in SCRAPERS:
		this_flights = main_scrape(scraper, city, date_from, date_to)
		flights.extend(this_flights)
	return flights

# DATABASE = VacationAlchemy()

# My_Alchemy.Alchemy_Connection.insert_flights(flights)




@app.route('/scrape/<city_from>/<date_from>/<date_to>/')
def do_all_scraping(city_from, date_from, date_to):
# create scrapers using factory
	# per scraper (airline):
	# - get all connections for this airline 
	# - (optional) save all connections for this airline to DB, replacing old records where needed
	# - for each connection:
	#   - get flights (with dates and prices) two months forward
	# 	- save flights to database (replace)

	# flights_curr = scrape(city_from, date_from, date_to)
	database = My_Alchemy.Alchemy_Connection()
	# database.insert_flights(flights_curr)	
	return f'your flights are ready{database.get_all_flights()}'
	

@app.route('/fly/')
def get_flights():
	# make form and redirect to '/fly/<city_from>/<city_to>/'
	return 'Please go to /fly/[city_from]/[city_to]/'


	
@app.route('/fly/<city_from>/<city_to>/<date_from>/<date_return>/')
def get_flights_somewhere(city_from, city_to, date_from, date_return):


    # dep_city = form. ....
    # date_dep  = form. ....
    # date_back = form. ....

    # all_flights_pairs = backend_get_flights_somewhere(my_city, date_from, date_to)
    # format nicely in html

# def backend_get_flights_somewhere(my_city, date_from, date_to):
# 	# get from database the list of all flights from dep_city to somewhere on date_dep
#     # for each flight:
#     #   - get from database the flights from destination to dep_city on date_back
#     #   - make pairs
#     # return pairs
	# flights_curr = scrape(city_from, date_from, date_return)
	database = My_Alchemy.Alchemy_Connection()
	# database.insert_flights(flights_curr)	
	# database.insert_flights(flights_curr)	
	# d = database.get_flight(arrivalStation=city_to)
	return f"your flights  from {city_from} to {city_to} are ready{database.get_flight(arrivalStation=city_to)}"
	# return f'Flying from {city_from} to {city_to} on {date_from} and back on {date_return}...'





if __name__ == "__main__":
	# flights_curr = scrape('TLV', '2018-03-05','2018-03-18')
	# pprint(flights_curr)
	# f = main_scrape(ws.WizzairScraper(), 'TLV', "2018-03-05","2018-03-10")
	# # pp.pprint(f)
	# # print(type(f))
	# # DATABASE = My_Alchemy.Flight_Alch()
	f = scrape('TLV', "2018-04-04","2018-04-10")
	database = My_Alchemy.Alchemy_Connection()
	database.insert_flights(f)	
	# all_f = database.get_all_flights() 
	# for item in all_f: 
	# 	print (item)
	# filter_flight = database.get_flight(arrivalStation = 'BGY')
	# pp.pprint (filter_flight)

	# # f = main_scrape(rs.RyanairScraper(), 'TLV', "2018-05-10","2018-05-20")
	# pp.pprint(f)
	# print(type(f))
	# scrape_and_print()
	# app.run(debug=True)

	# template.render(path='templates/my_template.jin2')

# all_wizz_cities = wizz_scraper.get_destinations_cities()
	# all_destination_map = wizz_scraper.get_destination_map()
	# print (all_destination_map)


	# while(True):
	# 	cheap_flights = wizz_scraper.get_cheap_flights()
	# 	for cheap_flight in cheap_flights: # ScheduledFlight
	# 		db.create_flight(conn, cheap_flight)


		# ryanair
# def main_ryan(my_city):
# 	ryan_scraper = rs.RyanairScraper()

# 	def get_my_destinations(my_city):
# 		all_dest = ryan_scraper.get_destination_map()
# 		return all_dest[my_city]

# 	my_dest = get_my_destinations (my_city)
# 	# print (my_dest)
# 	for y in range(0, len(my_dest)):
# 		c = dm.Connection(source_airport=my_city, dest_airport=my_dest[y])
# 		date_from = "2018-02-20"
# 		date_to = "2018-03-01"

# 		all_flights = ryan_scraper.get_time_table(c, date_from, date_to)
# 		print(all_flights)
# 	# import pdb; pdb.set_trace()
# 		a=[]
# 		for x in  range (0, len(all_flights)):
# 			my_data = ryan_scraper.flight_info(my_city, my_dest[y], all_flights[x])
# 			print (all_flights[x])
# 			# for item in range(0, len(a)-1):
# 			a.append(my_data)
			
		# for d in a: print (d.__dict__)	

	# c = [dm.Connection(source_airport=my_city, dest_airport=my_dest[x]) for x in range(0, len(my_dest))]
	# # date_from = "2018-02-20"
	# # date_to = "2018-03-01"
	# print(c)

	# all_flights = ryan_scraper.get_time_table(c, date_from, date_to)
	# # pp.pprint(all_flights)
	# # import pdb; pdb.set_trace()
	
	# my_data = [ryan_scraper.flight_info(my_city, my_dest[y], all_flights[x]) for x in  range (0, len(all_flights))]
	# # print (all_flights[x])
				
	# for d in my_data: print (d.__dict__)	

