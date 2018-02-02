
import wizzair_scraper as ws
# import ryanair_scraper as rs
import data_model as dm
# import database as db
# import my_data_model as my


def main(): 
	wizz_scraper = ws.WizzairScraper() # = ws
	# ryan_scraper = rs.RyanairScraper()

	# db_connection = db.create_connection()
	# conn = db.create_connection('Vacation.db')

	my_city = 'TLV'
	def get_my_destinations(my_city):
		all_dest = wizz_scraper.get_destination_map()
		return all_dest[my_city]
	my_dest = get_my_destinations (my_city)	

	# print (my_dest)
	# for d in my_dest: 
	my_data = wizz_scraper.flight_info(my_city, "VNO", "2018-02-20")
	print(my_data.airLine)
	print(my_data.discountedPrice)

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