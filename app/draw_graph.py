from turtle import color
import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(graph, critical_adges):

    # extract nodes from graph
    nodes = set([n1 for n1, n2 in graph.edges] + [n2 for n1, n2 in graph.edges])

    # create networkx graph
    G=nx.Graph()

    # add nodes
    for node in nodes:
        G.add_node(node)

    # add edges
    for edge in graph.edges:
        print(edge)
        if edge in critical_adges:
            print("Entrou aqui")
            G.add_edge(edge[0], edge[1], color='r')
        else:
            G.add_edge(edge[0], edge[1], color='b')

    # draw graph
    colors = nx.get_edge_attributes(G,'color').values()

    pos = nx.circular_layout(G)
    nx.draw(G, pos, edge_color=colors)

    # show graph
    plt.savefig("path.png")