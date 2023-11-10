# Представлення графа за допомогою списку суміжності
import networkx as nx

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

G = nx.Graph(graph)

# DFS
result_dfs = nx.dfs_tree(G, source="A")
print(list(result_dfs.edges()))

# BFS
result_bfs = nx.bfs_tree(G, source="A")
print(list(result_bfs.edges()))
