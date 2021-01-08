from architectures.core import Graph, Cluster, Group, Node, Edge, Flow
from architectures.themes import Default

theme = Default(graph_attr_overrides={"splines": "ortho"})

with Graph("my architecture", theme=theme, show=True):
    with Cluster("Container A") as container_a:
        a = Node("END")
        b = Node("START")
        c = Node("C")

    with Cluster("Container B") as container_b:
        d = Node("D")
        e = Node("E")

    with Cluster("Container C") as container_c:
        f = Node("F")

        with Cluster("Container D") as container_d:
            g = Node("G")

    Flow([b, c, d, container_c, e, container_d, a])