from architectures.core import Graph, Cluster, Group, Node, Edge, Flow
from architectures.themes import Default, Clean

from architectures.providers.azure.data import DataFactory, DataLake, AzureDatabricks, AnalysisService, AzureSynapseAnalytics
from architectures.providers.azure.ai import PowerBi

theme = Clean(graph_attr_overrides={"rankdir": "LR", "nodesep":"3"}, edge_attr_overrides={"minlen": "2"})

with Graph("my architecture", theme=theme, show=True):

    unstructured_data = Node("Logs Files and Media (Unstructured)")
    structured_data = Node("Business and Custom Apps (Structured)")

    with Group():
        with Cluster("Ingest") as ingest:
            data_factory = DataFactory("Azure Data Factory")

        with Cluster("Store") as store:
            data_lake = DataLake("Data Lake")

    with Cluster("Prep and train") as train:
        databricks = AzureDatabricks("Azure Databricks")

    with Cluster("Model") as model:
        analysis_services = AnalysisService("Azure Analysis Services")
        synapse_analytics = AzureSynapseAnalytics("Azure Synapse Analytics")

    with Cluster("Serve") as serve:
        power_bi = PowerBi("Power BI")

    Edge([unstructured_data, structured_data], data_factory)
    Flow([data_factory, data_lake, databricks, power_bi])
    Flow([data_lake, synapse_analytics, analysis_services, power_bi])
    Edge(databricks, synapse_analytics, dir="both")