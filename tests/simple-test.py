from architectures.core import Graph, Cluster, Group, Node, Edge, Flow
from architectures.themes import Default, Clean

theme = Default(graph_attr_overrides={"splines": "ortho"})

with Graph("my architecture", theme=theme, show=True):
    with Cluster("Cluster A") as cluster_a:
        a = Node("A")
        b = Node("B")
        c = Node("C")
    with Cluster ("Cluster B") as cluster_b:
        d = Node("D")
        e = Node("E")
        f = Node("F")
    with Cluster("Cluster C") as cluster_c:
        g = Node("G")