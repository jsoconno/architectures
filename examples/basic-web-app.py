from architectures.core import Graph, Cluster, Group, Node, Edge, Flow
from architectures.themes import LightMode, DarkMode

from architectures.providers.azure.general import Internet
from architectures.providers.azure.identity import AzureActiveDirectoryDomainServices
from architectures.providers.azure.networking import DnsZonePublic
from architectures.providers.azure.application import ApplicationService, ApplicationServiceEnvironment
from architectures.providers.azure.storage import StorageAccountBlobHot
from architectures.providers.azure.data import SqlDatabase, SqlServer
from architectures.providers.azure.compute import VirtualMachineWindows

theme = LightMode(graph_attr_overrides={"rankdir":"BT", "fontsize":"24"}, hue="blue")

with Graph('Web App Over SQL', theme=theme):
    with Group() as group:
        azure_ad = AzureActiveDirectoryDomainServices()
        internet = Internet()
        dns = DnsZonePublic()
    with Cluster(style="dotted") as resource_group:
        blob_storage = StorageAccountBlobHot()
        with Cluster("App Service Plan") as app_service_plan:
            app_service = ApplicationService("Test")
            app_service_environment = ApplicationServiceEnvironment()

        with Cluster("Azure SQL Database") as data_subnet:
            sql_server = SqlServer()
            sql_database = SqlDatabase()

            with Cluster("Another Cluster"):
                with Cluster("Another Cluster"):
                    with Cluster("Another Cluster"):
                        vm = VirtualMachineWindows("This is a really long name for a VM", color="grey")

    Edge(internet, [azure_ad, dns], style="dotted")
    Edge(internet, app_service)
    Edge(sql_server, sql_database)