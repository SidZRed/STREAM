import matplotlib.pyplot as plt
import networkx as nx

def visualize_graph(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=10, font_weight="bold")
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()

if __name__ == "__main__":
    from build_graph import read_graph

    file_path = 'graph_data.json'
    G = read_graph(file_path)
    visualize_graph(G)