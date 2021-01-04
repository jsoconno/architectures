from architectures.core import Graph, Cluster, Group, Node, Edge
from architectures.themes import Default, Clean

theme = Default()

with Graph("my architecture", theme=theme, show=True):
    with Cluster("Cluster A") as cluster_a:
        a = Node("A")
        b = Node("B")
        c = Node("C")
    with Cluster ("Cluster B") as cluster_b:
        d = Node("D")
        e = Node("E")
        f = Node("F")

    Edge(a, b)
    Edge([b, c], f)
    Edge(cluster_a, cluster_b)
