from architectures.core import Graph, Cluster, Group, Node, Edge, Flow

# Import the LightMode theme
from architectures.themes import Default, LightMode

theme = LightMode()

with Graph("My Graph", theme=theme):
    with Cluster():
        Flow(
            [
                Node("A"), 
                [
                    Node("B"),
                    Node("C"),
                    Node("D")
                ],
                Node("E")
            ]
        )