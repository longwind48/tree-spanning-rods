Author: Traci Lim

# How many rods can I cut?

This script returns the **maximum number of rods to cut down without risking an antimatter explosion**.



Or in other words,

Return the **maximal number of edges to cut such that connectivity of graph remains unchanged**.



# Example

```bash
$ python src/cut_down_rods.py
> 1,2 3,4 4,5

# Expected output
> Number of rods to cut: 0
```



# Unit Tests

```bash
$ pytest test/test_cut_down_rods.py -sv
```



# Algorithm

The idea is to keep removing edges that the do not change the connectivity of the graph. We know a spanning tree is a subgraph which includes all of the vertices of G​, with minimum possible number of edges. So we are essentially removing edges until we get to the spanning tree of G. In the case of G being disconnected, we just have to find all connected components, and its respective spanning tree. Since we do not need to enumerate which edges to remove, we can make use of the following theorems.

- Every connected component has at least 1 spanning tree.
- Any spanning tree has n-1 edges, where n​ is number of vertices.

Then,

![algo math](https://github.com/longwind48/tree_spanning_rods/blob/master/img/algo.png)

---

1. FInd the all connected components of input graph, using BFS.
2. Find total number of vertices and edges in each connected component.
3. Number of edges to cut = SUM_i(num_edges_in_component_i - num_edges_in_spanning_tree_of_component_i)



##  Before you go...

- I could've used a spanning tree algorithm but i figured this is more efficient in 

 terms of complexity.

- I used `networkx` library for defining graphs, and `nx.connected_components()` to find 

 connected components (they use breadth-first-search).

- I made many assumptions for the input graph. Look at docstrings for `is_input_valid()`. 
- In general, it takes in a multigraph with non-negative integers as vertex names.

- I would love to have a chat with the guy who came up with this. 

