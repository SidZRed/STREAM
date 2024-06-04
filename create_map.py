import os
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def create_map(map_file):
    with open(map_file, 'r') as f:
        