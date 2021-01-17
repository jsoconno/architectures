# Import the base objects
from architectures.core import Graph, Cluster, Group, Node, Edge, Flow

# Import the available themes
from architectures.themes import LightMode, DarkMode

# Import provider services
from architectures.providers.azure.networking import ApplicationGateway, LoadBalancer
from architectures.providers.azure.compute import VirtualMachineWindows
from architectures.providers.azure.data import DataLake

# Set the theme and add overrides
theme = LightMode(
    graph_attr_overrides={"labeljust":"c", "nodesep":"0.5"}, 
    cluster_attr_overrides={"style":"dotted"},
    node_attr_overrides={"fontcolor":"dimgrey"}, 
    edge_attr_overrides={"color":"dimgrey"},
    color_overrides=["#EBF4FA" "#D7E9F5", "#C3DEEF", "#AFD3EA"]
)

with Graph("My Customized Theme", theme=theme):
    with Cluster("Subscription"):
        with Cluster("Resource Group"):
            with Cluster("Virtual Network"):
                with Cluster("App Gateway Subnet") as app_gateway_subnet:
                    app_gateway = ApplicationGateway()
                
                with Cluster("Build Subnet") as build_subnet:
                    load_balancer = LoadBalancer()
                    vm_1 = VirtualMachineWindows()
                    vm_2 = VirtualMachineWindows()
                
            data_lake = DataLake()

    Flow([app_gateway_subnet, load_balancer, [vm_1, vm_2]])
    Edge(build_subnet, data_lake)