import pprint
import networkx as nx
import matplotlib.pyplot as plt
import network_analysis as netw
from networkx import edge_betweenness_centrality as betweenness

# create an empty graph
G = nx.DiGraph()

UG = nx.Graph()

# add nodes
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)

# add edges
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 1)
G.add_edge(4, 1)
G.add_edge(5, 4)
G.add_edge(5, 1)

# add nodes
UG.add_node(2)
UG.add_node(3)
UG.add_node(4)
UG.add_node(1)
UG.add_node(5)

# add edges
UG.add_edge(1, 2)
UG.add_edge(2, 3)
UG.add_edge(3, 1)
UG.add_edge(4, 1)
UG.add_edge(5, 4)
UG.add_edge(5, 1)

print("Node degree:")
for node in G.nodes():
   print(f"{node}: {G.degree(node)}")
# clustering coefficient
print("Node clustering coefficient:")
for node in G.nodes():
   print(f"{node}: {nx.clustering(G, node)}")

# draw the graph
nx.draw(G, with_labels=True)
plt.show()


# netw.identify_key_nodes(G)
# PageRank
netw.analyze_transaction(G)

netw.betweenness_centrality(G)

netw.community_detection(UG)

# rc = nx.rich_club_coefficient(UG, normalized=True)
# print(rc[0])

def most_central_edge(G):
    centrality = betweenness(G, weight="weight")
    return max(centrality, key=centrality.get)

def plot_degree_dist(G):
    degrees = [G.degree(n) for n in G.nodes()]
    plt.hist(degrees)
    plt.show()

# plot_degree_dist(UG)
# plot_degree_dist(nx.gnp_random_graph(100, 0.5, directed=True))

comp = nx.community.girvan_newman(G, most_valuable_edge=most_central_edge)
print(tuple(sorted(c) for c in next(comp)))