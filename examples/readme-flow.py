# you can create a graph with nodes
# you can connect those nodes with edges
# you can also use the flow object to connect multiple nodes
# you can group nodes in containers with a border
# you can also use groups to organize nodes without a border
# you can use themes to change the look and feel of a diagram
# you can use pre-defined provider services on your

from architectures.core import Graph, Cluster, Group, Node

with Graph("My Graph"):
    with Cluster("A"):
        Node("A")
        Node("B")
        Node("C")

    with Group("A"):
        Node("D")
        Node("E")

    Node("F")