import networkx as nx
import json

def read_graph(file_path):
    G = nx.DiGraph()
    with open(file_path, 'r') as file:
        data = json.load(file)
        for edge in data['edges']:
            G.add_edge(
                edge['start'], 
                edge['end'], 
                base_weight=edge['base_weight'], 
                linear_factor=edge['linear_factor'],
                weight=edge['base_weight']  # Initial weight set to base_weight
            )
    return G

if __name__ == "__main__":
    file_path = 'graph_data.json'
    G = read_graph(file_path)
    print("Graph created from file:")
    print(G.edges(data=True))
