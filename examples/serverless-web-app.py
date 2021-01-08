from architectures.core import Graph, Cluster, Group, Node, Edge, Flow
from architectures.themes import Clean

from architectures.providers.azure.generic import User
from architectures.providers.azure.identity import AzureActiveDirectoryDomainServices
from architectures.providers.azure.networking import DnsZonePublic
from architectures.providers.azure.application import ApplicationService, ApplicationServiceEnvironment
from architectures.providers.azure.storage import StorageAccountBlobCool
from architectures.providers.azure.data import SqlDatabase, SqlServer

theme = Clean()

with Graph('Serverless Web App', theme=theme):
