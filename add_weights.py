import os
import json
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def weight_function(base_weight, linear_factor, flow):
    return base_weight + linear_factor * flow

def update_edge_weights(G, flows):
    for edge in G.edges:
        u, v = edge
        base_weight = G[u][v]['base_weight']
        linear_factor = G[u][v]['linear_factor']
        flow = flows.get((u, v), 0)
        G[u][v]['weight'] = weight_function(base_weight, linear_factor, flow)