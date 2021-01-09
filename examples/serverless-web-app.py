from architectures.core import Graph, Cluster, Group, Node, Edge, Flow
from architectures.themes import Clean

from architectures.providers.azure.general import Internet
from architectures.providers.azure.identity import AzureActiveDirectoryDomainServices
from architectures.providers.azure.management import ApiManagementService, AzureMonitor
from architectures.providers.azure.application import FunctionApp
from architectures.providers.azure.data import AzureCosmosDb
from architectures.providers.azure.networking import CdnProfile
from architectures.providers.azure.storage import StorageAccountBlobCool
from architectures.providers.azure.deployment import AzurePipelines

theme = Clean(
    edge_attr_overrides={"minlen": "1.5"},
    graph_attr_overrides={"nodesep": "1"}
)

with Graph('Serverless Web App', theme=theme):

    with Cluster("Resource Group") as resource_group:
        with Cluster("Static Content") as static_content:
            cdn = CdnProfile("CDN")
            storage = StorageAccountBlobCool("Blob Storage")

        with Cluster("API") as api:
            api_management = ApiManagementService("API Management")
            function_app = FunctionApp("Function App")
            cosmos_db = AzureCosmosDb("Cosmos DB")

    with Group() as other_services:
        azure_pipelines = AzurePipelines("Azure Pipelines")
        monitor = AzureMonitor("Monitor")

    with Group():
        user = Node("")
        azure_ad = AzureActiveDirectoryDomainServices("Azure Active Directory")
        internet = Internet("Single-Page Web Application")

    Edge(user, azure_ad, style="dotted", label="Sign In")
    Edge([api_management, function_app], azure_ad, style="dotted", xlabel="Auth")
    Edge(internet, cdn, xlabel="Http GET")
    Edge(internet, api_management, xlabel="Http GET AJAX Request")
    Flow([api_management, function_app, cosmos_db])
    Edge(storage, cdn)
    Edge(cosmos_db, azure_pipelines, style="invis")

