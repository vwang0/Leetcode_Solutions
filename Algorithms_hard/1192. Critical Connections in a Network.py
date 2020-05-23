'''
1192. Critical Connections in a Network
There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.

Example 1:

Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
 
Constraints:

1 <= n <= 10^5
n-1 <= connections.length <= 10^5
connections[i][0] != connections[i][1]
There are no repeated connections.
'''
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def graph(connections):
            from collections import defaultdict
            g = defaultdict(list)
            for u, v in connections:
                g[u].append(v)
                g[v].append(u)
            return g

        g = graph(connections)
        n = len(g.keys()) # no of nodes

        self.id = 0
        ids = [0]*(n+1)
        lows = [0]*(n+1)
        visited = set()

        def dfs(at, parent, bridges):
            visited.add(at)
            self.id = self.id + 1
            lows[at] = ids[at] = self.id

            for to in g[at]:
                if to==parent: continue
                if to not in visited:
                    dfs(to, at, bridges)
                    lows[at] = min(lows[at], lows[to])
                    if ids[at]<lows[to]:
                        bridges.append([at, to])
                else:
                    # since a back edge find the lowest id at can reach 
                    lows[at] = min(lows[at], ids[to])
        bridges = []
        for i in range(n):
            if i not in visited:
                dfs(i, -1, bridges)

        return bridges        


