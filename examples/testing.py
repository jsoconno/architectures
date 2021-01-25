from architectures.core import Graph, Cluster, Group, Node, Edge, Flow

# Import the LightMode theme
from architectures.themes import Default, LightMode

theme = LightMode(graph_attr_overrides={"rankdir": "TB"})

with Graph("My Graph", theme=theme, show=True) as graph:
    with Cluster("A") as cluster_a:
        a = Node("A")
        b = Node("B")

    with Cluster("B") as cluster_b:
        c = Node("C")
        with Cluster("A"):
            d = Node("D")

    Flow([[a, b], cluster_b])