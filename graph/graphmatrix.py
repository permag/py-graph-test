"""
Undirected graph with adjacency matrix.
"""

class Graph:

	def __init__(self):
		self._node_matrix = [[0 for x in range(5)] for x in range(5)]


	@property
	def node_matrix(self):
		return self._node_matrix


	def add_node(self, node_item):
		self._node_matrix[node_item-1][node_item-1] = 1


	def add_edge(self, src_node, targ_node):
		self._node_matrix[src_node-1][targ_node-1] = 1



graph = MyGraph()
graph.add_node(1)
graph.add_node(2)
graph.add_node(3)
graph.add_node(4)

graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 3)
graph.add_edge(2, 4)
graph.add_edge(4, 1)


print graph.node_matrix

