# -*- coding: utf-8 -*-
"""
Author: Traci
Date: 19 Nov 2019

This script returns the maximum number of rods to cut down without causing antimatter explosion.

Or in other words,
Returns the maximal number of edges to cut such that connectivity graph remains unchanged.

Example
-------
    $ python src/cut_down_rods.py
    > 1,2 3,4 4,5

Unit Test Example
-------
    $ pytest test/test_cut_down_rods.py -sv

"""

import networkx as nx
import matplotlib.pyplot as plt
import ast
import re

def get_num_edges_in_connected_components(networkx_graph, connected_components_list):
    """
    Returns a dict,
    key: vertex set of the connected component(s)
    value: number of edges in the connected component(s)
    """
    num_edges_in_connected_components = [0 for x in connected_components_list]

    # Count num edges for each connected component 
    for idx, connected_component in enumerate(connected_components_list):
        for edge_set in list(networkx_graph.edges):
            if set(edge_set[:2]).issubset(connected_component):
                num_edges_in_connected_components[idx] += 1
    return {str(component):num_edges for component, num_edges in zip(connected_components_list, num_edges_in_connected_components)}

def get_num_edges_in_spanning_tree(connected_components_list):
    """
    Returns a dict,
    key: vertex set of the connected component
    value: number of edges in spanning tree of the component
    
    Number of edges in a spanning tree = Number of vertices - 1
    """
    num_vertices_list = [len(c) for c in connected_components_list]
    num_edges_in_spanning_tree_list = [x-1 for x in num_vertices_list]
    return {str(component):num_edges for component, num_edges in zip(connected_components_list, num_edges_in_spanning_tree_list)}

def get_num_edges_to_cut(networkx_graph):
    """
    Returns the maximal number of edges to cut such that connectivity of graph remains unchanged.

    """
    # Get list of connected components
    connected_components_list = list(nx.connected_components(networkx_graph))

    # Get number of edges in each connected component
    num_edges_in_connected_components_dict = get_num_edges_in_connected_components(networkx_graph, connected_components_list)

    # Get number of edges in spanning tree of each connected component
    get_num_edges_in_spanning_tree_dict = get_num_edges_in_spanning_tree(connected_components_list)

    num_edges_to_cut_dict = dict.fromkeys(num_edges_in_connected_components_dict.keys(), 0)

    for item1, item2 in zip(num_edges_in_connected_components_dict.items(), 
                            get_num_edges_in_spanning_tree_dict.items()):
        num_edges_to_cut_dict[item1[0]] =  item1[1] - item2[1]

    num_edges_to_cut = sum(num_edges_to_cut_dict.values())
    return num_edges_to_cut

def is_input_valid(input_graph):
    """
    Returns boolean indicating validity of input

    Cases not allowed:
    - Float
    - Odd number of non-negative integers
    - Negative integers
    - vertex with edge to itself
    - too many/little commas
    - Vertex name is string-type
    """
    if re.findall(r'\d+\.\d+', input_graph):
        print('Float not allowed. Non-negative integers required!')
        return False
    if len(re.findall(r'[0-9]+', input_graph))%2 != 0:
        print('Even number of non-negative integers required!')
        return False
    if len(re.findall(r'[0-9]+', input_graph))/len(re.findall(r'\,', input_graph)) != 2:
        print('Commas defined wrongly!')
        return False
    for edge_set in input_graph.split():
        if len(set(ast.literal_eval(edge_set))) == 1:
            print('Vertex with edge to itself not allowed!')
            return False
        if len(edge_set) < 2:
            print('Edge set defined wrongly!')
            return False
        try:
            for y in edge_set.split(','):
                if int(y)<0:
                    print('Non-negative integers required1!')
                    return False
        except ValueError:
            print('Edge set defined wrongly!')
            return False
    return True

def cut_down_rods():
    """
    Returns the maximum number of rods to cut.
    Returns None if input is not valid.
    """
    input_graph = input()
    if is_input_valid(input_graph):
        input_graph_edge_list = [ast.literal_eval(x) for x in input_graph.split()]

        G = nx.MultiGraph()
        G.add_edges_from(input_graph_edge_list)
        num_edges_to_cut = get_num_edges_to_cut(G)

        return num_edges_to_cut

if __name__ == "__main__":
    print('Number of rods to cut: {}'.format(cut_down_rods()))
