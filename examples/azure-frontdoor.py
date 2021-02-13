# Import the base objects
from architectures.core import Graph, Cluster, Node, Edge, Flow

# Import the available themes
from architectures.themes import Default, LightMode, DarkMode
from architectures.themes.settings import GraphSettings, ClusterSettings, NodeSettings, EdgeSettings

# Import services
from architectures.providers.azure.networking import ApplicationGateway, AzureFrontDoor, LoadBalancer, TrafficManagerProfile
from architectures.providers.azure.compute import VirtualMachineWindows
from architectures.providers.azure.application import ApplicationService
from architectures.providers.azure.data import SqlDatabase
from architectures.providers.azure.storage import StorageAccountBlob

theme = LightMode()

with Graph("Azure Frontdoor", theme=theme):
    traffic_manager = TrafficManagerProfile()
    front_door = AzureFrontDoor()

    with Cluster("Region 1") as region_1:
        app_gateway_1 = ApplicationGateway()
        with Cluster("Image Server Pool") as image_pool_1:
            VirtualMachineWindows()
            VirtualMachineWindows()
        with Cluster("Default Server Pool") as default_pool_1:
            VirtualMachineWindows()
            VirtualMachineWindows()
        load_balancer_1 = LoadBalancer()
        with Cluster("Data Tier", hide_border=True) as data_tier_1:
            vms_1 = [
                VirtualMachineWindows(),
                VirtualMachineWindows(),
                VirtualMachineWindows(),
            ]
        app_service_1 = ApplicationService()
        sql_database_1 = SqlDatabase()
        blob_storage_1 = StorageAccountBlob()

    with Cluster("Region 2") as region_2:
        app_gateway_2 = ApplicationGateway()
        with Cluster("Image Server Pool") as image_pool_2:
            VirtualMachineWindows()
            VirtualMachineWindows()
        with Cluster("Default Server Pool") as default_pool_2:
            VirtualMachineWindows()
            VirtualMachineWindows()
        load_balancer_2 = LoadBalancer()
        with Cluster("Data Tier", hide_border=True) as data_tier_2:
            vms_2 = [
                VirtualMachineWindows(),
                VirtualMachineWindows(),
                VirtualMachineWindows(),
            ]
        app_service_2 = ApplicationService()
        sql_database_2 = SqlDatabase()
        blob_storage_2 = StorageAccountBlob()

    # Global flows
    Edge(front_door, [app_gateway_1, app_gateway_2], color="purple")
    Edge(front_door, [app_service_1, app_service_2], color="green")
    Edge(traffic_manager, [blob_storage_1, blob_storage_2], color="blue")
    
    # Region 1 flows
    Edge(app_service_1, sql_database_1)
    Edge(app_gateway_1, [image_pool_1, default_pool_1])
    Flow([default_pool_1, load_balancer_1, vms_1])

    # Region 2 flows
    Edge(app_service_2, sql_database_2)
    Edge(app_gateway_2, [image_pool_2, default_pool_2])
    Flow([default_pool_2, load_balancer_2, vms_2])
