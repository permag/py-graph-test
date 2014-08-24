"""
Directed graph with adjacency list.
"""

class Graph:
    
    def __init__(self):
        self._node_dict = {}


    @property
    def node_dict(self):
        return self._node_dict


    def add_node(self, node_item):
        """ 
        node_item: node nr. value e.g. 1.
        _node_dict:
            key: node_item nr.
            value: [] (future endges to be added e.g. [2,3,4])

        """
        self._node_dict[node_item] = []  # add node_item in list here for directed graph


    def add_edge(self, src_node, targ_node):
        self._node_dict[src_node].append(targ_node)
