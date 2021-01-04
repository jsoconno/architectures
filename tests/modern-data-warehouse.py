from architectures.core import Graph, Cluster, Group, Node, Edge
from architectures.themes import Default, Clean

theme = Clean()

with Graph("my architecture", theme=theme, show=True):
    unstructured_data = Node("Logs Files and Media (Unstructured)")
    structured_data = Node("Business and Custom Apps (Structured)")