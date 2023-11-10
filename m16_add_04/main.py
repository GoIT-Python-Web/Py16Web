# Importing necessary libraries for plotting the graph
import matplotlib.pyplot as plt
import networkx as nx

# Представлення графа за допомогою списку суміжності
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


# Creating a new graph object
G = nx.Graph(graph)

# Drawing the graph
plt.figure(figsize=(6, 6))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos=pos, with_labels=True, node_size=700, node_color='skyblue', font_size=15, width=2)
plt.show()
