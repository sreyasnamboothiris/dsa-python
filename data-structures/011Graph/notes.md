# Graph

A Graph is a data structure that consists of a set of nodes (vertices) and a set of edges that connect pairs of nodes. Graphs are used to model relationships between objects, where the objects are represented as nodes and the relationships are represented as edges.

## Characteristics of Graph:
- **Vertex (Node):** A fundamental unit representing an entity in the graph.
- **Edge:** A connection between two vertices, representing a relationship between them.
- **Adjacent Vertices:** Two vertices are adjacent if they are connected by an edge.
- **Degree of a Vertex:** The number of edges incident to a vertex.
  - **In-degree:** Number of edges directed towards a vertex (in directed graphs).
  - **Out-degree:** Number of edges directed away from a vertex (in directed graphs).
- **Path:** A sequence of vertices where each adjacent pair is connected by an edge.
- **Cycle:** A path that starts and ends at the same vertex without repeating any edges or vertices.

## Types of Graphs:
- **Undirected Graph:** A graph where edges have no direction. The edge (u, v) is the same as (v, u).
- **Directed Graph (Digraph):** A graph where edges have a direction. The edge (u, v) is different from (v, u).
- **Weighted Graph:** A graph where each edge has a weight (cost) associated with it.
- **Unweighted Graph:** A graph where all edges have the same weight or no weight at all.
- **Cyclic Graph:** A graph that contains at least one cycle.
- **Acyclic Graph:** A graph that contains no cycles.
- **Connected Graph:** A graph in which there is a path between every pair of vertices.
- **Disconnected Graph:** A graph in which at least one pair of vertices is not connected by a path.
- **Bipartite Graph:** A graph whose vertices can be divided into two disjoint sets such that every edge connects a vertex in one set to a vertex in the other set.
- **Complete Graph:** A graph in which there is an edge between every pair of vertices.

## Graph Representation:
- **Adjacency Matrix:** A 2D array where the element at row `i` and column `j` is `1` (or the weight of the edge) if there is an edge between vertices `i` and `j`, and `0` if there is no edge.
  - **Space Complexity:** O(V^2) where `V` is the number of vertices.
  
- **Adjacency List:** An array of lists, where the `i`-th list contains all vertices adjacent to the `i`-th vertex.
  - **Space Complexity:** O(V + E) where `V` is the number of vertices and `E` is the number of edges.
  
- **Edge List:** A list of all edges in the graph, where each edge is represented as a pair of vertices.
  - **Space Complexity:** O(E)

## Graph Traversal:
- **Breadth-First Search (BFS):** Traverses the graph level by level, starting from a given vertex, and exploring all its neighbors before moving to the next level.
  - **Time Complexity:** O(V + E)
  - **Space Complexity:** O(V)
  
- **Depth-First Search (DFS):** Traverses the graph by going as deep as possible from a given vertex before backtracking to explore other vertices.
  - **Time Complexity:** O(V + E)
  - **Space Complexity:** O(V)

## Applications of Graphs:
- **Social Networks:** Modeling relationships between individuals (e.g., Facebook friends).
- **Routing Algorithms:** Finding the shortest path between nodes in a network (e.g., GPS navigation).
- **Web Crawlers:** Navigating links between pages on the internet.
- **Dependency Analysis:** Modeling dependencies in software or tasks (e.g., build systems).
- **Recommendation Systems:** Suggesting friends, products, or content based on connections in a graph.

## Graph Algorithms:
- **Dijkstra's Algorithm:** Finds the shortest path from a single source vertex to all other vertices in a weighted graph.
  - **Time Complexity:** O(V^2) or O((V + E) log V) with a priority queue
  
- **Bellman-Ford Algorithm:** Computes shortest paths from a single source vertex to all other vertices in a graph, which can have negative weights.
  - **Time Complexity:** O(VE)
  
- **Kruskal's Algorithm:** Finds the minimum spanning tree for a connected, undirected graph by selecting edges in order of increasing weight.
  - **Time Complexity:** O(E log E)
  
- **Prim's Algorithm:** Finds the minimum spanning tree for a weighted undirected graph, starting from a given vertex.
  - **Time Complexity:** O(V^2) or O(E log V) with a priority queue
  
- **Topological Sorting:** Ordering of vertices in a directed acyclic graph (DAG) such that for every directed edge (u, v), vertex `u` comes before `v`.
  - **Time Complexity:** O(V + E)

## Properties of Graphs:
- **Eulerian Path:** A path that visits every edge of the graph exactly once.
- **Eulerian Circuit:** An Eulerian path that starts and ends at the same vertex.
- **Hamiltonian Path:** A path that visits every vertex of the graph exactly once.
- **Hamiltonian Circuit:** A Hamiltonian path that starts and ends at the same vertex.

## Summary:
Graphs are a versatile data structure that can model a wide range of relationships and processes. Understanding their properties, representations, and traversal methods is crucial for solving complex problems in computer science, such as networking, scheduling, and optimization.

