# CSA1706-AI
bfs-1
BFS(G, start)

1. Create an empty queue Q
2. Create a visited array
3. Mark start as visited
4. Insert start into Q

5. While Q is not empty:
      a. Remove a vertex from Q
      b. Print the vertex

      c. For each adjacent vertex:
            If it is not visited:
                Mark it as visited
                Insert it into Q

6. Stop
dfs-1

DFS(G, vertex)

1. Mark vertex as visited
2. Print vertex

3. For each adjacent vertex:
      If it is not visited:
          DFS(G, adjacent vertex)

4. Stop
bfs-3

BFS(Graph, Start)

1. Create an empty Queue
2. Create an empty Visited set
3. Add Start to Queue
4. Mark Start as Visited

5. While Queue is not empty:
      a. Remove a vertex from Queue
      b. Print the vertex

      c. For each adjacent vertex:
            If vertex is not Visited:
                Mark vertex as Visited
                Add vertex to Queue

6. Stop
dfs-3

DFS(Graph, Vertex)

1. Mark Vertex as Visited
2. Print Vertex

3. For each adjacent vertex:
      If vertex is not Visited:
          DFS(Graph, vertex)

4. Stop
bfs-4

BFS(Graph, Start)

1. Create Queue
2. Create Visited array
3. Add Start vertex to Queue
4. Mark Start as Visited

5. While Queue is not empty:
      vertex ← Remove from Queue
      Print vertex

      For each adjacent vertex of vertex:
          If vertex is not Visited:
              Mark it Visited
              Add it to Queue

6. Stop

dfs-4

DFS(Graph, Vertex)

1. Mark Vertex as Visited
2. Print Vertex

3. For each adjacent vertex of Vertex:
      If vertex is not Visited:
          DFS(Graph, vertex)

4. Stop
