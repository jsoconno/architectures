from architectures.core import Graph, Cluster, Group, Node, Edge, Flow
from architectures.themes import DarkMode, LightMode

from architectures.providers.azure.hierarchies import Subscription, ResourceGroup

from architectures.providers.azure.general import Computer
from architectures.providers.azure.application import ApplicationService
from architectures.providers.azure.ai import BotService, CognitiveServicesSearch, CognitiveServices
from architectures.providers.azure.data import SqlDatabase
from architectures.providers.azure.compute import VirtualMachine

theme = LightMode(graph_attr_overrides={"nodesep":"3"})

with Graph("Intelligent Search", theme=theme):
    computer = Computer()
    with Subscription():
        with ResourceGroup():
            with Cluster() as app_service_cluster:
                app_service = ApplicationService()
            with Cluster() as bot_service_cluster:
                bot_service = BotService()
            with Cluster() as cognitive_search_cluster:
                cognitive_search = CognitiveServicesSearch()
            with Cluster() as cognitive_services_cluster:
                cognitive_services = CognitiveServices()
            with Cluster() as database_cluster:
                database = SqlDatabase()

    Flow([computer, app_service_cluster, cognitive_search_cluster])
    Flow([computer, bot_service_cluster, cognitive_search_cluster])
    Edge(cognitive_search_cluster, database_cluster, dir="both")
    Edge(cognitive_search_cluster, cognitive_services_cluster, dir="both")
    Edge(app_service_cluster, database_cluster, dir="both")