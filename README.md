# Dijkstra-s-algorithm
Dijkstra's algorithm in python

The task is to find the optimal path between different pairs of points in a given road network. Input is received on standard input separated by tabs (\t) and new lines (\n) in the following order:

- the number of pairs of points between which the path must be found (p)
- number of the nodes in the graph (n)
- number of the links in the graph (e)
- empty line

- (p) lines, each of them contains two integers separated by a tab. The first number represents the ID of the starting node and the second is the ID of the the destination node
- empty line

- (n) lines, each of them contains two integers separated by a tab. The first number is the x and the second number is the y coordinate of the point. The first line describes the 0th node and so on
- empty line

- (e) lines, each of them contains two integers separated by a tab. The two numbers indicate which intersections the given road section belongs to. All roads are two-way. The length of the road is the distance between its two endpoints as the crow flies.


For each of the p routes, the optimal route according to the route length must be calculated while traveling in the given road network.

The solution must be written to the standard output. The output is a tab-separated line containing (p) numbers, where the numbers are the lengths of the shortest path. The result must be entered with two decimal places.

Example input:

2
3
3

0 2
1	2

2	0
-4	1
6	3

1	0
1	2
0	2

In the example input, 2 routes need to be calculated, there are 3 intersections (nodes) and 3 links on the map. Route 1 must be calculated from 0 to the node with ID 2. Identifiers and coordinates of nodes: 0: (2,0), 1: (-4,1), 2: (6,3). The links runs between node 1-0, 1-2 and 0-2, their lengths are: 6.08, 10.20 and 5.0.

Since our network is triangular, the optimal path is the direct path between the nodes. So the output for the example is:
5.00	10.20
