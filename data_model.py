from enum import Enum 

class Airport(object):
	pass


class Connection:
	"""
	Respresents a connection between two cities.
	"""
	def __init__(self, ):
		"""
		:param: source_airport IATA code for the source airport
		:param: dest_airport IATA code for the destination airport
		"""
		self.source_airport = source_airport
		self.dest_airport = dest_airport


class Airlines (Enum): 
	WIZZ = 'Wizzair'
	RYAN = 'Ryanair'


class ScheduledFlight:
	'''
	Represents a scheduled flight over a connection.
	'''
	def __init__	(self, airLine, flightNumber, departureStation, arrivalStation,
					departureDateTime, currencyCode, basePrice, discountedPrice, administrationFeePrice):
		'''
		:param: connection From where to where this flight is going
		:param: airline Enum of which airline performs this flight
		:param: flight number String of flight number
		'''
		self.airLine = airLine
		self.flightNumber = flightNumber 
		self.departureStation = departureStation
		self.arrivalStation = arrivalStation
		self.departureDateTime = departureDateTime
		self.currencyCode = currencyCode
		self.basePrice = basePrice
		self.discountedPrice = discountedPrice
		self.administrationFeePrice = administrationFeePrice


class ActualFlight:
	def __init__(self, scheduled_flight, departure_date_time, price_in_usd):
		pass


