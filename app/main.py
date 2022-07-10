from logging import critical
from typing import List, Tuple
from critical_connections import CriticalConnections
from draw_graph import draw_graph

from fastapi import FastAPI, Response
from pydantic import BaseModel

app = FastAPI()


class Graph(BaseModel):
    nodes_number: int
    edges: List[Tuple[int, int]]


def normilize_edges(edges):
    aux_edges = edges.copy()

    for i in range(len(aux_edges)):
        edges[i] = tuple(sorted(aux_edges[i]))

    return edges


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/get-graph",
    responses = {
        200: {
            "content": {"image/png": {}}
        }
    },
    response_class=Response
)
def plot_graph(graph: Graph):

    graph.edges = normilize_edges(graph.edges)
    
    critical_connections = CriticalConnections().get_critical_connections(graph.nodes_number, graph.edges)

    img_bytes = draw_graph(graph, critical_connections)

    return Response(content=img_bytes.read(), media_type="image/png")
