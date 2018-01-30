import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "en-US,en;q=0.8,lt;q=0.6,ru;q=0.4",
}

s = requests.Session()
s.headers.update(headers)

# to get cookies
r = s.get("https://www.ryanair.com/")

payload = {
    "flight": "",
    "departure": "",
    "arrival": "",
    "minDepartureTime": "",
    "maxDepartureTime": ""
    }
    
    # "adultCount": 1,
    # "childCount": 0,
    # "infantCount": 0,
    # "wdc": True,
    # "dayInterval": 7


# get from https://wizzair.com/static/metadata.json
# in ['apiUrl']

# https://be.wizzair.com/7.8.3/Api/search/flightDates?departureStation=TLV&arrivalStation=VNO&from=2018-01-25&to=2018-03-28
# =>
# {"flightDates":["2018-01-27T00:00:00","2018-01-30T00:00:00","2018-02-03T00:00:00","2018-02-06T00:00:00","2018-02-10T00:00:00",
# "2018-02-13T00:00:00","2018-02-17T00:00:00","2018-02-20T00:00:00","2018-02-24T00:00:00","2018-02-27T00:00:00",
# "2018-03-03T00:00:00","2018-03-06T00:00:00","2018-03-10T00:00:00","2018-03-13T00:00:00","2018-03-17T00:00:00",
# "2018-03-20T00:00:00","2018-03-24T00:00:00","2018-03-27T00:00:00"]}

url = 'http://apigateway.ryanair.com/pub/v1/timetable/3/schedules/TLV/BGY/years/2018/months/02?apikey=tsVQ06jsOAWup17HPPkrQSZjon32yOik'

r = requests.post(url, json=payload)

print(r.text)

data = r.json()
# import pdb;pdb.set_trace()

#print(data['outboundFlights'][0]['flightNumber'])
# print(data['outboundFlights'][0]['departureStation'])
# print(data['outboundFlights'][0].get('departureDateTime'))
#print(type(data['outboundFlights'][0].values()))


# url2 = 'https://be.wizzair.com/7.8.2/Api/search/flightDates?departureStation=TLV&arrivalStation=VNO&from=2018-01-23&to=2018-03-26'
# r2 = requests.get(url)

