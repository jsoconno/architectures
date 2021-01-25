from architectures.core import Graph, Cluster, Group, Node, Edge, Flow

# Import the LightMode theme
from architectures.themes import Default, LightMode

theme = LightMode(graph_attr_overrides={"rankdir": "TB"})

with Graph("My Graph", theme=theme, show=True) as graph:
    with Cluster("A") as cluster_a:
        a = Node("A")

    with Cluster("B") as cluster_b:
        b = Node("B")
        c = Node("C")
        d = Node("D")
        e = Node("E")
        f = Node("F")
        collection = [b, c, d]
        with Cluster():
            g = Node("G")

    Flow([a, collection, e, f])