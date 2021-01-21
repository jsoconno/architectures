"""
This module contains all core classes required for drawing diagrams.  

Available Classes:
- Graph
- Cluster
- Group
- Node
- Edge
- Flow

Available Functions:
- get_graph
- set_graph
- get_cluster
- set_cluster
- get_node
- set_node
- wrap_text
- get_node_from_cluster
- get_cluster_from_node

Details for each can be found in the docstrings for the respective class or function.
"""

import contextvars
import os
import uuid
from pathlib import Path

from graphviz import Digraph

from architectures.themes import Default

__graph = contextvars.ContextVar("graph")
__cluster = contextvars.ContextVar("cluster")
__node = contextvars.ContextVar("node")

def get_graph():
    """
    Get the current graph context
    """
    try:
        return __graph.get()
    except LookupError:
        return None

def set_graph(graph):
    """
    Set the current graph context
    """
    __graph.set(graph)

def get_cluster():
    """
    Get the current cluster context
    """
    try:
        return __cluster.get()
    except LookupError:
        return None

def set_cluster(cluster):
    """
    Set the current cluster context
    """
    __cluster.set(cluster)

def get_node():
    """
    Get the current node to cluster mapping
    """
    try:
        return __node.get()
    except LookupError:
        return None

def set_node(node):
    """
    Set a node to cluster mapping
    """
    __node.set(node)


def wrap_text(text, max_length=16):
    """Return a new label with wrapped text

    Parameters
    ----------
    text : str
        The current label text
    max_length : int
        The max length for the label (defaults to 16 characters)

    Returns
    -------
    str
        The new label text
    """
    if max_length < 12:
        max_length = 12
        
    if len(text) > max_length:
        words = text.split()
        new_text = ""
        if len(words) > 1:
            temp_text = ""
            for word in words:
                test_text = temp_text + " " + word
                if len(test_text) < max_length:
                    new_text = new_text + " " + word
                    temp_text = test_text
                else:
                    new_text = new_text + "\n" + word
                    temp_text = word
        return new_text
    else:
        return text

def get_node_from_cluster(cluster):
    """Return the most central Node in a Cluster

    Parameters
    ----------
    cluster : Cluster
        A Cluster object

    Returns
    -------
    Node
        The most centrally located Node object
    """
    node_dict = get_node()
    center_node_index = round(len(node_dict[cluster])/2) - 1
    node = node_dict[cluster][center_node_index]
    return node

def get_cluster_from_node(node):
    """Return a Node's parent Cluster

    Parameters
    ----------
    node : Node
        A Node object

    Returns
    -------
    Cluster
        The parent Cluster
    """
    node_dict = get_node()
    for cluster, nodes in node_dict.items():
        for item in nodes:
            if item == node:
                return cluster

class Graph():
    """
    Create and set default settings for a graph and its clusters, nodes, and edges.
    """
    def __init__(self, name="my-architecture", output_file_format="png", theme=None, show=True):
        """
        :param str name: The name of the graph.
        :param str output_file_format: The format of the output file.
        :param theme: The base theme to apply to the graph and its clusters, nodes, and edges.
        :param bool show: Flag used to determine whether or not the graph will render.
        """

        # Set graph and output file name
        self.name = name
        self.output_file_name = "-".join(self.name.split()).lower()
        self.output_file_format = output_file_format

        # Create the graph
        self.dot = Digraph(name=self.name, filename=self.output_file_name, engine="dot")

        # Set the theme
        if theme is None:
            self.theme = Default()
        else:
            self.theme = theme

        # Set global graph attributes
        self.dot.graph_attr.update(self.theme.graph_attrs)
        self.dot.graph_attr["label"] = self.name

        # Set global node attributes
        self.dot.node_attr.update(self.theme.node_attrs)

        # Set global edge attributes
        self.dot.edge_attr.update(self.theme.edge_attrs)

        # Set option to show architecture diagram
        self.show = show

    def __str__(self):
        return str(self.dot)

    def __enter__(self):
        set_graph(self)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.render()
        # Remove the graphviz file leaving only the image.
        os.remove(self.output_file_name)
        set_graph(None)

    def node(self, node_id, label, **attrs):
        """
        Create a node.
        """
        self.dot.node(node_id, label=label, **attrs)

    def edge(self, start_node, end_node, **attrs):
        """
        Connect individual or lists of nodes with edges.
        """
        self.dot.edge(start_node.node_id, end_node.node_id, **attrs)

    def subgraph(self, dot):
        """
        Create a subgraph for grouping nodes.
        """
        self.dot.subgraph(dot)

    def render(self):
        """
        Generate output file.
        """
        self.dot.render(format=self.output_file_format, view=self.show, quiet=True)

class Cluster():
    """
    Create a cluster.
    """

    _default_label = None

    def __init__(self, label="", **attrs):
        """
        :param label: Label for the cluster.
        """

        # Set the cluster name
        self.name = "cluster_" + self._rand_id()

        #Set the cluster label
        if label == "" and self._default_label:
            self.label = self._default_label
        else:
            self.label = label

        # Create cluster
        self.dot = Digraph(self.name)

        # Set global graph and cluster context
        self._graph = get_graph()
        if self._graph is None:
            raise EnvironmentError("The object is not part of a Graph")
        self._cluster = get_cluster()

        # Set cluster attributes based on the theme using copy to ensure the objects are independent
        self.dot.graph_attr.update(self._graph.theme.cluster_attrs)

        # Set cluster depth to allow for logic based on the nesting of clusters
        self._depth = self._cluster._depth + 1 if self._cluster else 0

        # Get background colors from theme
        _colors = self._graph.theme.colors

        # Set the cluster background color
        if _colors:
            color_index = self._depth % len(_colors)
            self.dot.graph_attr["bgcolor"] = _colors[color_index]

        # Update cluster label
        self.dot.graph_attr["label"] = self.label

        # Override any values directly passed from the object
        self.dot.graph_attr.update(attrs)


    def __enter__(self):
        set_cluster(self)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self._cluster:
            self._cluster.subgraph(self.dot)
        else:
            self._graph.subgraph(self.dot)
        set_cluster(self._cluster)

    def node(self, node_id, label, **attrs):
        """
        Create a node in the cluster.
        """
        self.dot.node(node_id, label=label, **attrs)

    def subgraph(self, dot=Digraph):
        """
        Create a subgraph of the cluster.
        """
        self.dot.subgraph(dot)

    @staticmethod
    def _rand_id():
        return uuid.uuid4().hex


class Group(Cluster):
    """
    Creates a special type of cluster used only or grouping nodes.
    """

    def __init__(self, label="group", **attrs):

        # Set the group name
        self.name = "cluster_" + self._rand_id()

        # Set the group label
        self.label = label

        # Create group
        self.dot = Digraph(self.name)

        # Set global graph and group context
        self._graph = get_graph()
        if self._graph is None:
            raise EnvironmentError("The object is not part of a Graph")
        self._cluster = get_cluster()

        # Update group background color style
        self.dot.graph_attr["style"] = "invis"

        # Set group depth
        self._depth = self._cluster._depth + 1 if self._cluster else 0

class Node():
    """
    Creates a node.  This can be a standard node or a node representing a service from a provider.
    """

    _provider = None
    _service_type = None

    _icon_dir = None
    _icon = None

    _default_label = None

    def __init__(self, label="", wrap_label_text=True, **attrs):
        """
        :param str label: Label for a node.
        """
        # Generate an ID used to uniquely identify a node
        self._id = self._rand_id()

        #Set the label
        if self._icon and label == "":
            self.label = self._default_label
        else:
            self.label = label

        # Get global graph and cluster context to ensure the Node is part of the graph or cluster
        self._graph = get_graph()
        if self._graph is None:
            raise EnvironmentError("The object is not part of a Graph")
        self._cluster = get_cluster()

        # Set default icon
        if not isinstance(self._graph.theme, Default) and not self._icon:
            self._provider = "general"
            self._service_type = "blank"

            self._icon_dir = "icons/general/blank"
            self._icon = "default.png"

        # Auto-wrap labels
        if wrap_label_text:
            if self._cluster is not None:
                self.label = wrap_text(self.label, len(self._cluster.label))
            else:
                self.label = wrap_text(self.label)

        # Set node attributes based on the theme using copy to ensure the objects are independent
        self.node_attrs = self._graph.theme.node_attrs.copy()

        # Override any values directly passed from the object
        self.node_attrs.update(attrs)

        # Add attributes specific for when provider service nodes are used.
        if self._icon:
            padding = 0.1 * (self.label.count('\n'))
            self.node_attrs["height"] = str(float(self.node_attrs['height']) + padding)
            self.node_attrs["image"] = self._load_icon()

        # If a node is in the cluster context, add it to cluster.
        if self._cluster:
            self._cluster.node(self._id, self.label, **self.node_attrs)
        else:
            self._graph.node(self._id, self.label, **self.node_attrs)

        node_dict = get_node()
        if node_dict is None:
            # Creates the initial node dictionary if one does not exist
            node_dict = {self._cluster: [self]}
            set_node(node_dict)
        elif self._cluster not in node_dict:
            # Adds a new cluster key and value to the node dictionary
            node_dict.update({self._cluster: [self]})
        else:
            # Updates an existing cluster value in the node dictionary
            node_list = node_dict[self._cluster]
            node_list.append(self)
            node_dict.update({self._cluster: node_list})
            set_node(node_dict)

    @property
    def node_id(self):
        """
        Return the node id
        """
        return self._id

    @staticmethod
    def _rand_id():
        return uuid.uuid4().hex

    def _load_icon(self):
        basedir = Path(os.path.abspath(os.path.dirname(__file__)))
        return os.path.join(basedir.parent.parent, self._icon_dir, self._icon)

class Edge():
    """
    Creates an edge between two nodes
    """

    def __init__(self, start_node, end_node, **attrs):
        """
        :param start: The origin cluster, group, or node object.
        :param end: The destination cluster, group, or node object.
        :param attrs: Other edge attributes.
        """

        self.start_node = start_node
        self.end_node = end_node

        # Get global graph and cluster context to ensure the node is part of the graph or cluster
        self._graph = get_graph()
        if self._graph is None:
            raise EnvironmentError("The object is not part of a Graph")
        self._node = get_node()

        # Set edge attributes based on the theme using copy to ensure the objects are independent
        self.edge_attrs = self._graph.theme.edge_attrs.copy()

        if not isinstance(self.start_node, list):
            self.start_node = [self.start_node]
        
        if not isinstance(self.end_node, list):
            self.end_node = [self.end_node]

        # Ensure object passed is of the correct type
        for nodes in [self.start_node, self.end_node]:
            if not all(isinstance(node, (Cluster, Group, Node)) for node in nodes):
                raise TypeError("The Edge object only accepts Clusters, Groups, and Nodes.")

        start_node_list = self.start_node
        end_node_list = self.end_node

        # Handle all cases
        for current_start_node in start_node_list:
            for current_end_node in end_node_list:
                if isinstance(current_start_node, Node) and isinstance(current_end_node, Node):
                    self.start_node = current_start_node
                    self.end_node = current_end_node
                    self.edge_attrs.update({"ltail": "", "lhead": ""})
                elif isinstance(current_start_node, Node) and isinstance(current_end_node, (Cluster, Group)):
                    start_cluster = get_cluster_from_node(current_start_node)
                    end_cluster = current_end_node
                    if start_cluster == end_cluster:
                        self.start_node = None
                        self.end_node = None
                    else:
                        self.start_node = current_start_node
                        self.end_node = get_node_from_cluster(current_end_node)
                        self.edge_attrs.update({"lhead": end_cluster.name})
                elif isinstance(current_start_node, (Cluster, Group)) and isinstance(current_end_node, Node):
                    start_cluster = current_start_node
                    end_cluster = get_cluster_from_node(current_end_node)
                    if start_cluster == end_cluster:
                        self.start_node = None
                        self.end_node = None
                    else:
                        self.start_node = get_node_from_cluster(current_start_node)
                        self.end_node = current_end_node
                        self.edge_attrs.update({"ltail": start_cluster.name})
                elif isinstance(current_start_node, (Cluster, Group)) and isinstance(current_end_node, (Cluster, Group)):
                    start_cluster = current_start_node
                    end_cluster = current_end_node
                    if start_cluster == end_cluster:
                        self.start_node = None
                        self.end_node = None
                    else:
                        self.start_node = get_node_from_cluster(current_start_node)
                        self.end_node = get_node_from_cluster(current_end_node)
                        self.edge_attrs.update({"ltail": start_cluster.name, "lhead": end_cluster.name})
                else:
                    assert isinstance(self.start_node, (Cluster, Group, Node))
                    assert isinstance(self.end_node, (Cluster, Group, Node))

                # Override any attributes directly passed from the object
                self.edge_attrs.update(attrs)

                if self.start_node is not None and self.end_node is not None:
                    self._graph.edge(self.start_node, self.end_node, **self.edge_attrs)

class Flow():
    """
    Another method of connecting nodes by allowing users to define a flow as a list
    """
    def __init__(self, nodes, **attrs):

        self.nodes = nodes
        self.node_count = len(self.nodes)

        # Get global graph and cluster context to ensure the node is part of the graph or cluster
        self._graph = get_graph()
        if self._graph is None:
            raise EnvironmentError("The object is not part of a Graph")

        # Set edge attributes based on the theme using copy to ensure the objects are independent
        self.edge_attrs = self._graph.theme.edge_attrs.copy()

        # Override any attributes directly passed from the object
        self.edge_attrs.update(attrs)

        # Make sure there is more than one node
        if self.node_count > 1:

            # For every node in the list
            for i in range(self.node_count):

                # Set the start and end node
                if i < self.node_count - 1:
                    self.start_node = self.nodes[i]
                    self.end_node = self.nodes[i + 1]

                    Edge(self.start_node, self.end_node, **self.edge_attrs)
        else:
            raise Exception('More than one node must be passed in the list to use the Flow object')

Connection = Edge
Container = Cluster
