from architectures.core import Graph, Cluster, Group, Node, Edge, Flow

# Import the LightMode theme
from architectures.themes import Default, LightMode

theme = LightMode()

with Graph("My Graph", theme=theme):
    with Cluster() as cluster_a:
        with Cluster() as cluster_b:
            Node()

    with Cluster() as cluster_c:
        with Cluster() as cluster_d:
            Node()

    Edge(cluster_a, cluster_c)



    from architectures.providers.azure.hierarchies import Subscription
    from architectures.providers.azure.general import Subscription

    Edge(node_a, node_b, ltail=cluster_a._id, lhead=cluster_b._id)