from architectures.core import Graph, Cluster, Group, Node, Edge, Flow
from architectures.themes import DarkMode, LightMode

from architectures.providers.azure.hierarchies import Subscription, ResourceGroup

from architectures.providers.azure.data import DataLake, SqlServer
from architectures.providers.azure.compute import VirtualMachine
from architectures.providers.azure.networking import ApplicationGateway

theme = LightMode()

with Graph("Simple", theme=theme):
    app_gateway = ApplicationGateway()
    with Cluster() as cluster_a:
        vms_a = [
            VirtualMachine(),
            VirtualMachine(),
            VirtualMachine()
        ]
    
    database = DataLake()

    Flow([app_gateway, vms_a, database])