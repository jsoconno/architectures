from architectures.core import Graph, Cluster, Group, Node, Edge, Flow
from architectures.themes import Default, LightMode

theme = Default(graph_attr_overrides={"splines": "ortho"})

with Graph("my architecture", theme=theme, show=True):
    with Cluster("Cluster A") as cluster_a:
        a = Node("A")
        b = Node("B")
        c = Node("C")

    with Cluster("Cluster B") as cluster_b:
        d = Node("D")
        e = Node("E")

        with Cluster("Cluster C") as cluster_c:
            f = Node("F")
            g = Node("G")

            with Cluster("Cluster D") as cluster_d:
                h = Node("H")

    # With Edges you can connect...

    # Nodes to nodes
    Edge(a, b)

    # Nodes to clusters
    Edge(c, cluster_b)

    # Clusters to clusters
    Edge(cluster_d, cluster_a, style="dotted")

    # Lists of nodes or clusters to lists of nodes or clusters
    Edge([d, f], [e, cluster_c])

    # With Flows you can connect...

    # Any list of nodes or clusters with support for nested lists
    Flow([a, h, [b, g], c, f, d, e], color="red")

    # All objects support keyword arguments to change the style