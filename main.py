import networkx as nx
import json

from build_graph import read_graph
from update_weights import update_edge_weights
from shortest_path import find_shortest_path
from analyse_braess import analyze_braess_paradox

def main():
    # Load graph and flow data
    file_path = 'graph_data.json'
    G = read_graph(file_path)

    flow_path = 'graph_flow.json'
    with open(flow_path, 'r') as file:
        flow_data = json.load(file)['flows']
    update_edge_weights(G, flow_data)

    all_results = {}

    # Loop through each pair of nodes
    for source in G.nodes:
        for destination in G.nodes:
            if source != destination:
                print(f"Analyzing from {source} to {destination}...")
                results = analyze_braess_paradox(G, source, destination, flow_data)
                all_results[(source, destination)] = results

    # Save results to a file
    with open('braess_analysis_results.json', 'w') as outfile:
        json.dump(all_results, outfile, indent=4)

    print("Analysis complete. Results saved to 'braess_analysis_results.json'.")

if __name__ == "__main__":
    main()
