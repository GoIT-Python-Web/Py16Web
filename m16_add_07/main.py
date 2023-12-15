import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edge('A', "B", weight=7)
G.add_edge('A', "D", weight=6)
G.add_edge('B', "C", weight=8)
G.add_edge('B', "D", weight=10)
G.add_edge('B', "E", weight=7)
G.add_edge('C', "E", weight=5)
G.add_edge('D', "E", weight=17)
G.add_edge('D', "F", weight=9)
G.add_edge('E', "F", weight=7)
G.add_edge('E', "G", weight=9)
G.add_edge('F', "G", weight=13)

pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()
