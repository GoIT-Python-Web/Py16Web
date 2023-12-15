import networkx as nx
import matplotlib.pyplot as plt

def kruskal(graph: nx.Graph):
    forest = nx.Graph()
    for node in graph.nodes():
        forest.add_node(node)

    sorted_edges = sorted(graph.edges(data=True), key=lambda t: t[2].get('weight', 1))
    mst = nx.Graph()

    for edge in sorted_edges:
        u, v, weight = edge
        if not nx.has_path(forest, u, v):
            forest.add_edge(u, v)
            mst.add_edge(u, v, weight=weight["weight"])

    return mst


if __name__ == '__main__':

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
    # print(G.edges(data=True))
    mst = kruskal(G)

    for edge in mst.edges(data=True):
        print(edge)

    pos = nx.spring_layout(mst, seed=42)
    nx.draw(mst, pos, with_labels=True)
    labels = nx.get_edge_attributes(mst, 'weight')
    nx.draw_networkx_edge_labels(mst, pos, edge_labels=labels)
    plt.show()