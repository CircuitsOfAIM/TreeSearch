#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from search import breadth_first_search as BFS
from search import depth_first_search as DFS
from search import uniform_cost_search as UCS
import graph
import queue


class improvedvertex(graph.Vertex):
    def get_neighbours(self):
    	# overwrites get_neighbour method to return vertex obj instead of vertex name
        neighbours = [(edge.destination, edge.cost) for edge in self.edges]
        return neighbours
    def __init__(self,name):
        super().__init__(name)
        self.total_cost =0
    def __lt__(self,other):
        # use total cost as an priority thus comparison factor
        self.total_cost <= other.total_cost

graph.Vertex = improvedvertex

# initiating graph object based on figure 1 structure
test_graph = graph.Graph()
# adding vertices to graph
test_graph.add_vertex('A')
test_graph.add_vertex('B')
test_graph.add_vertex('C')
test_graph.add_vertex('D')
test_graph.add_vertex('E')
test_graph.add_vertex('F')
test_graph.add_vertex('G')
# adding edges to the vertices
test_graph.add_edge('A','B',2)
test_graph.add_edge('A','C',1)
test_graph.add_edge('A','D',1)
test_graph.add_edge('A','G',6)
test_graph.add_edge('C','E',1)
test_graph.add_edge('D','F',1)
test_graph.add_edge('G','F',3)

# print(test_graph)

# search.uniform_cost_search(test_graph.vertices['B'],test_graph.vertices['G'])

BFS(test_graph.vertices['B'],test_graph.vertices['G'])
DFS(test_graph.vertices['B'],test_graph.vertices['G'])
UCS(test_graph.vertices['B'],test_graph.vertices['G'])




