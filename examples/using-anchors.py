from architectures.core import Graph, Cluster, Group, Node, Anchor, Edge, Flow
from architectures.themes import Default, LightMode

with Graph(theme=LightMode(), show=True) as graph:
    with Cluster(rank="same"):
        a = Node()
        x = Anchor()
        b = Node()

    y = Anchor()

    with Cluster(rank="same"):
        c = Node()
        d = Node()
        e = Node()

    Flow([a, x, b], dir="none")
    Edge(x, y,)
    Edge(y, [c, d, e])