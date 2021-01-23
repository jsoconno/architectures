from architectures.core import Graph, Cluster, Group, Node, Edge, Flow

# Import the LightMode theme
from architectures.themes import Default, LightMode

theme = LightMode(graph_attr_overrides={"rankdir": "TB"})

with Graph("My Graph", theme=theme) as graph:
    with Cluster() as cluster_a:
        with Group() as group_b:
            node_a = Node("A")
            node_b = Node("B")
            node_c = Node("C")

    with Cluster() as cluster_c:
        with Group() as group_d:
            node_d = Node("D")

    Flow([node_a, group_d, group_b, node_d])