import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    "Origin": "https://www.ryanair.com",
    "Referer": "https://www.ryanair.com/gb/en/booking/home",
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "en-US,en;q=0.8,lt;q=0.6,ru;q=0.4",
}

s = requests.Session()
s.headers.update(headers)
coo = s.get("https://www.ryanair.com/")
url ='https://api.ryanair.com/aggregate/4/common?embedded=airports,countries,cities,regions,nearbyAirports,defaultAirport&market=en-gb'
r = s.get(url)
# print(r.text)
data = r.json()
# print(data['airports'])
# print(data['defaultAirport'])
for x in range (0, len(data['airports'])):
    print (data['airports'][x]['iataCode'])

rout = data['airports'][0]['routes']
my_rout = [d.partition(':')[2] for d in rout if d.partition(':')[0] == 'airport']
# print (my_rout)
        




url2 = 'https://desktopapps.ryanair.com/v4/Calendar?Destination=BGY&IncludeConnectingFlights=true&IsTwoWay=false&Months=17&Origin=TLV&StartDate=2018-02-06'
r = s.get(url2)
data = r.json()
print(data)

# import pdb; pdb.set_trace()

url3 = 'https://desktopapps.ryanair.com/v4/en-ie/availability?ADT=1&CHD=0&DateOut=2018-03-26&Destination=BGY&FlexDaysOut=4&INF=0&IncludeConnectingFlights=true&Origin=TLV&RoundTrip=false&TEEN=0&ToUs=AGREED&exists=false&promoCode='
# r = s.get(url3)

# data = r.json()
# # print(data)
# c = data['trips']
# # print(c)
# print(data.keys())



payload = {"trips": [{'origin': 'TLV','destination': 'BGY','dates': [{'DateOut':'2018-03-26T00:00:00.000'}]} ]}
            
        
    
r = s.get(url3, json=payload)
data = r.json()
# print(data['currency'])
# # print(data['trips'][0])
# print(data['trips'][0])
# print(data['trips'][0]['dates'][0]['flights'][0]['flightNumber'])
# # print(data['trips'][0]['origin'])
# # print(data['trips'][0]['destination'])
# print(data['trips'][0]['dates'])
# print(data['trips'][0]['dates'][0]['flights'][0]['regularFare'])



# url4 = 'https://flights.ryanair.com/booking/airline/widget/change'
# r = s.get(url4)
# print(r.text)
# data = r.json()
#

# get from https://wizzair.com/static/metadata.json
# in ['apiUrl']

# https://be.wizzair.com/7.8.3/Api/search/flightDates?departureStation=TLV&arrivalStation=VNO&from=2018-01-25&to=2018-03-28
# =>
# {"flightDates":["2018-01-27T00:00:00","2018-01-30T00:00:00","2018-02-03T00:00:00","2018-02-06T00:00:00","2018-02-10T00:00:00",
# "2018-02-13T00:00:00","2018-02-17T00:00:00","2018-02-20T00:00:00","2018-02-24T00:00:00","2018-02-27T00:00:00",
# "2018-03-03T00:00:00","2018-03-06T00:00:00","2018-03-10T00:00:00","2018-03-13T00:00:00","2018-03-17T00:00:00",
# "2018-03-20T00:00:00","2018-03-24T00:00:00","2018-03-27T00:00:00"]}

# url = 'http://apigateway.ryanair.com/pub/v1/timetable/3/schedules/TLV/BGY/years/2018/months/02?apikey=tsVQ06jsOAWup17HPPkrQSZjon32yOik'
# url ='https://api.ryanair.com/aggregate/4/common?embedded=airports,countries,cities,regions,nearbyAirports,defaultAirport&market=en-gb'
# r = requests.post(url, json=payload)

# print(r.text)

# data = r.json()
# import pdb;pdb.set_trace()

#print(data['outboundFlights'][0]['flightNumber'])
# print(data['outboundFlights'][0]['departureStation'])
# print(data['outboundFlights'][0].get('departureDateTime'))
#print(type(data['outboundFlights'][0].values()))


# url2 = 'https://be.wizzair.com/7.8.2/Api/search/flightDates?departureStation=TLV&arrivalStation=VNO&from=2018-01-23&to=2018-03-26'
# r2 = requests.get(url)

