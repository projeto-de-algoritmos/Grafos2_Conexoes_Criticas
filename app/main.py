from logging import critical
from typing import List, Tuple
from critical_connections import CriticalConnections
from draw_graph import draw_graph

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Graph(BaseModel):
    nodes_number: int
    edges: List[Tuple[int, int]]


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/get-graph")
def plot_graph(graph: Graph):

    print(graph.edges)
    
    critical_connections = CriticalConnections().get_critical_connections(graph.nodes_number, graph.edges)
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(critical_connections)

    draw_graph(graph, critical_connections)

    return None
