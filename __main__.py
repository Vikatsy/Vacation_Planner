import wizzair_scraper as ws
import ryanair_scraper as rs
import data_model as dm
import database as db


def main():
	wizz_scraper = ws.WizzairScraper() # = ws
	ryan_scraper = rs.RyanairScraper()

	# db_connection = db.create_connection()
	conn = db.create_connection('Vacation.db')


	while(True):
		cheap_flights = wizz_scraper.get_cheap_flights()
		for cheap_flight in cheap_flights: # ScheduledFlight
			db.create_flight(conn, cheap_flight)


		# ryanair



if __name__ == "__main__":
	main()