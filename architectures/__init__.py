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
    def __init__(self, name="", output_file_name="", output_file_format="png", settings=None, show=True, engine='dot'):
        """
        :param name ...
        :param output_file_name ...
        :param output_file_format ...
        :param settings ...
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

        # Set settings
        if settings is None:
            self.settings = Setting()
        else:
            self.settings = settings

        # Set global graph attributes
        for k, v in self.settings.graph_attrs.items():
            self.dot.graph_attr[k] = v

        self.dot.graph_attr["label"] = self.name

        # Set global node attributes
        for k, v in self.settings.node_attrs.items():
            self.dot.node_attr[k] = v

        # Set global edge attributes
        for k, v in self.settings.edge_attrs.items():
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

    def connect(self, node: "Node", node2: "Node", edge: "Edge") -> None:
        """Connect the two Nodes."""
        self.dot.edge(node.node_id, node2.node_id, **edge.attrs)

    def subgraph(self, dot: Digraph) -> None:
        """Create a subgraph for clustering"""
        self.dot.subgraph(dot)

    def render(self) -> None:
        self.dot.render(format=self.output_file_format, view=self.show, quiet=True)

class Cluster():
    """
    Creates a cluster in the architecture diagram.
    """
    __background_colors = ("#FFFFFF")

    def __init__(self, label="cluster", settings=None):
        """Cluster represents a cluster context.
        :param label: Cluster label.
        :param settings: Data flow direction. Default is 'left to right'.
        """

        # Set the cluster label
        self.label = label

        # Set the cluster name
        self.name = "cluster_" + self.label

        # Create cluster
        self.dot = Digraph(self.name)

        # Set settings
        if settings is None:
            self.settings = Setting()
        else:
            self.settings = settings

        # Set cluster attributes.
        for k, v in self.settings.cluster_attrs.items():
            self.dot.graph_attr[k] = v
        self.dot.graph_attr["label"] = self.label

        # Node must be belong to a diagrams.
        self._diagram = get_diagram()
        if self._diagram is None:
            raise EnvironmentError("Global diagrams context not set up")
        self._parent = get_cluster()

        # Set cluster depth for distinguishing the background color
        self.depth = self._parent.depth + 1 if self._parent else 0
        color_index = self.depth % len(self.__background_colors)
        self.dot.graph_attr["background_color"] = self.__background_colors[color_index]


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

    _height = 1.9

    def __init__(self, label="", settings=None):
        """Node represents a system component.
        :param label: Node label.
        """
        # Generates an ID for identifying a node.
        self._id = self._rand_id()
        self.label = label

        # Set settings
        if settings is None:
            self.settings = Setting()
        else:
            self.settings = settings

        # Set node attributes
        for k, v in self.settings.node_attrs.items():
            self.dot.node_attr[k] = v

        # fmt: off
        # If a node has an icon, increase the height slightly to avoid
        # that label being spanned between icon image and white space.
        # Increase the height by the number of new lines included in the label.
        padding = 0.4 * (label.count('\n'))
        self._attrs = {
            "shape": "none",
            "height": str(self._height + padding),
            "image": self._load_icon(),
        } if self._icon else {}

        self._attrs.update(settings)

        # Node must be belong to a diagrams.
        self._diagram = get_diagram()
        if self._diagram is None:
            raise EnvironmentError("Global diagrams context not set up")
        self._cluster = get_cluster()

        # If a node is in the cluster context, add it to cluster.
        if self._cluster:
            self._cluster.node(self._id, self.label, **self._attrs)
        else:
            self._diagram.node(self._id, self.label, **self._attrs)

    @property
    def node_id(self):
        return self._id

    @staticmethod
    def _rand_id():
        return uuid.uuid4().hex

    def _load_icon(self):
        basedir = Path(os.path.abspath(os.path.dirname(__file__)))
        return os.path.join(basedir.parent, self._icon_dir, self._icon)

class Edge():
    """
    Creates an edge between two nodes on an architecture diagram.
    """
    pass

class Setting():
    """
    Creates an objects that holds settings be be used by Graph, Cluster, Node, and Edge
    """

    def __init__(self, graph_attrs={}, cluster_attrs={}, node_attrs={}, edge_attrs={}):
        """
        :param graph_attr: Provide graph_attr dot config attributes.
        :param node_attr: Provide node_attr dot config attributes.
        :param edge_attr: Provide edge_attr dot config attributes.
        """

        self.graph_attrs = {
            "compound": "true", 
            "pad": "1.0",
            "splines": "ortho",
            "nodesep": "0.5",
            "ranksep": "1.0",
            "fontname": "Sans-Serif",
            "fontsize": "15",
            "fontcolor": "#2D3436",
            "style": "rounded",
            "rankdir": "LR",
            "labeljust": "l",
            "labelloc": 't'
        }

        # Update these to meet out standards
        self.cluster_attrs = {
            "shape": "box",
            "style": "rounded",
            "labeljust": "l",
            "pencolor": "#AEB6BE",
            "fontname": "Sans-Serif",
            "fontsize": "12",
        }

        self.node_attrs = {
            "shape": "box",
            "style": "rounded",
            "fixedsize": "true",
            "width": "1.0",
            "height": "1.8",
            "labelloc": "b",
            "imagescale": "true",
            "fontname": "Sans-Serif",
            "fontsize": "13",
            "fontcolor": "#2D3436",
            "color": "white"
        }

        self.edge_attrs = {
            "penwidth": "2",
            "margin": "1",
            "minlen": "1.0"
        }

        self.graph_attrs.update(graph_attrs)
        self.cluster_attrs.update(cluster_attrs)
        self.node_attrs.update(node_attrs)
        self.edge_attrs.update(edge_attrs)