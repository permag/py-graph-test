#!/usr/bin/env python
from graph.graphlist import Graph as GraphList
from graph.graphmatrix import Graph as GraphMatrix


def test_graph_list():
    graph = GraphList()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    print graph.node_dict


def test_graph_matrix():
    graph = GraphMatrix()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    print graph.node_matrix


def main():
    test_graph_list()
    test_graph_matrix()


if __name__ == '__main__':
    main()
