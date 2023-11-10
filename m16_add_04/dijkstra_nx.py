import networkx as nx

# Створення графа
G = nx.Graph()

# Додавання міст і доріг
G.add_edge('A', 'B', weight=5)
G.add_edge('A', 'C', weight=10)
G.add_edge('B', 'D', weight=3)
G.add_edge('B', 'C', weight=1)
G.add_edge('C', 'D', weight=2)
G.add_edge('D', 'E', weight=4)

# Застосування алгоритму Дейкстри
shortest_paths = nx.single_source_dijkstra_path(G, source='A')
shortest_path_lengths = nx.single_source_dijkstra_path_length(G, source='A')

print(shortest_paths)  # виведе найкоротші шляхи від вузла 'A' до всіх інших вузлів
print(shortest_path_lengths)  # виведе довжини найкоротших шляхів від вузла 'A' до всіх інших вузлів