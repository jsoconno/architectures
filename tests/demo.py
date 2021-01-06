from architectures.core import Graph, Cluster, Group, Node, Edge, Flow
from architectures.themes import Default, Clean

from architectures.providers.azure.compute import VirtualMachine

theme = Clean(graph_attr_overrides={"rankdir": "LR", "nodesep":"2", "margin":"30"}, edge_attr_overrides={"minlen":"2"})

with Graph("my-architecture", theme=theme):
    with Cluster("Cluster A") as cluster_a:
        a = VirtualMachine("A")
        b = VirtualMachine("B")
        c = VirtualMachine("C")

    with Cluster("Cluster B") as cluster_b:
        d = VirtualMachine("D")
        e = VirtualMachine("E")
        f = VirtualMachine("F")

    with Cluster("Cluster C") as cluster_c:
        g = VirtualMachine("G")

    Flow([a, e, cluster_c, cluster_b, b, e, g, f])