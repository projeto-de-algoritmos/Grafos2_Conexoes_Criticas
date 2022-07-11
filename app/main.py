import base64
from logging import critical
from typing import List, Tuple
from critical_connections import CriticalConnections
from draw_graph import draw_graph

from fastapi import FastAPI, Response
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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


@app.post("/get-graph")
def plot_graph(graph: Graph):

    graph.edges = normilize_edges(graph.edges)
    
    critical_connections = CriticalConnections().get_critical_connections(graph.nodes_number, graph.edges)

    img_bytes = draw_graph(graph, critical_connections)

    encoded_image_string = base64.b64encode(img_bytes.read())

    return {"image_string": encoded_image_string}
