import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()


G.add_node('A')
G.add_nodes_from(["B", "C", "D"])
G.add_edge('A', 'B')
G.add_edges_from([("A", "C"), ("B", "C"), ("B", "D")])

print(G.nodes())
print(G.edges())
print(list(G.neighbors('B')))

# G.remove_node('B')
# G.remove_edge("A", "B")

DG = nx.DiGraph(G)
DG.remove_edge("A", "B")

DG.add_node(1)
DG.add_edge(1, "A", weight=2.5, label='connection')
DG.nodes[1]['color'] = 'green'

print(DG.number_of_edges())
print(DG.number_of_nodes())

print(nx.degree_centrality(DG))  # Ступінь центральності
print(nx.closeness_centrality(DG))  # Близькість вузла
print(nx.betweenness_centrality(DG))  # Наскільки вузол є 'міст' між вузлами

print(nx.shortest_path(DG, source="B", target="A"))  #

# Drawing the graph
plt.figure(figsize=(6, 6))
pos = nx.spring_layout(DG, seed=42)
nx.draw(DG, pos=pos, with_labels=True, node_size=700, node_color='skyblue', font_size=15, width=2)
plt.show()
