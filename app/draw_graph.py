from turtle import color
from PIL import Image

import io
import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(graph, critical_adges):

    nodes = set([n1 for n1, n2 in graph.edges] + [n2 for n1, n2 in graph.edges])

    G=nx.Graph()

    for node in nodes:
        G.add_node(node)

    for edge in graph.edges:
        if edge in critical_adges:
            G.add_edge(edge[0], edge[1], color='r', weight=2)
        else:
            G.add_edge(edge[0], edge[1], color='g', weight=2)

    colors = nx.get_edge_attributes(G,'color').values()
    weights = nx.get_edge_attributes(G,'weight').values()

    pos = nx.planar_layout(G)
    nx.draw(G, pos, edge_color=colors, width=list(weights), with_labels=True)

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

    return buf