from architectures.core import Graph, Cluster, Group, Node, Edge, Flow

# Import the LightMode theme
from architectures.themes import Default, LightMode

theme = LightMode()

with Graph("My Graph", theme=theme):
    with Cluster() as cluster_a:
        with Cluster() as cluster_b:
            a = Node("A")
            b = Node("B")
            c = Node("C")

    with Cluster() as cluster_c:
        with Cluster() as cluster_d:
            d = Node("D")
            e = Node("E")

    Flow([c, e], ltail=cluster_a.name)