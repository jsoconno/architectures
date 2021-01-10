from architectures.core import Graph, Cluster, Group, Node, Edge, Flow
from architectures.themes import LightMode, DarkMode

from architectures.providers.azure.general import Internet
from architectures.providers.azure.identity import AzureActiveDirectoryDomainServices
from architectures.providers.azure.networking import DnsZonePublic
from architectures.providers.azure.application import ApplicationService, ApplicationServiceEnvironment
from architectures.providers.azure.storage import StorageAccountBlobCool
from architectures.providers.azure.data import SqlDatabase, SqlServer
from architectures.providers.azure.compute import VirtualMachine

theme = DarkMode(graph_attr_overrides={"rankdir":"BT", "fontsize":"24"})

with Graph('Web App Over SQL', theme=theme):
    with Group() as group:
        azure_ad = AzureActiveDirectoryDomainServices("Azure Active Directory")
        internet = Internet("Internet")
        dns = DnsZonePublic("Azure DNS")
    with Cluster("Resource Group", style="dotted") as resource_group:
        blob_storage = StorageAccountBlobCool("Storage Blob")
        with Cluster("App Service Plan") as app_service_plan:
            app_service = ApplicationService("App Service")
            app_service_environment = ApplicationServiceEnvironment("App Service Environment")

        with Cluster("Azure SQL Database"):
            sql_server = SqlServer("Logical Server")
            sql_database = SqlDatabase("Database")

            with Cluster("Another Cluster"):
                with Cluster("Another Cluster"):
                    with Cluster("Another Cluster"):
                        vm = VirtualMachine()

    Edge(internet, [azure_ad, dns], style="dotted")
    Edge(internet, app_service)
    Edge(sql_server, sql_database)