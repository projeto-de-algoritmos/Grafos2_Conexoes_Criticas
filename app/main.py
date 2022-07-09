from typing import Union, List, Tuple

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
def plot_graph():

