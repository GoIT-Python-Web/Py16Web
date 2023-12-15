from heapq import heappop, heappush

import networkx as nx
import matplotlib.pyplot as plt


def prima(graph: nx.Graph):
    mst = nx.Graph()
    visited = {list(graph.nodes())[0]}

    edges = []
    for u, v, weight in graph.edges(data='weight', nbunch=visited):
        heappush(edges, (weight, u, v))
    print(edges)
    while visited != set(graph.nodes()):
        weight, u, v = heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.add_edge(u, v, weight=weight)
            for _, new_v, new_weight in graph.edges(data='weight', nbunch=[v]):
                if new_v not in visited:
                    heappush(edges, (new_weight, v, new_v))

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
    mst = prima(G)

    for edge in mst.edges(data=True):
        print(edge)

    pos = nx.spring_layout(mst, seed=42)
    nx.draw(mst, pos, with_labels=True)
    labels = nx.get_edge_attributes(mst, 'weight')
    nx.draw_networkx_edge_labels(mst, pos, edge_labels=labels)
    plt.show()
