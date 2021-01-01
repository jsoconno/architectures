import contextvars
import os
import uuid
from pathlib import Path
from typing import List, Union, Dict

from graphviz import Digraph

__diagram = contextvars.ContextVar("diagrams")
__cluster = contextvars.ContextVar("cluster")

def get_diagram():
    try:
        return __diagram.get()
    except LookupError:
        return None


def set_diagram(diagram):
    __diagram.set(diagram)


def get_cluster():
    try:
        return __cluster.get()
    except LookupError:
        return None


def set_cluster(cluster):
    __cluster.set(cluster)

class Graph():
    """
    Creates the base graph for an architecture diagram.
    """
    def __init__(self, name="", output_file_name="", output_file_format="png", theme=None, show=True, engine='dot'):
        """
        :param name ...
        :param output_file_name ...
        :param output_file_format ...
        :param theme ...
        :param show ...
        """

        # Set graph and output file name
        self.name = name
        if not name and not output_file_name:
          output_file_name = "architecture_diagram"
        elif not output_file_name:
            output_file_name = "_".join(self.name.split()).lower()
        self.output_file_name = output_file_name
        self.output_file_format = output_file_format

        self.dot = Digraph(name=self.name, filename=self.output_file_name, engine=engine)

        # Set theme
        if theme is None:
            self.theme = Setting()
        else:
            self.theme = theme

        # Set global graph attributes
        for k, v in self.theme.graph_attrs.items():
            self.dot.graph_attr[k] = v

        self.dot.graph_attr["label"] = self.name

        # Set global node attributes
        for k, v in self.theme.node_attrs.items():
            self.dot.node_attr[k] = v

        # Set global edge attributes
        for k, v in self.theme.edge_attrs.items():
            self.dot.edge_attr[k] = v

        # Set option to show architecture diagram
        self.show = show

    def __str__(self) -> str:
        return str(self.dot)

    def __enter__(self):
        set_diagram(self)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.render()
        # Remove the graphviz file leaving only the image.
        os.remove(self.output_file_name)
        set_diagram(None)

    def node(self, node_id, label, **attrs) -> None:
        """Create a new node."""
        self.dot.node(node_id, label=label, **attrs)

    def connect(self, node: "Node", node2: "Node", **attrs) -> None:
        """Connect the two Nodes."""
        if isinstance(node, list) and isinstance(node2, list):
            for n in node:
                for n2 in node2:
                    self.dot.edge(n.node_id, n2.node_id, **attrs)
        elif isinstance(node, list):
            for n in node:
                self.dot.edge(n.node_id, node2.node_id, **attrs)
        elif isinstance(node2, list):
            for n in node2:
                self.dot.edge(node.node_id, n.node_id, **attrs)
        else:
            self.dot.edge(node.node_id, node2.node_id, **attrs)

    def subgraph(self, dot: Digraph) -> None:
        """Create a subgraph for clustering"""
        self.dot.subgraph(dot)

    def render(self) -> None:
        self.dot.render(format=self.output_file_format, view=self.show, quiet=True)

class Cluster():
    """
    Creates a cluster in the architecture diagram.
    """
    __background_colors = ("#FFFFFF", "#FFFFFF")

    def __init__(self, label="cluster", background_colors=False):
        """Cluster represents a cluster context.
        :param label: Cluster label.
        """

        # Set the cluster label
        self.label = label

        # Set the cluster name
        self.name = "cluster_" + self.label

        # Create cluster
        self.dot = Digraph(self.name)

        self.dot.graph_attr["label"] = self.label

        # Node must be belong to a diagrams.
        self._diagram = get_diagram()
        if self._diagram is None:
            raise EnvironmentError("Global diagrams context not set up")
        self._parent = get_cluster()

        # Set cluster depth for distinguishing the background color
        self.depth = self._parent.depth + 1 if self._parent else 0
        color_index = self.depth % len(self.__background_colors)

        if background_colors:
            self.dot.graph_attr["bgcolor"] = self.__background_colors[color_index]


    def __enter__(self):
        set_cluster(self)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self._parent:
            self._parent.subgraph(self.dot)
        else:
            self._diagram.subgraph(self.dot)
        set_cluster(self._parent)

    def node(self, node_id: str, label: str, **attrs) -> None:
        """Create a new node in the cluster."""
        self.dot.node(node_id, label=label, **attrs)

    def subgraph(self, dot=Digraph):
        self.dot.subgraph(dot)


class Group(Cluster):
    """
    Creates a special type of group used only or organizing nodes.
    """
    pass

class Node():
    """
    Creates a node on the architecture diagram which correlates with a service.
    """
    """Node represents a node for a specific backend service."""

    _provider = None
    _type = None

    _icon_dir = None
    _icon = None

    _height = 1.5

    def __init__(self, label="", **attrs):
        """Node represents a system component.
        :param label: Node label.
        """
        # Generate an ID used to uniquely identify a node
        self._id = self._rand_id()

        # Set the label based on what the user passes to the object
        self.label = label

        # Make sure that the node is part of the graph
        self._diagram = get_diagram()
        if self._diagram is None:
            raise EnvironmentError("Global diagrams context not set up")
        self._cluster = get_cluster()

        self.node_attrs = self._diagram.theme.node_attrs

        # Add appropriate padding for icon label
        padding = 0.4 * (label.count('\n'))

        self._attrs = {
            #"shape": "none",
            "height": str(float(self.node_attrs['height']) + padding),
            "image": self._load_icon(),
        } if self._icon else {}

        self.node_attrs.update(self._attrs)

        # If a node is in the cluster context, add it to cluster.
        if self._cluster:
            self._cluster.node(self._id, self.label, **self.node_attrs)
        else:
            self._diagram.node(self._id, self.label, **self.node_attrs)

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
    Creates an edge between two nodes on an architecture diagram.
    """
    _default_edge_attrs = {
        "fontcolor": "#2D3436",
        "fontname": "Sans-Serif",
        "fontsize": "13",
    }

    def __init__(
        self,
        start_node,
        end_node,
        **attrs: Dict,
    ):
        """Edge represents an edge between two nodes.
        :param start_node
        :param end_node
        :param attrs: Other edge attributes
        """
        if start_node is not None:
            assert isinstance(start_node, (Node, list))

        if end_node is not None:
            assert isinstance(end_node, (Node, list))

        self.start_node = start_node
        self.end_node = end_node

        if isinstance(start_node, list):
            self._node = start_node[0]
        else:
            self._node = start_node

        self._node._diagram.connect(start_node, end_node, **attrs)