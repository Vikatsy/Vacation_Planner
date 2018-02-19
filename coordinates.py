import math 

def distance(node1, node2):
	R_EARTH = 6373
	lat1 = math.radians(node1.lat)
	lon1 = math.radians(node1.long)

	lat2 = math.radians(node2.lat)
	lon2 = math.radians(node2.long)

	dlon = lon2 - lon1 
	dlat = lat2 - lat1 

	a = (math.sin(dlat/2))**2 + math.cos(lat1) * math.cos(lat2) * (math.sin(dlon/2))**2 
	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a)) 
	d = R_EARTH * c 
	return d


class Node():
	def __init__(self, long, lat):
		self.long = long
		self.lat = lat


class Vertex():
	def __init__(self, _from, _to):
		self._from = _from
		self._to = _to

class Graph():
	def __init__(self, nodes, vertices):
		self.nodes = nodes
		self.vertices = vertices


nodes = {}

if not "TIA" in nodes:
	nodes['TIA'] = Node(19.720555555555553, 41.414722222222224)

vertices = []

vertices.append( ("TIA", "BUD") )

vertices.append( ("TIA", "LTN") )

graph = Graph(nodes=nodes, vertices=vertices)

tia_bud_distance = distance(nodes["TIA"], nodes["BUD"])






