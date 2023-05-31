#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Search Algorithms implementation
"""


import graph as G
import queue as Q


def breadth_check(queue, destination, visited, parents):
    """
    Helper function for BFS search.Gets every node in queue.
    Gets its neighbours checks wether visited and put new ones in queue
    
    Args:
        queue (Queue): queue object instance keep tracking of nodes to be visited with FIFO mechanism.
        destination (Vertex):The vertex at the end point.
        visited (list):list of verticies visited during search
        parents (dict): A dictionary containing keys of vertices names and value of parent nodes.
    """    
    vertex = queue.get()
    print("Visiting: ", vertex.name)
    if (vertex== destination):
        return True, vertex    
    for child_tup in vertex.get_neighbours():
        child,cost = child_tup
        if child not in visited:
            parents[child.name] = vertex  
            visited.append(child)
            print(f"    Adding to queue {child.name} ")
            queue.put(child)
    return False


def make_path(parents, vertex):
    """
    makes parents from start toward destination
    
    Args:
        parents (dict) : A dictionary containing keys of vertices names and value of parent nodes.
        vertex (Vertex): The vertex on the destination.
    """    
    path = f"{vertex.name}"
    
    while parents[vertex.name] is not None:
        vertex = parents[vertex.name]
        path = f"{vertex.name} -> " + path       
    return path
    

def breadth_first_search(start, destination):
    """
    Does BFS search by FIFO queue through breadth_check helper function
    
    Args:
        start (Vertex): The vertex on the starting point.
        destination (Vertex): The vertex on the end point.
    """
    print('\nPerforming BFS ')    
    found = False 
    queue = Q.Queue()
    queue.put(start)
    visited = [start]
    parents = {start.name:None}
    while found == False:
        found = breadth_check(queue, destination, visited, parents)
        
    print("The path to the destination is :")
    print(make_path(parents, destination))  
    
    
def depth_first_search(start, destination):
    """
    Does DFS search by stack mechanism through depth_check helper function
    
    Args:
        start (Vertex): The vertex on the starting point.
        destination (Vertex): The vertex on the end point.
    """ 
    print('\nPerforming DFS')   
    found = False 
    queue = Q.LifoQueue()
    queue.put(start)
    visited = [start]
    parents = {start.name: None}
    while found == False:
        found = depth_check(queue, destination,visited, parents)
        
    print("The path to the destination is :")
    print(make_path(parents, destination))
    
    
def depth_check(queue, destination,visited, parents):
    """
    Helper function for DFS search.Gets every node in queue.
    Gets its neighbours checks wether visited and put new ones in queue
    
    Args:
        queue (Queue): queue object instance keep tracking of nodes to be visited with stack mechanism.
        destination (Vertex):The vertex at the end point.
        visited (list):list of verticies visited during search
        parents (dict): A dictionary containing keys of vertices names and value of parent nodes.
    """  
    vertex = queue.get()
    print("Visiting: ", vertex.name)
    if (vertex== destination):
        return True, vertex    
    for child_tup in vertex.get_neighbours():
        child,cost = child_tup
        if child not in visited:  
            parents[child.name] = vertex
            visited.append(child)
            print(f"    Adding to queue {child.name}")
            queue.put(child)
    
    return False


def uniform_cost_search(start, destination):
    """
    Does UCS search by queue priority mechanism through uniform_check helper function
    
    Args:
        start (Vertex): The vertex on the starting point.
        destination (Vertex): The vertex on the end point.
    """    
    print('\nPerforming UCS ')
    found = False 
    queue = Q.PriorityQueue()
    queue.put((0,start))
    visited = [start]
    parents = {start.name: None}
    while found == False:
        found = uniform_check(queue, destination, visited, parents)
        
    print("The path to the destination is :")
    print(make_path(parents, destination))
    
    
def uniform_check(queue,destination, visited, parents):
    """
    Helper function for UCS search.Gets every node in queue.
    Gets its neighbours.Priorotises through total cost of current node and the previous ones in the path
    
    Args:
        queue (Queue): queue object instance keep tracking of nodes to be visited with stack mechanism.
        destination (Vertex):The vertex at the end point.
        visited (list):list of verticies visited during search
        parents (dict): A dictionary containing keys of vertices names and value of parent nodes.
    """    
    cost,vertex = queue.get()
    print("Visiting: ", vertex.name)
    if vertex== destination:
        return True, vertex    
    for child_tup in vertex.get_neighbours():
        child,edge_cost = child_tup
        if ((child not in visited) or ((child in visited) & (child.total_cost>cost))) :
            # second part of condition is necessary for visiting nodes
            # that are visited but have lower cost so they can be the optimal path
            parents[child.name] = vertex
            visited.append(child)
            total_cost= cost+edge_cost
            child.total_cost = total_cost
            # total cost for comparing objects in PriorityQueue algorithm
            print(f"Adding to queue {child.name} with cost {edge_cost}")
            queue.put((total_cost,child))
    return False