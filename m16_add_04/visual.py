import matplotlib.pyplot as plt
import networkx as nx

G = nx.complete_graph(6)

options = {
    "node_color": "#D35400",
    "edge_color": "#1B4F72",
    "node_size": 500,
    "width": 3,
    "with_labels": True,
    "pos": nx.shell_layout(G, [[0, 1, 2], [3], [4, 5]]),
}

nx.draw(G, **options)
plt.title('Shell layout')
plt.show()
