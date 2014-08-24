#!/usr/bin/env python
from graph.graphlist import Graph as GraphList

def test_graph_list():
    graph = GraphList()
    graph.add_node(1)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    print graph.node_dict


def main():
    test_graph_list()


if __name__ == '__main__':
    main()