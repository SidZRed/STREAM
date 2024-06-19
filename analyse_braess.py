def analyze_braess_paradox(G, source, destination, flow_distribution):
    results = {}

    # Remove each edge one by one and check if the shortest path length decreases
    for edge in list(G.edges):
        G_temp = G.copy()
        G_temp.remove_edge(*edge)
        update_edge_weights(G_temp, flow_distribution)
        new_path, new_length = find_shortest_path(G_temp, source, destination)
        results[f'remove_edge_{edge}'] = {
            'new_shortest_path': new_path,
            'new_shortest_length': new_length
        }

    # Add new edges from source to every other node (except destination) and check if shortest path length increases
    for node in G.nodes:
        if node != destination and not G.has_edge(source, node):
            G_temp = G.copy()
            G_temp.add_edge(source, node, base_weight=0, linear_factor=0, weight=0)
            update_edge_weights(G_temp, flow_distribution)
            new_path, new_length = find_shortest_path(G_temp, source, destination)
            results[f'add_edge_({source},{node})'] = {
                'new_shortest_path': new_path,
                'new_shortest_length': new_length
            }

    return results

if __name__ == "__main__":
    from build_graph import read_graph
    from update_weights import update_edge_weights
    from shortest_path import find_shortest_path
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

    # Analyze Braess's Paradox
    results = analyze_braess_paradox(G, source, destination, flow_data)

    for key, value in results.items():
        print(f"{key}: Path: {value['new_shortest_path']}, Length: {value['new_shortest_length']}")
