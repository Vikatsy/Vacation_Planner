
import wizzair_scraper as ws
# import ryanair_scraper as rs
import data_model as dm
import pprint
# import database as db
# import my_data_model as my


def main(): 
	pp = pprint.PrettyPrinter(indent=4)
	wizz_scraper = ws.WizzairScraper() # = ws
	# ryan_scraper = rs.RyanairScraper()

	# db_connection = db.create_connection()
	# conn = db.create_connection('Vacation.db')

	my_city = 'TLV'
	def get_my_destinations(my_city):
		all_dest = wizz_scraper.get_destination_map()
		return all_dest[my_city]

	my_dest = get_my_destinations (my_city)
	print (my_dest)
	a =[]
	# for d in my_dest: 
		# print(d)
	# import pdb; pdb.set_trace()

	c = dm.Connection(source_airport=my_city, dest_airport="VNO")
	date_from = "2018-02-20"
	date_to = "2018-03-01"

	all_flights = wizz_scraper.get_time_table(c, date_from, date_to)
	pp.pprint(all_flights)
	# import pdb; pdb.set_trace()

	my_data = wizz_scraper.flight_info(my_city, 'VNO', "2018-02-20")
	a.append(my_data)
	for item in range(0, len(a)):
		# for k,v in item.items():
		pp.pprint(a[item].__dict__)

	# all_wizz_cities = wizz_scraper.get_destinations_cities()
	# all_destination_map = wizz_scraper.get_destination_map()
	# print (all_destination_map)


	# while(True):
	# 	cheap_flights = wizz_scraper.get_cheap_flights()
	# 	for cheap_flight in cheap_flights: # ScheduledFlight
	# 		db.create_flight(conn, cheap_flight)


		# ryanair



if __name__ == "__main__":
	main()