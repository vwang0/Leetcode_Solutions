"""
0323. Number of Connected Components in an Undirected Graph
Medium

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:

Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4 

Output: 2
Example 2:

Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1
Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
"""
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = {x:[] for x in range(n)}
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
            
        res = 0
        for i in range(n):
            queue = [i]
            res += 1 if i in g else 0
            for j in queue:
                if j in g:
                    queue += g[j]
                    del g[j]

        return res