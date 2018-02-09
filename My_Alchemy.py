from datetime import datetime
from sqlalchemy import (Table, Column, Integer, Numeric, String, DateTime, ForeignKey)
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import relationship, backref

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data_model import Flight, Connection

# import __main__ as m
# from __main__ import main_wizz

engine  = create_engine('sqlite:///memory:', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base() 
class Flight_Alch(Base):
	__tablename__ = 'flights'
	flight_id = Column(Integer(), primary_key=True)
	airLine = Column(String(16), index=True)
	departureStation  = Column(String(16), index=True)
	arrivalStation  = Column(String(16), index=True)
	departureDateTime = Column(String(16), index=True)
	currencyCode  = Column(String(16), index=True)
	basePrice  = Column(String(16), index=True)
	discountedPrice  = Column(String(16), index=True)
	administrationFeePrice = Column(String(16), index=True)
  
	
	def __repr__(self):
		return "Flight_Alch(airLine='{self.airLine}', " \
				"departureStation='{self.departureStation}', " \
				"arrivalStation='{self.arrivalStation}', " \
				"departureDateTime='{self.departureDateTime}', " \
				"currencyCode='{self.currencyCode}', " \
				"basePrice='{self.basePrice}', " \
				"discountedPrice='{self.discountedPrice}', " \
				"administrationFeePrice='{self.administrationFeePrice}')".format(self=self)
Base.metadata.create_all(engine)				


# insert one instance:
cc_flight =  Flight_Alch(airLine = 'WIZZ',
						departureStation = 'TLV',
						arrivalStation = 'VNO',
						departureDateTime = '28-02-20',
						currencyCode = 'USD',
						basePrice = '280',
						discountedPrice = '140',
						administrationFeePrice='35')
session.add(cc_flight)
session.commit
print (cc_flight.flight_id)
coo = session.query(Flight_Alch).all()
print (coo)
print (cc_flight.flight_id)
conn = Connection('LUZ', 'VNO')
cc_flights =[]
w = Flight('Airflot', '354', connection=conn,
		departureDateTime= '2018-10-11', currencyCode='RUB', basePrice='100', discountedPrice='68', 
		administrationFeePrice='30') 
cc_flights.append(w)
w1 = Flight(airLine='WIZZ', flightNumber='150', connection=conn,
		departureDateTime= '2020-10-11', currencyCode='USD', basePrice='150', discountedPrice='90', 
		administrationFeePrice='31') 
cc_flights.append(w1)
print (cc_flights)
#########################################################################################
my_city = 'TLV'
date_from = "2018-02-20"
date_to = "2018-03-01"

wizz_flights = m.main_wizz(my_city)
print(wizz_flights) 
for d in wizz_flights: print (d.__dict__)

# multiple inserting:
def insert_flight(flights_list):
	data =[]
	for  f  in flights_list:
		flight =  Flight_Alch(airLine = f.airLine,
					departureStation = f.departureStation,
					arrivalStation = f.arrivalStation,
					departureDateTime = f.departureDateTime,
					currencyCode = f.currencyCode,
					basePrice = f.basePrice,
					discountedPrice = f.discountedPrice,
					administrationFeePrice= f.administrationFeePrice)
		data.append(flight)	
	session.bulk_save_objects(data)
	session.commit()
	
insert_flight(wizz_flights)

			 
