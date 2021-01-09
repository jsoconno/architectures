from architectures.core import Graph, Cluster, Group, Node, Edge, Flow, Container, Connection
from architectures.themes import Default, Clean

from architectures.providers.azure.hierarchies import Subscription, ResourceGroup
from architectures.providers.azure.compute import VirtualMachine
from architectures.providers.azure.networking import ApplicationGateway
from architectures.providers.azure.ai import PowerBi

theme = Clean()

with Graph(theme=theme):
    with Subscription(color="#121212") as subscription:
        with ResourceGroup() as resource_group:
            app_gateway = ApplicationGateway()
            with Group():
                vms = [VirtualMachine() for i in range(3)]
            power_bi = PowerBi()

    Edge(app_gateway, vms)
    Edge(vms, power_bi)