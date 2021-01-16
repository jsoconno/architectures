from architectures.core import Graph, Cluster, Group, Node, Edge
from architectures.themes import Default, LightMode
from architectures.providers.azure.compute import VirtualMachine
from architectures.providers.azure.deployment import AzureDevops
from architectures.providers.azure.networking import ApplicationGateway, LoadBalancer, PrivateEndpoint
from architectures.providers.azure.security import Firewall
from architectures.providers.azure.data import SqlDatabase, SqlDataWarehouse, DataLake, AzureCosmosDb, DataFactory, AzureDatabricks
from architectures.providers.azure.security import KeyVault
from architectures.providers.azure.ai import PowerBi

theme = LightMode()

with Graph("my architecture", theme=theme, show=True):
    with Cluster("Azure") as azure:
        with Cluster("Subscription") as subscription:
            with Cluster("Resource Group") as resource_group:
                with Cluster("Data Source") as data_source:
                    sql_database = SqlDatabase("Sql Database")
                    sql_data_warehouse = SqlDataWarehouse("Sql Data Warehouse")
                    cosmos_db = AzureCosmosDb("Cosmos DB")
                with Cluster("Virtual Network") as virtual_network:
                    data_lake = DataLake("Data Lake")
                    with Cluster("Private Endpoint Subnet") as private_endpoint_subnet:
                        private_endpoints = [
                            PrivateEndpoint("Sql Database"),
                            PrivateEndpoint("Sql Data Warehouse"),
                            PrivateEndpoint("Cosmos DB"),
                        ]
                    with Cluster("Data Factory Machine Subnet") as data_factory_subnet:
                        data_factory = DataFactory("Azure Data Factory")
                        data_factory_vm = VirtualMachine("Integration Runtime")

                    with Cluster("Workstation Subnet") as workstation_subnet:
                        with Group() as vm_group:
                            vms = [
                                VirtualMachine(""),
                                VirtualMachine(""),
                                VirtualMachine("")
                            ]

                    with Cluster("AzureDatabricks Private Subnet") as azure_databricks_private_subnet:
                        private_azure_databricks = AzureDatabricks("Azure AzureDatabricks")

                    with Cluster("AzureDatabricks Public Subnet") as azure_databricks_public_subnet:
                        public_azure_databricks = AzureDatabricks("Azure AzureDatabricks")
                        node = Node("Test")

    # # node to node
    # Edge(sql_database, data_lake)

    # # node to list of nodes
    # Edge(cosmos_db, private_endpoints)

    # # list of nodes to node
    # Edge(private_endpoints, cosmos_db)

    # # list of nodes to cluster
    # Edge(vms, data_factory_subnet)

    # # cluster to list of nodes
    # Edge(data_factory_subnet, private_endpoints)

    # # list of nodes to list of nodes
    # Edge(vms, private_endpoints)

    # # cluster to cluster
    # Edge(azure_databricks_private_subnet, azure_databricks_public_subnet)
    
    # # cluster to group
    # Edge(vms, azure_databricks_public_subnet)