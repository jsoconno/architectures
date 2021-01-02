from architectures.core import Graph, Cluster, Group, Node, Edge
from architectures.themes import Default, Clean
from architectures.providers.azure.compute import VirtualMachine
from architectures.providers.azure.devops import Devops
from architectures.providers.azure.network import ApplicationGateway, Firewall, LoadBalancers, PrivateEndpoint
from architectures.providers.azure.database import SQLDatabases, SQLDatawarehouse, DataLake, CosmosDb
from architectures.providers.azure.security import KeyVaults
from architectures.providers.azure.integration import DataFactory
from architectures.providers.azure.general import PowerBI, Databricks

theme = Clean()

with Graph("my architecture", theme=theme):
    with Cluster("Azure") as azure:
        with Cluster("Subscription") as subscription:
            with Cluster("Resource Group") as resource_group:
                with Cluster("Data Source") as data_source:
                    sql_database = SQLDatabases("SQL Database")
                    sql_data_warehouse = SQLDatawarehouse("SQL Data Warehouse")
                    cosmos_db = CosmosDb("Cosmos DB")
                with Cluster("Virtual Network") as virtual_network:
                    data_lake = DataLake("Data Lake")
                    with Cluster("Private Endpoint Subnet") as private_endpoint_subnet:
                        private_endpoints = [
                            PrivateEndpoint("SQL Database"),
                            PrivateEndpoint("SQL Data Warehouse"),
                            PrivateEndpoint("Cosmos DB"),
                        ]
                    with Cluster("Data Factory Machine Subnet") as data_factory_machine_subnet:
                        data_factory = DataFactory("Azure Data Factory")
                        data_factory_vm = VirtualMachine("Integration Runtime")

                    with Cluster("Workstation Subnet") as workstation_subnet:
                        for i in range(3):
                            with Group():
                                VirtualMachine("")
                                PowerBI(f"WS{i + 1}")

                    with Cluster("Databricks Private Subnet") as databricks_private_subnet:
                        private_databricks = Databricks("Azure Databricks")

                    with Cluster("Databricks Public Subnet") as databricks_public_subnet:
                        public_databricks = Databricks("Azure Databricks")

    Edge(sql_data_warehouse, private_endpoints[1])