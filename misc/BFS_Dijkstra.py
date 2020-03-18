"""
Dijkstra's algorithm (or Dijkstra's Shortest Path First algorithm, 
SPF algorithm)[2] is an algorithm for finding the shortest paths 
between nodes in a graph, which may represent, for example, 
road networks. It was conceived by computer scientist 
Edsger W. Dijkstra in 1956 and published three years later.

The algorithm exists in many variants. Dijkstra's original 
algorithm found the shortest path between two given nodes,
but a more common variant fixes a single node as the "source" 
node and finds shortest paths from the source to all other nodes 
in the graph, producing a shortest-path tree.
"""
import heapq
import math

graph = {
    "A": {"B": 5, "C": 1},
    "B": {"A": 5, "C": 2, "D": 1},
    "C": {"A": 1, "B": 2, "D": 4, "E": 8},
    "D": {"B": 1, "C": 4, "E": 3, "F": 6},
    "E": {"C": 8, "D": 3},
    "F": {"D": 6}
}

class Solution(object):
    def init_distance(graph, s):
        distance = {s: 0}
        for vertex in graph:
            if vertex != s:
                distance[vertex] = math.inf
        return distance

    def BFS_Dijkstra(graph, s):
        pqueue = []
        heapq.heappush(pqueue,(0, s))
        seen = set()
        seen.add(s)
        parent = {s: None}
        distance = init_distance(graph, s)

        while (len(pqueue) > 0):
            pair = heapq.heappop(pqueue)
            dist = pair[0]
            vertex = pair[1]
            seen.add(vertex)
            nodes = graph[vertex].keys()
            for w in nodes:
                if w not in seen:
                    if dist + graph[vertex][w] < distance[w]:
                        heapq.heappush(pqueue, (dist + graph[vertex][w], w))
                        parent[w] = vertex
                        distance[w] = dist + graph[vertex][w]
        return parent, distance