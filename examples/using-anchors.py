# Import the base objects
from architectures.core import Graph, Cluster, Node, Edge, Flow

# Import the available themes
from architectures.themes import LightMode, DarkMode

# Import provider services
from architectures.providers.azure.networking import ApplicationGateway, LoadBalancer
from architectures.providers.azure.compute import VirtualMachineWindows
from architectures.providers.azure.data import DataLake

# Set the theme
theme = LightMode()

with Graph("Basic Architecture", theme=theme):
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")

    to_x_to = Node(hide_node=True)
    to_y_to = Node(hide_node=True)
    to_z_to = Node(hide_node=True)

    # Flow([a, to_x_to, [b, c]])

    Edge(a, to_x_to)
    Edge(to_x_to, [to_y_to, to_z_to])
    Edge(to_y_to, [b, c])
    Edge(to_z_to, [d, e])