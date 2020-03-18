"""
Applications of Breadth First Traversal
1) Shortest Path and Minimum Spanning Tree for unweighted graph 
2) Peer to Peer Networks
3) Crawlers in Search Engines
4) Social Networking Websites
5) GPS Navigation systems
6) Broadcasting in Network
7) In Garbage Collection
8) Cycle detection in undirected graph
9) Ford–Fulkerson algorithm
10) To test if a graph is Bipartite
11) Path Finding
12) Finding all nodes within one connected component
"""
class Solution(object):
    def BFS_ShortestPath(graph, s, e):
        queue = []
        queue.append(s)
        seen = set()
        seen.add(s)
        parent ={s:None}
        shortestpath = []
        while (len(queue)>0):
            vertex = queue.pop(0)
            nodes = graph[vertex]
            for w in nodes:
                if w not in seen:
                    queue.append(w)
                    seen.add(w)
                    parent[w] = vertex
        for key, value in parent.items():
            print(key,value)
        while e != None:
            shortestpath.append(e)
            e = parent[e]
        print("shortest path")        
        print(shortestpath[::-1])
            
# graph = {
#     "A": ["B", "C"],
#     "B": ["A", "C", "D"],
#     "C": ["A", "B", "D", "E"],
#     "D": ["B", "C", "E", "F"],
#     "E": ["C", "D"],
#     "F": ["D"]
# }