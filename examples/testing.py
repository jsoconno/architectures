# Import the base objects
from architectures.core import Graph, Cluster, Group, Node, Edge, Flow

# Import the available themes
from architectures.themes import LightMode, DarkMode

# Import provider services
from architectures.providers.azure.networking import ApplicationGateway, LoadBalancer
from architectures.providers.azure.compute import VirtualMachineWindows
from architectures.providers.azure.data import DataLake

# Set the theme
theme = LightMode()

with Graph("Basic Architecture", theme=theme):
    Flow([Node("A"), Node("B"), [Node("C"), Node("D"), Node("E")]])