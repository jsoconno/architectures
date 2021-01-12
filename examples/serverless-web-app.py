from architectures.core import Graph, Cluster, Group, Node, Edge, Flow
from architectures.themes import LightMode

from architectures.providers.azure.hierarchies import ResourceGroup

from architectures.providers.azure.general import Internet, Computer
from architectures.providers.azure.identity import AzureActiveDirectoryDomainServices
from architectures.providers.azure.management import ApiManagementService, AzureMonitor, Subscription
from architectures.providers.azure.application import FunctionApp
from architectures.providers.azure.data import AzureCosmosDb
from architectures.providers.azure.networking import CdnProfile
from architectures.providers.azure.storage import StorageAccountBlobCool
from architectures.providers.azure.deployment import AzurePipelines

theme = LightMode()

with Graph('Serverless Web App', theme=theme):

    with Cluster("Subscription") as subscription:
        Subscription(
            fontsize="6", 
            loc="t",
            fixedsize="true", 
            width="0.5", 
            height="0.8", 
            pin="true", 
            pos="0,2")
        with ResourceGroup() as resource_group:
            with Cluster("Static Content") as static_content:
                cdn = CdnProfile("CDN")
                storage = StorageAccountBlobCool("Blob Storage")

            with Cluster("API", bgcolor="red") as api:
                api_management = ApiManagementService()
                function_app = FunctionApp()
                cosmos_db = AzureCosmosDb()

    with Group():
        azure_pipelines = AzurePipelines()
        monitor = AzureMonitor()

    with Group():
        user = Computer()
        azure_ad = AzureActiveDirectoryDomainServices("AAD")
        internet = Internet()

    Edge(user, azure_ad, style="dotted", xlabel="Sign In")
    Edge([api_management, function_app], azure_ad, style="dotted", xlabel="Auth")
    Edge(internet, cdn, xlabel="Http GET")
    Edge(internet, api_management, xlabel="Http GET AJAX Request")
    Flow([api_management, function_app, cosmos_db])
    Edge(storage, cdn)
    Edge(cosmos_db, azure_pipelines, style="invis")

