import requests
import database
import  data_model 

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "en-US,en;q=0.8,lt;q=0.6,ru;q=0.4",
}

s = requests.Session()
s.headers.update(headers)

# to get cookies
r = s.get("https://www.wizzair.com/")

########################################################################################
# 1. Get API URL
########################################################################################
# get from https://wizzair.com/static/metadata.json
# in ['apiUrl']
url_API = 'https://wizzair.com/static/metadata.json'
r = requests.get(url_API)
data = r.json()
apiUrl = data['apiUrl']
print (apiUrl)
# apiUrl = 'https://be.wizzair.com/7.8.3/Api/'





########################################################################################
# 2. Get destinations map
########################################################################################

url3 = f'{apiUrl}/asset/map?languageCode=en-gb'
list_of_cities ={}
r = s.get(url3)
map_of_dest = r.json()
for x in range (len(map_of_dest['cities'])):
    list_of_cities[map_of_dest['cities'][x]['shortName']] = map_of_dest['cities'][x]['iata']
print (list_of_cities)

wizzair_cities = dict()

for city in map_of_dest['cities']:
    city_iata_code = city['iata']
    a = []
    wizzair_cities[city_iata_code] = a
    for connection in city['connections']:
        a.append(connection['iata'])
# print(wizzair_cities)        

 
# print(wizzair_cities) # { 'LTN': ['GDN', 'WAW', 'BUD', 'KTW', 'KUN', ...], 'LGW': ['OTP'] }




israel_cities = [x for x in map_of_dest['cities'] if x['countryCode'] == 'IL']
for city in israel_cities:
    print(f"NAME: {city['shortName']}")
    print(f"IATA CODE: {city['iata']}")
    print("DESTINATIONS:")
    dest = wizzair_cities[city['iata']]
# for city in dest print()   
        

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

# for source_city_code, destination_city_code in destinations_from_israel:
#     url = f'{apiUrl}search/flightDates?departureStation={source_city_code}'
#             '&arrivalStation={destination_city_code}&from=2018-01-25&to=2018-03-28'
#     print(url)
# =>
# {"flightDates":["2018-01-27T00:00:00","2018-01-30T00:00:00","2018-02-03T00:00:00","2018-02-06T00:00:00","2018-02-10T00:00:00",
# "2018-02-13T00:00:00","2018-02-17T00:00:00","2018-02-20T00:00:00","2018-02-24T00:00:00","2018-02-27T00:00:00",
# "2018-03-03T00:00:00","2018-03-06T00:00:00","2018-03-10T00:00:00","2018-03-13T00:00:00","2018-03-17T00:00:00",
# "2018-03-20T00:00:00","2018-03-24T00:00:00","2018-03-27T00:00:00"]}



url = f'{apiUrl}/search/search'

payload = {
    "flightList":[
        {
            "departureStation": "VNO",
            "arrivalStation": "TLV",
            "departureDate": "2018-02-20"
        }
    ],
    "adultCount": 1,
    "childCount": 0,
    "infantCount": 0,
    "wdc": True,
    "dayInterval": 7
}


r = s.post(url, json=payload)
data = r.json()
print(data['outboundFlights'][0].keys())
print(data['outboundFlights'][0]['fares'][0])


# print(data['outboundFlights'][0]['flightNumber'])
# print(data['outboundFlights'][0]['departureStation'])
# print(data['outboundFlights'][0].get('departureDateTime'))
# print(type(data['outboundFlights'][0].values()))
airLine = 'WIZZ'
flightNumber = data['outboundFlights'][0]['flightNumber']
departureStation = data['outboundFlights'][0]['departureStation']
arrivalStation = data['outboundFlights'][0]['arrivalStation']
departureDateTime  = data['outboundFlights'][0]['departureDateTime']
currencyCode = data['outboundFlights'][0]['fares'][0]['basePrice']['currencyCode']
basePrice = data['outboundFlights'][0]['fares'][0]['basePrice']['amount']
discountedPrice = data['outboundFlights'][0]['fares'][0]['discountedPrice']['amount']
administrationFeePrice = data['outboundFlights'][0]['fares'][0]['administrationFeePrice']['amount']

y = data_model.ScheduledFlight(airLine, 
    flightNumber, 
    departureStation, 
    arrivalStation, 
    departureDateTime, 
    currencyCode, 
    basePrice, 
    discountedPrice, 
    administrationFeePrice)
print(y.basePrice)
conn = database.create_connection('Vacation.db')
flight1 = (y.airLine, y.flightNumber, y.departureStation, y.arrivalStation, y.departureDateTime, 
            y.currencyCode, y.basePrice, y.discountedPrice, y.administrationFeePrice)
database.create_flight(conn,flight1)


# israel_connections = israel['connections']





# print (r.json())


# url2 = 'https://be.wizzair.com/7.8.2/Api/search/flightDates?departureStation=TLV&arrivalStation=VNO&from=2018-01-23&to=2018-03-26'
# r2 = s.get(url)

