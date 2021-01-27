from architectures.core import Graph, Cluster, Group, Node, Edge, Flow
from architectures.themes import Default, LightMode

with Graph(theme=LightMode()):
    node_a = Node("A")
    node_b = Node("B")
    with Cluster() as cluster_a:
        node_c = Node("C")
        node_d = Node("D")
    with Cluster() as cluster_b:
        node_e = Node("E")

    Edge(node_e, node_d)
    Edge(node_a, [node_b, node_c])
    Edge(cluster_a, cluster_b)
