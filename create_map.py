import os
import json
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def create_map(map_file):
    G = nx.DiGraph()
    with open(map_file, 'r') as f:
        graph_data = json.load(f)
        for edge in graph_data['edges']:
            G.add_edge(edge['start'], edge['end'], base_weight=edge['base_weight'], linear_factor=edge['linear_factor'])
    return G

if __name__ == "__main__":
    map_file = "graph_data.json"
    G = create_map(map_file)
    print("Graph created successfully")

