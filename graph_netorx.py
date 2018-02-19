import networkx as nx
from wizzair_scraper import WizzairScraper as WS
import matplotlib.pyplot as plt
import requests


def main():
	G = nx.DiGraph()
	scraper = WS()
	all_dest = WS.get_destinations_cities(scraper)
	# G.add_nodes_from(all_dest)

	# all_conection ={}
	# # all_dest = WS.get_destination_map(scraper)
	# for city in all_dest:
	# 	connection = WS.get_destination_map(scraper) 
	# all_connection.city = connection	
	# print(all_connection)
	api_url = 'https://be.wizzair.com/7.8.6/Api'
	url = f'{api_url}/asset/map?languageCode=en-gb'

        
	r = scraper.session.get(url)
	map_of_dest = r.json()
	print(len(map_of_dest['cities']))
	data = map_of_dest['cities']
	for city in  range(len(data)):
		G.add_node(data[city]['iata'], pos = (data[city]['longitude'], data[city]['latitude']))
		 # print(map_of_dest['cities'][city]['longitude'])
		 # print(map_of_dest['cities'][city]['latitude'])
	destination = dict()

	for city in map_of_dest['cities']:
		city_iata_code = city['iata']
		a = []
		destination[city_iata_code] = a
		for connection in city['connections']:
			a.append(connection['iata'])
	# print (destination) 

	

	# G.add_nodes_from(list(destination))
	for x,y in destination.items():
	# 	# print(x)
	# 	G.add_node(x)	
		for i in range(len(y)):
		# 	# print(x,y[i]) 
			G.add_edge(x,y[i]) 
	# print(list(G.edges()))	
	# print(list(G.nodes()))	
	# for node in  range (len(list(G.nodes()))): print(G.node['longitude'])
	nodes = G.nodes.data()
	# for i in nodes: print(i[1]) 
	
	neib = G.neighbors('TLV')	
	# print(list(neib))
	# print(nx.get_node_attributes(G, 'pos').items())
	# # for i in range(len(neib))
	# for city in neib:
	# pos = {city:(lon,lat) for (city, (lat, lon)) in nx.get_node_attributes(G, 'pos').items()}	
	# nx.draw_networkx_edges(G, pos, with_labels=True, node_size=0)
	# plt.show() 

	# print(nx.is_tree(G)) 
	# print(neib.dict)
	# print(G.number_of_nodes())
	# print ('TLV' in G)
	# for item in G:
	# 	print(item) 
	
	pos = {city:(lon,lat) for (city, (lat, lon)) in nx.get_node_attributes(G, 'pos').items()}
	# print(pos.keys())
	# print(pos)
	
	pos1 ={ x:pos[x] for x in list(neib)}
	print (pos1)
	while True:
		try:
			nx.draw_networkx_nodes(G, pos1, with_labels=True, node_size=0)
			plt.show() 
			break
		except Exception as e:
			print('KOOKO')
			raise
	
		
	nx.draw_networkx_nodes(G, pos1, with_labels=True, node_size=0)
	plt.show() 
		

	# print(pos1)
	# print(pos)
	# if pos['MAD']: 
	# nx.draw_networkx(G, pos, with_labels=True, node_size=0)
	# plt.show()			
	# url2 = f'{api_url}/search/search/'
	# r2 = requests.get(url2)
	# m = r2.json()
	# print(m)
	



if __name__ == '__main__':
	main()