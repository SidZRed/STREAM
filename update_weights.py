import networkx as nx
import json

def weight_function(base_weight, linear_factor, flow):
    return base_weight + linear_factor * flow

def update_edge_weights(G, flows):
    for edge in G.edges:
        u, v = edge
        base_weight = G[u][v]['base_weight']
        linear_factor = G[u][v]['linear_factor']
        flow = flows.get((u, v), 0)
        G[u][v]['weight'] = weight_function(base_weight, linear_factor, flow)

if __name__ == "__main__":
    from build_graph import read_graph

    file_path = 'graph_data.json'
    G = read_graph(file_path)

    flow_path = 'graph_flow.json'
    with open(flow_path, 'r') as file:
        flow_data = json.load(file)['flows']
    update_edge_weights(G, flow_data)
    print("Updated edge weights:")
    print(G.edges(data=True))
