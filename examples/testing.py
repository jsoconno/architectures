from architectures.core import Graph, Cluster, Group, Node, Anchor, Edge, Flow

# Import the LightMode theme
from architectures.themes import Default, LightMode

theme = LightMode(graph_attr_overrides={"rankdir": "TB"})

with Graph("My Graph", theme=theme):
    with Cluster() as cluster_a:
        snooze = Node("Snooze")
        code = Node("Code")
        coffee = Node("Coffee")

        anchor = Anchor()
        
    
    Flow([coffee, code, snooze], constraint="False")
    Edge(snooze, coffee, style="dotted", constraint="False")