"""
BFS vs DFS for Binary Tree
What are BFS and DFS for Binary Tree?
A Tree is typically traversed in two ways:

Breadth First Traversal (Or Level Order Traversal)


Depth First Traversals
Inorder Traversal (Left-Root-Right)
Preorder Traversal (Root-Left-Right)
Postorder Traversal (Left-Right-Root)

"""
class Solution(object):
    def BFS(graph, s):
        queue = []
        queue.append(s)
        seen = set()
        seen.add(s)
        while (len(queue)>0):
            vertex = queue.pop(0)
            nodes = graph[vertex]
            for w in nodes:
                if w not in seen:
                    queue.append(w)
                    seen.add(w)
            print(vertex)
            
graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}