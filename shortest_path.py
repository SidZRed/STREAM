import networkx as nx

def find_shortest_path(G, source, destination):
    return nx.dijkstra_path(G, source, destination), nx.dijkstra_path_length(G, source, destination)

if __name__ == "__main__":
    from build_graph import read_graph
    from update_weights import update_edge_weights
    import json

    # Load graph and flow data
    file_path = 'graph_data.json'
    G = read_graph(file_path)

    flow_path = 'graph_flow.json'
    with open(flow_path, 'r') as file:
        flow_data = json.load(file)['flows']
    update_edge_weights(G, flow_data)

    # Prompt user for source and destination
    source = input("Enter the source node: ")
    destination = input("Enter the destination node: ")

    new_path, new_length = find_shortest_path(G, source, destination)
    print("Shortest path for new person:", new_path)
    print("Length of the shortest path:", new_length)
