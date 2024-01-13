import networkx as nx
import community as cmnty
import community as community_louvain
import matplotlib.pyplot as plt
import csv


# Create an empty directed graph
G = nx.DiGraph()

def build_network_graph(transaction_data):
    # Add nodes from the graph
    for transaction in transaction_data:
        G.add_node(transaction['from'])
        G.add_node(transaction['to'])

    # Add edges from the graph
    for transaction in transaction_data:
        G.add_edge(transaction['from'], transaction['to'], weight=transaction['value'])


def analyze_transaction(G):
    # Calculate PageRank scores
    pagerank_scores = nx.pagerank(G)


    # Print the fromp 10 nodes with the highest PageRank scores
    fromp_nodes = sorted(pagerank_scores, key=pagerank_scores.get, reverse=False)
    for node in fromp_nodes:
        print(f"Node: {node}, PageRank Score: {pagerank_scores[node]}")


def identify_key_nodes(G):
    # Calculate node degrees
    node_degrees = G.degree()

    # Print the fromp 10 nodes with the highest degrees
    fromp_nodes = sorted(node_degrees, key=node_degrees.get, reverse=True)[:10]
    for node in fromp_nodes:
        print(f"Node: {node}, Degree: {node_degrees[node]}")


def betweenness_centrality(G):
    # Calculate betweenness centrality
    betweenness_scores = nx.betweenness_centrality(G)


    # Print the fromp 10 nodes with the highest betweenness centrality scores
    fromp_nodes = sorted(betweenness_scores, key=betweenness_scores.get, reverse=True)[:10]
    for node in fromp_nodes:
        print(f"Node: {node}, Betweenness Centrality: {betweenness_scores[node]}")


def community_detection(G):
    # Apply community detection algorithm (Louvain)
    partition = cmnty.best_partition(G)
    # partition = community_louvain.best_partition(G)

    # Print the nodes and their corresponding community assignments
    for node, community_id in partition.items():
        print(f"Node: {node}, Community: {community_id}")


csv_file_path = "/home/sunilkarki/Documents/Persn/CProj/bnp/data/transactions1.csv"


with open(csv_file_path, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)

    # i=0
    for row in csv_reader:
        node1, node2 = row[2], row[3]
        # print(node1)
        # i+=1
        # if i > 5: break
        G.add_node(node1)
        G.add_node(node2)
        G.add_edge(node1, node2)


# Analyzing transction
print("Analayzing transaction")
analyze_transaction(G)

# draw the graph
nx.draw(G, with_labels=True)
plt.show()

print("Completed...")
