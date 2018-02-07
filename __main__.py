
import wizzair_scraper as ws
import ryanair_scraper as rs
import data_model as dm
import pprint
from My_Alchemy 
# import database as db
# import my_data_model as my


def main_wizz(my_city): 
	wizz_scraper = ws.WizzairScraper() # = ws
	

	# db_connection = db.create_connection()
	# conn = db.create_connection('Vacation.db')

	
	def get_my_destinations(my_city):
		all_dest = wizz_scraper.get_destination_map()
		return all_dest[my_city]

	my_dest = get_my_destinations (my_city)
	# print (my_dest)
	a =[]
	# for d in my_dest: 
		# print(d)
	# import pdb; pdb.set_trace()
	for y in range(0, len(my_dest)):
		c = dm.Connection(source_airport=my_city, dest_airport=my_dest[y])
		date_from = "2018-02-20"
		date_to = "2018-03-01"

		all_flights = wizz_scraper.get_time_table(c, date_from, date_to)
		pp.pprint(all_flights)
	# import pdb; pdb.set_trace()
	
		for x in  range (0, len(all_flights)):
			my_data = wizz_scraper.flight_info(my_city, my_dest[y], all_flights[x])
			print (all_flights[x])
			# for item in range(0, len(a)-1):
			a.append(my_data)
			
	for d in a: print (d.__dict__)	

	# all_wizz_cities = wizz_scraper.get_destinations_cities()
	# all_destination_map = wizz_scraper.get_destination_map()
	# print (all_destination_map)


	# while(True):
	# 	cheap_flights = wizz_scraper.get_cheap_flights()
	# 	for cheap_flight in cheap_flights: # ScheduledFlight
	# 		db.create_flight(conn, cheap_flight)


		# ryanair
def main_rayn(my_city):
	ryan_scraper = rs.RyanairScraper()

	def get_my_destinations(my_city):
		all_dest = ryan_scraper.get_destination_map()
		return all_dest[my_city]

	my_dest = get_my_destinations (my_city)
	# print (my_dest)
	
	c = [dm.Connection(source_airport=my_city, dest_airport=my_dest[y]) for x in range(0, len(my_dest))
		# date_from = "2018-02-20"
		# date_to = "2018-03-01"

	all_flights = ryan_scraper.get_time_table(c, date_from, date_to)
	# pp.pprint(all_flights)
	# import pdb; pdb.set_trace()
	
	my_data = [ryan_scraper.flight_info(my_city, my_dest[y], all_flights[x]) for x in  range (0, len(all_flights))]
	# print (all_flights[x])
				
	for d in my_data: print (d.__dict__)	

def main():
	pp = pprint.PrettyPrinter(indent=4)
	my_city = 'TLV'
	date_from = "2018-02-20"
	date_to = "2018-03-01"

	main_wizz(my_city)
	main_ryan(my_city) 

if __name__ == "__main__":
	main()