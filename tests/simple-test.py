from architectures.core import Graph, Cluster, Group, Node, Edge, Flow, Container, Connection
from architectures.themes import Default, Clean

from architectures.providers.azure.compute import VirtualMachine
from architectures.providers.azure.networking import ApplicationGateway
from architectures.providers.azure.generic import Azure
from architectures.providers.azure.management import Subscription

theme = Default(graph_attr_overrides={"splines": "ortho"})

with Graph("my architecture", theme=theme, show=True):
    with Cluster("Container A") as container_a:
        a = Node("A")
        b = Node("B")

    with Cluster("Container A") as container_b:
        c = Node("C")
        d = Node("D")