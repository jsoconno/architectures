from architectures.core import Graph, Cluster, Group, Node, Edge
from architectures.themes import Default, Clean
from architectures.providers.azure.compute import VirtualMachine
from architectures.providers.azure.deployment import AzureDevops
from architectures.providers.azure.networking import ApplicationGateway, LoadBalancer, PrivateEndpoint
from architectures.providers.azure.security import Firewall
from architectures.providers.azure.data import SqlDatabase, SqlDataWarehouse, DataLake, AzureCosmosDb, DataFactory, AzureDatabricks
from architectures.providers.azure.security import KeyVault
from architectures.providers.azure.ai import PowerBi

theme = Clean()

with Graph("my architecture", theme=theme):
    with Cluster("Azure") as azure:
        with Cluster("Subscription") as subscription:
            with Cluster("Resource Group") as resource_group:
                with Cluster("Data Source") as data_source:
                    Sql_database = SqlDatabase("Sql Database")
                    Sql_data_warehouse = SqlDataWarehouse("Sql Data Warehouse")
                    cosmos_db = AzureCosmosDb("Cosmos DB")
                with Cluster("Virtual Network") as virtual_network:
                    data_lake = DataLake("Data Lake")
                    with Cluster("Private Endpoint Subnet") as private_endpoint_subnet:
                        private_endpoints = [
                            PrivateEndpoint("Sql Database"),
                            PrivateEndpoint("Sql Data Warehouse"),
                            PrivateEndpoint("Cosmos DB"),
                        ]
                    with Cluster("Data Factory Machine Subnet") as data_factory_machine_subnet:
                        data_factory = DataFactory("Azure Data Factory")
                        data_factory_vm = VirtualMachine("Integration Runtime")

                    with Cluster("Workstation Subnet") as workstation_subnet:
                        for i in range(3):
                            with Group():
                                VirtualMachine("")
                                PowerBi(f"WS{i + 1}")

                    with Cluster("AzureDatabricks Private Subnet") as AzureDatabricks_private_subnet:
                        private_AzureDatabricks = AzureDatabricks("Azure AzureDatabricks")

                    with Cluster("AzureDatabricks Public Subnet") as AzureDatabricks_public_subnet:
                        public_AzureDatabricks = AzureDatabricks("Azure AzureDatabricks")

    Edge(Sql_data_warehouse, private_endpoints[1])