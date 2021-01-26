from architectures.core import Graph, Cluster, Group, Node, Edge, Flow
from architectures.themes import Default, LightMode

with Graph("My Graph Broken", theme=LightMode(), show=True) as graph:
    with Cluster("A") as cluster_a:
        a = Node("A")
        b = Node("B")

    with Cluster("B") as cluster_b:
        with Cluster("C") as cluster_c:
            with Cluster("D") as cluster_d:
                c = Node("C")
                d = Node("D")

    Edge(cluster_a, cluster_b)