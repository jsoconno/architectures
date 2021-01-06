from architectures.core import Graph, Cluster, Group, Node, Edge, Flow
from architectures.themes import Default, Clean

from architectures.providers.azure.compute import VirtualMachine
from architectures.providers.azure.networking import ApplicationGateway
from architectures.providers.azure.generic import Azure
from architectures.providers.azure.management import Subscription

theme = Clean(graph_attr_overrides={"splines": "ortho"})

with Graph("my architecture", theme=theme, show=True):
    with Cluster("Azure") as azure:
        azure = Azure("", width=".5", height=".5")
        with Cluster("Subscription") as subscription:
            subscription = Subscription("", width=".5", height=".5")
            with Cluster("Resource Group") as resource_group:
                pass
                with Cluster("Virtual Network") as virtual_network_1:
                    pass
                    with Cluster("Build Subnet") as build_subnet:
                        with Group():
                            vm1 = VirtualMachine("Build Machine")
                            vm2 = VirtualMachine("Build Machine")
                        vm3 = VirtualMachine("Build Machine")

                with Cluster("Virtual Network 2") as virtual_network_2:
                    pass
                    with Cluster("Admin Subnet") as admin_subnet:
                        app_gateway = ApplicationGateway("test")
