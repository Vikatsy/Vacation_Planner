import requests
import data_model 
from data_model import Airlines
from datetime import datetime

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
        self.r = self.session.get("https://www.wizzair.com/")
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


    def get_destinations_cities(self):

        # get destination map
        # return dict {Name of City : IAT} for all destination

        url = 'https://api.ryanair.com/aggregate/4/common?embedded=airports,countries,cities,regions,' \
                'nearbyAirports,defaultAirport&market=en-gb'

        list_of_cities ={}
        r = self.session.get(url)
        map_of_dest = r.json()
        for x in range (len(map_of_dest['airports'])):
            list_of_cities[map_of_dest['airports'][x]['name']] = map_of_dest['airports'][x]['iataCode']
        # self.list_of_cities = list_of_cities

        return list_of_cities
        


    def  get_destination_map(self):

        # get all destinatination for each city 
        # { 'LTN': ['GDN', 'WAW', 'BUD', 'KTW', 'KUN', ...], 'LGW': ['OTP'] }

        url ='https://api.ryanair.com/aggregate/4/common?embedded=airports,countries,cities,regions,'\
                    'nearbyAirports,defaultAirport&market=en-gb'
        r = self.session.get(url)
        map_of_dest = r.json()

        list_of_cities ={}
        destination = dict()

        for x in  range (0, len(map_of_dest['airports'])):
            city_iata_code = city[x]['iataCode']
            connection = data['airports'][x]['routes']
            my_conn = [d.partition(':')[2] for d in connection if d.partition(':')[0] == 'airport']
            destination[city_iata_code] = my_conn 
            print (my_conn)   
            return destination 
        

    def api_connection(self, url):
        pass     

    def flight_info(self, iata_dep, iata_arr, date):
        # get information about flight 
        # param: departure_iata IATA shot name of departure city
        # param: arrival_iata IATA shot name of arrival city
        # param: date  in format year-month-day 


        
        url = 'https://desktopapps.ryanair.com/v4/en-ie/availability?ADT=1&CHD=0&DateOut=2018-03-26&Destination=BGY&FlexDaysOut=4&INF=0&IncludeConnectingFlights=true&Origin=TLV&RoundTrip=false&TEEN=0&ToUs=AGREED&exists=false&promoCode='
        

        payload = {"trips": [{'origin': 'TLV','destination': 'BGY','dates': [{'DateOut':'2018-03-26T00:00:00.000'}]} ]}   
        r = self.session.get(url, json=payload)
        data = r.json()

        airLine = 'RYAN'
        outbound_flight =  data['trips'][0]['dates'][0]['flights'][0]
        flightNumber = outbound_flight['flightNumber']
        departureStation = data['trips'][0]['origin']
        arrivalStation = data['trips'][0]['destination']
        departureDateTime  = outbound_flight['dateOut']
       
        currencyCode = data['currency']
        basePrice = outbound_flight['regularFare']['fares'][0]['amount']
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
        source_city_code = connect.source_airport
        destination_city_code = connect.dest_airport 
        date1 = date_from
        date2 = date_to  
        # for source_city_code, destination_city_code in destinations_from_israel:
        url = f'https://desktopapps.ryanair.com/v4/Calendar?Destination={destination_city_code}&IncludeConnectingFlights=true&IsTwoWay=false&Months=17&Origin={source_city_code}&StartDate={date1}'
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