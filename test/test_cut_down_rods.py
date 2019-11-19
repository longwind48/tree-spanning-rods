import sys
import pytest

sys.path.append('./src')
from cut_down_rods import *


@pytest.mark.parametrize("input_string, expected_output",
                         [('1,2 3,4', {'{1, 2}': 1, '{3, 4}': 1}),
                          ('1,2 3,4 3,4', {'{1, 2}': 1, '{3, 4}': 2}),
                          ('1,2 3,4 4,5 5,1', {'{1, 2, 3, 4, 5}': 4}),
                          ('10,2 30,400 400,5 5,10', {'{2, 5, 10, 400, 30}': 4}),])
def test_get_num_edges_in_connected_components(input_string, expected_output):
    G = nx.MultiGraph()
    input_graph_edge_list = [ast.literal_eval(x) for x in input_string.split()]
    G.add_edges_from(input_graph_edge_list) 
    connected_components_list = list(nx.connected_components(G))

    assert get_num_edges_in_connected_components(G, connected_components_list) == expected_output

@pytest.mark.parametrize("input_string, expected_output",
                         [('1,2 3,4', {'{1, 2}': 1, '{3, 4}': 1}),
                          ('1,2 3,4 3,4', {'{1, 2}': 1, '{3, 4}': 1}),
                          ('1,2 3,4 4,5 5,1', {'{1, 2, 3, 4, 5}': 4}),
                          ('10,2 30,400 400,5 5,10', {'{2, 5, 10, 400, 30}': 4}),])
def test_get_num_edges_in_spanning_tree(input_string, expected_output):
    G = nx.MultiGraph()
    input_graph_edge_list = [ast.literal_eval(x) for x in input_string.split()]
    G.add_edges_from(input_graph_edge_list) 
    connected_components_list = list(nx.connected_components(G))
    assert get_num_edges_in_spanning_tree(connected_components_list) == expected_output

@pytest.mark.parametrize("input_string, expected_output",
                         [('1,2 3,4', 0), #disconnected
                          ('1,2 3,4 3,4', 1), #disconnected, multi-edge
                          ('1,2 3,4 3,4 3,4', 2), 
                          ('1,2 3,4 4,3', 1),
                          ('1,2 1,3 1,4', 0), #star
                          ('1,2 1,3 1,4 2,3 3,4 2,4', 3), #planar
                          ('1,2 3,4 4,5 5,1', 0), #cycle
                          ('1,2 1,3 1,4 2,3 2,4 3,4', 3), #complete
                          ('1,2 2,3 3,4 4,5 5,6', 0), #bipartitle
                          ('1,2 1,4 1,6 3,2 3,4 3,6 5,2 5,4 5,6', 4),]) #bipartite complete
def test_get_num_edges_to_cut(input_string, expected_output):
    G = nx.MultiGraph()
    input_graph_edge_list = [ast.literal_eval(x) for x in input_string.split()]
    G.add_edges_from(input_graph_edge_list) 
    assert get_num_edges_to_cut(G) == expected_output

