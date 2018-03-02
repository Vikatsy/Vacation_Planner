import requests
import data_model 
from data_model import Airlines
import datetime
from datetime import datetime
from datetime import timedelta
import time
import re

class RyanairScraper:

    # TYPE = Airlines.RYAN

    def __init__(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
            "Origin": "https://www.ryanair.com",
            "Referer": "https://www.ryanair.com/gb/en/booking/home",
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, sdch, br",
            "Accept-Language": "en-US,en;q=0.8,lt;q=0.6,ru;q=0.4",
        }
 

        self.session  = requests.Session()
        self.session.headers.update(headers)
        # self.r = self.session.get("https://www.wizzair.com/")
        # self.api_url = self._get_api_url()
        # to get cookies
        coo = self.session.get("https://www.ryanair.com/")


        # print(self.api_url)


    # def _get_api_url(self):
        
    #     # get API from https://wizzair.com/static/metadata.json
    #     # in ['apiUrl']

    #     url_API = 'https://wizzair.com/static/metadata.json'
    #     r = self.session.get(url_API)
    #     data = r.json()
    #     apiUrl = data['apiUrl']
    #     print (apiUrl)

    #     return apiUrl

    # @classmethod
    def get_destinations_cities(self):

        # get destination map
        # return dict {Name of City : IAT} for all destination

        url = 'https://api.ryanair.com/aggregate/4/common?embedded=airports,countries,cities,regions,nearbyAirports,defaultAirport&market=en-gb'

        list_of_cities ={}
        r = self.session.get(url)
        map_of_dest = r.json()
        for x in range (len(map_of_dest['airports'])):
            list_of_cities[map_of_dest['airports'][x]['name']] = map_of_dest['airports'][x]['iataCode']
        # self.list_of_cities = list_of_cities
        # print (list_of_cities)
        # list_of_cities.remove('MAD|Air Europa')
        return list_of_cities
        


    def  get_destination_map(self):

        # get all destinatination for each city 
        # { 'LTN': ['GDN', 'WAW', 'BUD', 'KTW', 'KUN', ...], 'LGW': ['OTP'] }

        url ='https://api.ryanair.com/aggregate/4/common?embedded=airports,countries,cities,regions,nearbyAirports,defaultAirport&market=en-gb'
        r = self.session.get(url)
        map_of_dest = r.json()

        list_of_cities ={}
        destination = dict()

        for x in  map_of_dest['airports']:
            city_iata_code = x['iataCode']
            # print (city_iata_code)    
            connection = x['routes']
            # print (connection)
            # for item in connection: (lambda item: item if x!= 'airport:MAD|Air Europa' else 'airport:MAD')
            # my_conn = [d.partition(':')[2] for d in connection if d.partition(':')[0] == 'airport']
            my_conn =[]
            for d in connection:
                if d.partition(':')[0] == 'airport':
                    iata = d.partition(':')[2]
                    if len(iata) > 3:
                        iata = iata.partition('|')[0] 
                    my_conn.append(iata)
                    # print (my_conn)
                    # print (len(my_conn))
                    # if len(my_conn) > 3:
                    #     my_conn = my_conn.partition('|')[0] 
            # print (my_conn)
            # for item in my_conn: (lambda item: item if x!= 'MAD|Air Europa' else 'MAD')
               
            
                destination[city_iata_code] = my_conn 
            # print (my_conn)   
        # del destination['MAD|Air Europa']
        # print (destination)    
        return destination 
        

    def api_connection(self, url):
        pass     

    def flight_info(self, iata_dep, iata_arr, date):
        # get information about flight 
        # param: departure_iata IATA shot name of departure city
        # param: arrival_iata IATA shot name of arrival city
        # param: date  in format year-month-day 


        
        # url = 'https://desktopapps.ryanair.com/v4/en-ie/availability?ADT=1&CHD=0&DateOut=2018-03-26&Destination=BGY&FlexDaysOut=4&INF=0&IncludeConnectingFlights=true&Origin=TLV&RoundTrip=false&TEEN=0&ToUs=AGREED&exists=false&promoCode='
        # url = 'https://api.ryanair.com/farefinder/3/oneWayFares?&departureAirportIataCode={iata_dep}&language=en&limit=16&market=en-gb&offset=0&outboundDepartureDateFrom=2018-02-28&outboundDepartureDateTo=2018-10-28&priceValueTo=150
        if not date: 
            return None 
        else:    
            url = f'https://api.ryanair.com/farefinder/3/oneWayFares?&departureAirportIataCode={iata_dep}&arrivalAirportIataCode={iata_arr}&language=en&limit=16&market=en-gb&offset=0&outboundDepartureDateFrom={date}&outboundDepartureDateTo={date}'

            # payload = {"trips": [{'origin': 'TLV','destination': 'BGY','dates': [{'DateOut':'2018-03-26T00:00:00.000'}]} ]}   
            r = self.session.get(url)
            data = r.json()
            
            
            airLine = 'RYAN'
            
            if not 'fares' in data:
                return None
                # flightNumber = '2006'
                # departureStation = None
                # arrivalStation = None
                # departureDateTime  = None
                # currencyCode = None
                # basePrice = None
                # discountedPrice = 'NOT FIND'
                # administrationFeePrice = 'NOT FIND'
                # connection = data_model.Connection(departureStation, arrivalStation)
            else:  
                # print(data)
                outbound_flight =  data['fares'][0]['outbound'] 
                # print (data['fares'])
                flightNumber = '2006'
                departureStation = outbound_flight['departureAirport']['iataCode']
                arrivalStation = outbound_flight['arrivalAirport']['iataCode']
                departureDateTime  = outbound_flight['departureDate']
                currencyCode = outbound_flight['price']['currencyCode']
                basePrice = outbound_flight['price']['value']
                discountedPrice = 'NOT FIND'
                administrationFeePrice = 'NOT FIND'
                connection = data_model.Connection(departureStation, arrivalStation)
            
            y = data_model.Flight(airLine, 
                    flightNumber, 
                    connection,
                    departureDateTime, 
                    currencyCode, 
                    basePrice, 
                    discountedPrice, 
                    administrationFeePrice)
            
            return y

    def  possible_flight(self, departure_iata, date1, date2):
        # get all possible flights from city between these dates
        # param: departure_iata IATA shot name of departure city
        # param: date1 date2  in format year-month-day 
        pass
        
    
        # conn = database.create_connection('Vacation.db')

        # database.create_flight(conn,y)


# israel_connections = israel['connections']
# print (r.json())



# url2 = 'https://be.wizzair.com/7.8.2/Api/search/flightDates?departureStation=TLV&arrivalStation=VNO&from=2018-01-23&to=2018-03-26'
# r2 = s.get(url)

###############################################################################

# israel_cities = [x for x in map_of_dest['cities'] if x['countryCode'] == 'IL']
# for city in israel_cities:
#     print(f"NAME: {city['shortName']}")
#     print(f"IATA CODE: {city['iata']}")
#     print("DESTINATIONS:")
#     dest = wizzair_cities[city['iata']]
# # for city in dest print()   
        

# israel_airports = [x['iata'] for x in israel_cities]

# destinations_from_israel = []
# for city in israel_cities:
#     source_city_code = city['iata']
#     for destination in city['connections']:
#         destination_city_code = destination['iata']
        # destinations_from_israel.append((source_city_code, destination_city_code))

# @TODO write to database to scheduled Flights table



########################################################################################
# 3. For each pair of cities (TLV, RIX) 
# get flight dates
########################################################################################
    def get_time_table(self, connect, date_from, date_to):
		# logger.debug(f"get_time_table: got {connect}, {date_from}, {date_to}")

    	# if date_from is None:
    	# 	# BAD!!!!
    	# 	raise ValueError("Date_from can't be None")

        source_city_code = connect.source_airport
        destination_city_code = connect.dest_airport 
        
        date_format = "%Y-%m-%d"
        date1 = datetime.strptime(date_from, date_format)
        date2 = datetime.strptime(date_to, date_format) 
        delta = date2-date1
        # print(delta)
        # d1 = datetime.strptime(date_to, date_format) + timedelta(days=1) 
        # for source_city_code, destination_city_code in destinations_from_israel:
        # url = f'https://desktopapps.ryanair.com/v4/Calendar?Destination={destination_city_code}&IncludeConnectingFlights=true&IsTwoWay=false&Months=17&Origin={source_city_code}&StartDate={date1}'
        # url3 = 'https://desktopapps.ryanair.com/Calendar?Destination={destination_city_code}&IsTwoWay=false&Months=16&Origin=CFU&StartDate=2018-03-06'
        
        # url = f'https://desktopapps.ryanair.com/v4/Calendar?Destination={destination_city_code}&IncludeConnectingFlights=true&IsTwoWay=false&Origin={source_city_code}&StartDate={date_from}'
        url = f'https://desktopapps.ryanair.com/v4/Calendar?Destination={connect.dest_airport}&IncludeConnectingFlights=false&IsTwoWay=false&Origin=TLV&StartDate={date_from}'
        r = self.session.get(url)
        data = r.json()
        if 'outboundDates' in data:
        # print(data)
            data_clear =[]
            
            for d in  data['outboundDates']:
                if  datetime.strptime(d, date_format)<= date2:
                    data_clear.append(d.partition('T')[0])
          
            # logger.debug(f"get_time_table: returning {data_clear}")
            # print (data_clear)
            return data_clear
        else:  
            print('No date table')
            return None  
# =>
# {"flightDates":["2018-01-27T00:00:00","2018-01-30T00:00:00","2018-02-03T00:00:00","2018-02-06T00:00:00","2018-02-10T00:00:00",
# "2018-02-13T00:00:00","2018-02-17T00:00:00","2018-02-20T00:00:00","2018-02-24T00:00:00","2018-02-27T00:00:00",
# "2018-03-03T00:00:00","2018-03-06T00:00:00","2018-03-10T00:00:00","2018-03-13T00:00:00","2018-03-17T00:00:00",
# "2018-03-20T00:00:00","2018-03-24T00:00:00","2018-03-27T00:00:00"]}
#########################################
if __name__ == '__main__':
    c= RyanairScraper()
    cities = c.get_destinations_cities()

    # print(cities)
    a =  c.get_destination_map()
    print(a['TLV'])
    # a['TLV'].remove('MAD|Air Europa')
    # print(a['TLV'])
    for city in a['TLV']:
        connect = data_model.Connection('TLV',city)
        print (connect)
        #
        ti = c.get_time_table(connect, '2018-05-02','2018-05-03')
        print (ti)
        time.sleep(3)
        for t in ti: 
            flight = c.flight_info('TLV', city, t)
            # print(flight) 
    # f = c.flight_info('TLV', 'BGY', '2018-03-07')
    # print(f)
