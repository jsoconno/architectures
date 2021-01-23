from architectures.core import Graph, Cluster, Group, Node, Edge, Flow

# Import the LightMode theme
from architectures.themes import Default, LightMode

theme = LightMode(graph_attr_overrides={"rankdir": "TB"})

with Graph("My Graph", theme=theme):
    with Cluster() as cluster_a:
        with Cluster() as cluster_b:
            node_a = Node("A")
            node_b = Node("B")
            node_c = Node("C")

    with Cluster() as cluster_c:
        with Cluster() as cluster_d:
            node_d = Node("D")

    Edge(node_a, cluster_d, ltail=str(cluster_b))

    print(node_a)