from architectures.core import Graph, Cluster, Group, Node, Edge, Flow
from architectures.themes import Clean, DarkMode

from architectures.providers.azure.general import Internet
from architectures.providers.azure.identity import AdDomainServices
from architectures.providers.azure.network import DnsZones
from architectures.providers.azure.web import AppServices, AppServiceEnvironments
from architectures.providers.azure.storage import BlobStorage
from architectures.providers.azure.database import SqlDatabases, SqlServers
from architectures.providers.azure.compute import Vm

theme = DarkMode(graph_attr_overrides={"rankdir":"BT", "fontsize":"24"})

with Graph('Web App Over SQL', theme=theme):
    with Group() as group:
        azure_ad = AdDomainServices("Azure Active Directory")
        internet = Internet("Internet")
        dns = DnsZones("Azure DNS")
    with Cluster("Resource Group", style="dotted") as resource_group:
        blob_storage = BlobStorage("Storage Blob")
        with Cluster("App Service Plan") as app_service_plan:
            app_service = AppServices("App Service")
            app_service_environment = AppServiceEnvironments("App Service Environment")

        with Cluster("Azure SQL Database"):
            sql_server = SqlServers("Logical Server")
            sql_database = SqlDatabases("Database")

            with Cluster("Another Cluster"):
                with Cluster("Another Cluster"):
                    with Cluster("Another Cluster"):
                        vm = Vm()

    Edge(internet, [azure_ad, dns], style="dotted")
    Edge(internet, app_service)
    #Edge(app_service, sql_server, style="invis")
    Edge(sql_server, sql_database)