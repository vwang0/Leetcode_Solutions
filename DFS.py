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
    def DFS(graph, s):
        stack = []
        stack.append(s)
        seen = set()
        seen.add(s)
        while (len(stack)>0):
            vertex = stack.pop()
            nodes = graph[vertex]
            for w in nodes:
                if w not in seen:
                    stack.append(w)
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