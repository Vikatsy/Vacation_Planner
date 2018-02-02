import requests
import data_model 
from data_model import Airlines
from datetime import datetime

class WizzairScraper:

    # TYPE = Airlines.WIZZ

    def __init__(self):
         
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, sdch, br",
            "Accept-Language": "en-US,en;q=0.8,lt;q=0.6,ru;q=0.4",
        }

        # # s = requests.Session()
        # # s.headers.update(headers)
        # url = 'https://be.wizzair.com/7.8.3/Api/'    
        # # to get cookies
        # # r = s.get("https://www.wizzair.com/")
        # self.session = requests.Session()
        # s.headers.update(headers)

        self.session  = requests.Session()
        self.session.headers.update(headers)
        self.r = self.session.get("https://www.wizzair.com/")
        self.api_url = self._get_api_url()
        # to get cookies
        # import pdb; pdb.set_trace() 
        # self.list_of_cities = None


        # print(self.api_url)


    def _get_api_url(self):
        
        # get API from https://wizzair.com/static/metadata.json
        # in ['apiUrl']

        url_API = 'https://wizzair.com/static/metadata.json'
        r = self.session.get(url_API)
        data = r.json()
        apiUrl = data['apiUrl']
        print (apiUrl)

        return apiUrl


    def get_destinations_cities(self):

        # get destination map
        # return dict {Name of City : IAT} for all destination

        url3 = f'{self.api_url}/asset/map?languageCode=en-gb'
        list_of_cities ={}
        r = self.session.get(url3)
        map_of_dest = r.json()
        for x in range (len(map_of_dest['cities'])):
            list_of_cities[map_of_dest['cities'][x]['shortName']] = map_of_dest['cities'][x]['iata']
        # self.list_of_cities = list_of_cities

        return list_of_cities
        


    def  get_destination_map(self):

        # get all destinatination for each city 
        # { 'LTN': ['GDN', 'WAW', 'BUD', 'KTW', 'KUN', ...], 'LGW': ['OTP'] }

        url3 = f'{self.api_url}/asset/map?languageCode=en-gb'
        list_of_cities ={}
        r = self.session.get(url3)
        map_of_dest = r.json()

        destination = dict()

        for city in map_of_dest['cities']:
            city_iata_code = city['iata']
            a = []
            destination[city_iata_code] = a
            for connection in city['connections']:
                a.append(connection['iata'])
        # self.destination =  destination    
        return destination  
            
    def api_connection(self, url):
        pass     

    def flight_info(self, iata_dep, iata_arr, date):
        # get information about flight 
        # param: departure_iata IATA shot name of departure city
        # param: arrival_iata IATA shot name of arrival city
        # param: date  in format year-month-day 


        
        url = f'{self.api_url}/search/search'

        payload = {
            "flightList":[
                {
                    "departureStation": iata_dep,
                    "arrivalStation": iata_arr,
                    "departureDate": date
                }
            ],
            "adultCount": 1,
            "childCount": 0,
            "infantCount": 0,
            "wdc": True,
            "dayInterval": 7
        }


        r = self.session.post(url, json=payload)
        data = r.json()
        print (data.keys())
        airLine = 'WIZZ'
        outbound_flight =  data['outboundFlights'][0]
        flightNumber = outbound_flight['flightNumber']
        departureStation = outbound_flight['departureStation']
        arrivalStation = outbound_flight['arrivalStation']
        departureDateTime  = outbound_flight['departureDateTime']
        fares = outbound_flight['fares'][0]
        currencyCode = fares['basePrice']['currencyCode']
        basePrice = fares['basePrice']['amount']
        discountedPrice = fares['discountedPrice']['amount']
        administrationFeePrice = fares['administrationFeePrice']['amount']
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
        source_city_code = connect.source_airport
        destination_city_code = connect.dest_airport 
        date1 = date_from
        date2 = date_to  
        # for source_city_code, destination_city_code in destinations_from_israel:
        url = f'{self.api_url}/search/flightDates?departureStation={source_city_code}&arrivalStation={destination_city_code}&from={date1}&to={date2}'
        # https://be.wizzair.com/7.8.5/Api/search/flightDates?departureStation=TLV&arrivalStation=VNO&from=2018-02-02&to=2018-04-05   
        r = self.session.get(url)
        data = r.json()
        data_clear =[]
        for d in  data['flightDates']:
            data_clear.append(d.partition('T')[0])
        
        return data_clear
# =>
# {"flightDates":["2018-01-27T00:00:00","2018-01-30T00:00:00","2018-02-03T00:00:00","2018-02-06T00:00:00","2018-02-10T00:00:00",
# "2018-02-13T00:00:00","2018-02-17T00:00:00","2018-02-20T00:00:00","2018-02-24T00:00:00","2018-02-27T00:00:00",
# "2018-03-03T00:00:00","2018-03-06T00:00:00","2018-03-10T00:00:00","2018-03-13T00:00:00","2018-03-17T00:00:00",
# "2018-03-20T00:00:00","2018-03-24T00:00:00","2018-03-27T00:00:00"]}
#########################################
