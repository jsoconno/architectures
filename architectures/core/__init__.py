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
    try:
        return __graph.get()
    except LookupError:
        return None


def set_graph(graph):
    __graph.set(graph)


def get_cluster():
    try:
        return __cluster.get()
    except LookupError:
        return None


def set_node(node):
    __node.set(node)

def get_node():
    try:
        return __node.get()
    except LookupError:
        return None


def set_cluster(cluster):
    __cluster.set(cluster)


def wrap_text(text, max_length=16):
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

def validate_node(connection):
    """
    Validates that the type of node passed is of the right type
    """
    validate_types = isinstance(connection, (Cluster, Group, Node, list))

    if type(connection) == list:
        validate_list_items = isinstance(connection, list) and all(isinstance(x, (Cluster, Group, Node)) for x in connection)
        return validate_types and validate_list_items
    else:
        return validate_types

class Graph():
    """
    Create and set default settings for a graph and its clusters, nodes, and edges.
    """
    def __init__(self, name, output_file_name="", output_file_format="png", theme=None, show=True):
        """
        :param str name: The name of the graph.
        :param str output_file_name: The name of the file that will be output.
        :param str output_file_format: The format of the output file.
        :param theme: The base theme to apply to the graph and its clusters, nodes, and edges.
        :param bool show: Flag used to determine whether or not the graph will render.
        """

        # Set graph and output file name
        self.name = name
        if not output_file_name:
            output_file_name = "-".join(self.name.split()).lower()
        self.output_file_name = output_file_name
        self.output_file_format = output_file_format

        # Create the graph
        # Support for multiple engines can be added later by adding in the engine argument passed from the class
        self.dot = Digraph(name=self.name, filename=self.output_file_name)

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

    def edge(self, tail_node, head_node, **attrs):
        """
        Connect individual or lists of nodes with edges.
        """
        # Handle conditions where both passed objects are lists
        if isinstance(tail_node, list) and isinstance(head_node, list):
            [self.dot.edge(tail.node_id, head.node_id, **attrs) for head in head_node for tail in tail_node]
        elif isinstance(tail_node, list):
            [self.dot.edge(tail.node_id, head_node.node_id, **attrs) for tail in tail_node]
        elif isinstance(head_node, list):
            [self.dot.edge(tail_node.node_id, head.node_id, **attrs) for head in head_node]
        else:
            self.dot.edge(tail_node.node_id, head_node.node_id, **attrs)

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
    __background_colors = ("#FFFFFF", "#FFFFFF")

    def __init__(self, label="cluster", background_colors=False, **attrs):
        """
        :param label: Label for the cluster.
        :param background_colors: Flag for adding background colors to clusters.
        """

        # Set the cluster label
        self.label = label

        # Set the cluster name
        self.name = "cluster_" + self.label

        # Create cluster
        self.dot = Digraph(self.name)

        # Set global graph and cluster context
        self._graph = get_graph()
        if self._graph is None:
            raise EnvironmentError("No global graph object found.  A cluster must be part of a graphs context.")
        self._cluster = get_cluster()

        # Set cluster attributes based on the theme using copy to ensure the objects are independent
        self.dot.graph_attr.update(self._graph.theme.cluster_attrs)

        # Override any values directly passed from the object
        self.dot.graph_attr.update(attrs)

        # Update cluster label
        self.dot.graph_attr["label"] = self.label

        # Set cluster depth to allow for logic based on the nesting of clusters
        self.depth = self._cluster.depth + 1 if self._cluster else 0
        color_index = self.depth % len(self.__background_colors)

        # Set the background colors
        # Update this functionality to be something that is passed from a theme
        if background_colors:
            self.dot.graph_attr["bgcolor"] = self.__background_colors[color_index]


    def __enter__(self):
        set_cluster(self)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self._cluster:
            self._cluster.subgraph(self.dot)
        else:
            self._graph.subgraph(self.dot)
        set_cluster(self._cluster)

    def node(self, node_id: str, label: str, **attrs) -> None:
        """
        Create a node in the cluster.
        """
        self.dot.node(node_id, label=label, **attrs)

    def subgraph(self, dot=Digraph):
        self.dot.subgraph(dot)

    @staticmethod
    def _rand_id():
        return uuid.uuid4().hex


class Group(Cluster):
    """
    Creates a special type of group used only or organizing nodes.
    """
    def __init__(self):

        # Set the cluster label
        self.label = self._rand_id()

        # Set the cluster name
        self.name = "cluster_" + self.label

        # Create cluster
        self.dot = Digraph(self.name)

        # Set global graph and cluster context
        self._graph = get_graph()
        if self._graph is None:
            raise EnvironmentError("No global graph object found.  A cluster must be part of a graphs context.")
        self._cluster = get_cluster()

        # Update cluster label
        self.dot.graph_attr["style"] = "invis"
    

class Node():
    """
    Creates a node.  This can be a standard node or a node representing a service from a provider.
    """

    _provider = None
    _service_type = None

    _icon_dir = None
    _icon = None

    def __init__(self, label="", **attrs):
        """
        :param str label: Label for a node.
        """
        # Generate an ID used to uniquely identify a node
        self._id = self._rand_id()

        # Set the label
        self.label = label

        # Get global graph and cluster context to ensure the node is part of the graph and/or cluster
        self._graph = get_graph()
        if self._graph is None:
            raise EnvironmentError("No global graph object found.  A cluster must be part of a graphs context.")
        self._cluster = get_cluster()

        # Auto-wrap labels
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
            padding = 0.4 * (self.label.count('\n'))
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
            node_list.append([self])
            node_dict.update({self._cluster: node_list})
            set_node(node_dict)

    @property
    def node_id(self):
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

    def __init__(self, start_node, end_node, **attrs,
    ):
        """
        :param start: The origin cluster, group, or node object.
        :param end: The destination cluster, group, or node object.
        :param attrs: Other edge attributes.
        """

        # Ensure that the object passed is the correct type
        if start_node is not None and validate_node(start_node) is False:
            raise TypeError(f"The Edge class only accepts arguments of type Cluster, Group, or Node")

        if end_node is not None and validate_node(end_node) is False:
            raise TypeError(f"The Edge class only accepts arguments of type Cluster, Group, or Node")

        self.start_node = start_node
        self.end_node = end_node

        # Get global graph and cluster context to ensure the node is part of the graph and/or cluster
        self._graph = get_graph()
        if self._graph is None:
            raise EnvironmentError("No global graph object found.  A cluster must be part of a graphs context.")

        # Set edge attributes based on the theme using copy to ensure the objects are independent
        self.edge_attrs = self._graph.theme.edge_attrs.copy()

        # Override any attributes directly passed from the object
        self.edge_attrs.update(attrs)

        # Set the start_node to the first object if a list of nodes are passed
        if isinstance(start_node, list):
            self._node = start_node[0]
        else:
            self._node = start_node

        # Set the end_node to the first object if a list of nodes are passed
        if isinstance(end_node, list):
            self._node = end_node[0]
        else:
            self._node = end_node

        # Handles cases where the start_node is a Cluster or Group
        if isinstance(start_node, (Cluster, Group)) and isinstance(end_node, (Node, list)):
            cluster = start_node
            node_dict = get_node()
            center_node_index = round(len(node_dict[start_node])/2) - 1
            start_node = node_dict[start_node][center_node_index]
            self.edge_attrs.update({"ltail": cluster.name})
            self._node._graph.edge(start_node, end_node, **self.edge_attrs)

        # Handles cases where the end_node is a Cluster or Group
        elif isinstance(start_node, (Node, list)) and isinstance(end_node, (Cluster, Group)):
            cluster = end_node
            node_dict = get_node()
            center_node_index = round(len(node_dict[end_node])/2) - 1
            end_node = node_dict[end_node][center_node_index]
            self.edge_attrs.update({"lhead": cluster.name})
            self._node._graph.edge(start_node, end_node, **self.edge_attrs)

        # Handles cases where the start_node and end_node are a Cluster or Group
        elif isinstance(start_node, (Cluster, Group)) and isinstance(end_node, (Cluster, Group)):
            start_cluster = start_node
            end_cluster = end_node
            node_dict = get_node()
            start_center_node_index = round(len(node_dict[start_node])/2) - 1
            end_center_node_index = round(len(node_dict[end_node])/2) - 1
            start_node = node_dict[start_node][start_center_node_index]
            end_node = node_dict[end_node][end_center_node_index]
            self.edge_attrs.update({"ltail": start_cluster.name})
            self.edge_attrs.update({"lhead": end_cluster.name})
            self._node._graph.edge(start_node, end_node, **self.edge_attrs)

        # Handles the standard case of node to node connection
        else:
            self._node._graph.edge(start_node, end_node, **self.edge_attrs)