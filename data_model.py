from enum import Enum 

class Airport(object):
	pass


class Connection:
	"""
	Respresents a connection between two cities.
	"""
	def __init__(self, source_airport, dest_airport):
		"""
		:param: source_airport IATA code for the source airport
		:param: dest_airport IATA code for the destination airport
		"""
		self.source_airport = source_airport
		self.dest_airport = dest_airport
		
	def __repr__(self):
		return f"Connection from {self.source_airport} to {self.dest_airport}"


class Airlines: 
	WIZZ = 'Wizzair'
	RYAN = 'Ryanair'
	def __init__(self): pass



class Flight:
	'''
	Represents a scheduled flight over a connection.
	'''
	# def __init__	(self, airLine, flightNumber, departureStation, arrivalStation,
	def __init__	(self, airLine, flightNumber, connection,
		departureDateTime, currencyCode, basePrice, discountedPrice, administrationFeePrice):
		'''
		:param: connection From where to where this flight is going
		:param: airline Enum of which airline performs this flight
		:param: flight number String of flight number
		'''
		self.airLine = airLine
		self.flightNumber = flightNumber 
		self.departureStation = connection.source_airport
		self.arrivalStation = connection.dest_airport
		self.departureDateTime = departureDateTime
		self.currencyCode = currencyCode
		self.basePrice = basePrice
		self.discountedPrice = discountedPrice
		self.administrationFeePrice = administrationFeePrice

	def __repr__(self):
		return f"FLight {self.airLine} {self.flightNumber}  time {self.departureDateTime} to {self.arrivalStation} {self.basePrice}{self.currencyCode}"
	


class ActualFlight:
	def __init__(self, scheduled_flight, departure_date_time, price_in_usd):
		pass

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

