import networkx as nx
from wizzair_scraper import WizzairScraper as WS
import matplotlib.pyplot as plt


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
	print(map_of_dest)
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
	
	neib = G.neighbors('TLV')	
	print(list(neib))
	print(nx.is_tree(G)) 
	# print(neib.dict)
	# print(G.number_of_nodes())
	# print ('TLV' in G)
	# for item in G:
	# 	print(item) 

	# pos = nx.spring_layout(G)		
	# nx.draw(G,pos, font_size=16, with_labels=False)
	# plt.show()			
 
	



if __name__ == '__main__':
	main()