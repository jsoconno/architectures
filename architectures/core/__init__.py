"""
This module contains all core classes required for drawing diagrams.

Available Classes:
- Graph
- Cluster
- Node
- Edge
- Flow

Available Functions:
- get_graph
- set_graph
- get_cluster
- set_cluster
- get_state
- set_state
- update_state
- search_state
- wrap_text
- get_node_obj

Details for each can be found in the docstrings for the respective class or function.
"""
from __future__ import annotations

import contextvars
import os
from pathlib import Path
from typing import Any, Union

from graphviz import Digraph

from architectures.themes import Default

__graph = contextvars.ContextVar("graph")
__cluster = contextvars.ContextVar("cluster")
__state = contextvars.ContextVar("state")


def get_graph() -> Union[None, Graph]:
    """
    Get the current graph context.
    """
    try:
        return __graph.get()
    except LookupError:
        return None


def set_graph(graph: Union[None, Graph]) -> None:
    """
    Set the current graph context.
    """
    __graph.set(graph)


def get_cluster() -> Union[None, Cluster]:
    """
    Get the current cluster context.
    """
    try:
        return __cluster.get()
    except LookupError:
        return None


def set_cluster(cluster: Cluster) -> None:
    """
    Set the current cluster context.
    """
    __cluster.set(cluster)


def get_state() -> Union[None, dict]:
    """
    Get the current node to cluster mapping.
    """
    try:
        return __state.get()
    except LookupError:
        return None


def set_state(state: dict) -> None:
    """
    Set a node to cluster mapping.
    """
    __state.set(state)


def update_state(state: dict, target_key: Union[Cluster, Node], target_value: Union[dict, Node]) -> dict:
    """
    Create a map of all resources hierarchial relationship as a nested dictionary.
    """
    if isinstance(state, dict):
        for k, v in state.items():
            if k is target_key:
                v.append(target_value)
            else:
                if isinstance(v, list):
                    for i in v:
                        update_state(i, target_key, target_value)

        return {k: v}


def search_state(search_dict: dict, search_key: Cluster, output: list = None) -> list:
    """
    Search nested dicts and lists for the search_value (key)
    and return the corresponding value.
    """
    if output is None:
        output = []
    
    for k, v in search_dict.items():
        if k is not search_key and isinstance(v, list):
            for item in v:
                if isinstance(item, dict):
                    search_state(item, search_key, output)
        else:
            for item in v:
                output.append(item)

    return output

def wrap_text(text: str, max_length: int = 16) -> str:
    """Return a new label with wrapped text.

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


def get_node_obj(obj: Union[Cluster, Node]) -> Node:
    """Return the most central Node in a Cluster.

    Parameters
    ----------
    obj : Cluster, Node
        A Cluster, Group, or Node object

    Returns
    -------
    Node
        The most centrally located Node object
    """
    if isinstance(obj, Cluster):
        state = get_state()
        values = search_state(state, obj)
        if any(isinstance(x, Node) for x in values):
            node_list = [item for item in values if isinstance(item, Node)]
            count = len(node_list)
            center_node_index = round(count/2) - 1
            obj = node_list[center_node_index]
        else:
            for item in values:
                if isinstance(item, dict):
                    for k, v in item.items():
                        return get_node_obj(k)
    
    return obj


class Graph():
    """
    Create and set default settings for a graph and its clusters, nodes, and edges.
    """
    def __init__(self, name: str = "My Architecture",
                 output_file_format: str = "png",
                 theme: Any = None, show: bool = True,
                 **attrs: Any
                 ) -> None:
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
        self.dot.graph_attr.update(attrs)
        self.dot.graph_attr["label"] = self.name

        # Set global node attributes
        self.dot.node_attr.update(self.theme.node_attrs)

        # Set global edge attributes
        self.dot.edge_attr.update(self.theme.edge_attrs)

        # Set option to show architecture diagram
        self.show = show

        # Set initial state to just the Graph
        set_state({self: []})

    # def __str__(self) -> str:
    #     return str(self.dot)

    def __enter__(self) -> Graph:
        set_graph(self)
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.render()
        # Remove the graphviz file leaving only the image.
        os.remove(self.output_file_name)
        set_graph(None)

    def node(self, name: str, label: str, **attrs: Any) -> None:
        """
        Create a node.
        """
        self.dot.node(name, label=label, **attrs)

    def edge(self, start_node: Node, end_node: Node, **attrs: Any) -> None:
        """
        Connect individual or lists of nodes with edges.
        """
        self.dot.edge(start_node.id, end_node.id, **attrs)

    def subgraph(self, dot: Digraph) -> None:
        """
        Create a subgraph for grouping nodes.
        """
        self.dot.subgraph(dot)

    def render(self) -> None:
        """
        Generate output file.
        """
        self.dot.render(format=self.output_file_format, view=self.show, quiet=True)


class Cluster():
    """
    Create a cluster.
    """

    _default_label = None

    def __init__(self, label: str = "", hide_border: bool = False, **attrs: Any) -> None:
        """
        :param label str: Label for the cluster.
        :param bool hide_border: Determines whether or not a border is shown around the cluster.
        """

        # Set the cluster id
        self.id = "cluster_" + str(id(self))

        #Set the cluster label
        if label == "" and self._default_label:
            self.label = self._default_label
        else:
            self.label = label

        # Create cluster
        self.dot = Digraph(self.id)

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
            _color_index = self._depth % len(_colors)
            self.dot.graph_attr["bgcolor"] = _colors[_color_index]

        # Update cluster label
        self.dot.graph_attr["label"] = self.label

        # Make group border invisible
        if hide_border:
            self.dot.graph_attr["penwidth"] = "0"
            self.dot.graph_attr["bgcolor"] = "invis"

        # Override any values directly passed from the object
        self.dot.graph_attr.update(attrs)

        # Add Clusters to state
        state = get_state()
        if self._cluster:
            state = update_state(state, self._cluster, {self: []})
        else:
            state = update_state(state, self._graph, {self: []})
        set_state(state)

    def __enter__(self) -> Cluster:
        set_cluster(self)
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        if self._cluster:
            self._cluster.subgraph(self.dot)
        else:
            self._graph.subgraph(self.dot)
        set_cluster(self._cluster)

    def node(self, name: str, label: str, **attrs: Any) -> None:
        """
        Create a node in the cluster.
        """
        self.dot.node(name, label=label, **attrs)

    def subgraph(self, dot: Digraph = Digraph) -> None:
        """
        Create a subgraph of the cluster.
        """
        self.dot.subgraph(dot)


class Node():
    """
    Creates a node.  This can be a standard node or a node representing a service from a provider.
    """

    _provider = None
    _service_type = None

    _icon_dir = None
    _icon = None

    _default_label = None

    def __init__(self, label: str = "",
                 hide_node: bool = False,
                 wrap_label_text: bool = True,
                 **attrs: Any
                 ) -> None:
        """
        :param str label: Label for a node.
        :param bool hide_node: Determines whether or not a node should act as a hidden node with not width or height.
        """
        # Generate an ID used to uniquely identify a node
        self.id = "node_" + str(id(self))

        # Set hide_node attribute
        self.hide_node = hide_node

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

        if self.label == "":
            baseline_padding = 0.0
        else:
            baseline_padding = 0.5

        # Add attributes specific for when provider service nodes are used.
        if self._icon:
            padding = baseline_padding + (0.15 * (self.label.count('\n')))
            self.node_attrs["height"] = str(float(self.node_attrs['height']) + padding)
            self.node_attrs["image"] = self._load_icon()

        # Set the width and height to be 0
        if hide_node:
            self.node_attrs.update({"width":"0", "height":"0"})

        # If a node is in the cluster context, add it to cluster.
        if self._cluster:
            self._cluster.node(self.id, self.label, **self.node_attrs)
        else:
            self._graph.node(self.id, self.label, **self.node_attrs)

        # Add Nodes to state
        state = get_state()
        if self._cluster:
            state = update_state(state, self._cluster, self)
        else:
            state = update_state(state, self._graph, self)
        set_state(state)

    def _load_icon(self) -> str:
        basedir = Path(os.path.abspath(os.path.dirname(__file__)))
        return os.path.join(basedir.parent.parent, self._icon_dir, self._icon)

class Edge():
    """
    Creates an edge between two nodes.
    """

    def __init__(self, start_obj: Union[Cluster, Group, Node],
                 end_obj: Union[Cluster, Group, Node],
                 **attrs: Any
                 ) -> None:
        """
        :param start: The origin cluster, group, or node object.
        :param end: The destination cluster, group, or node object.
        :param attrs: Other edge attributes.
        """

        self.id = "edge_" + str(id(self))

        self.start_obj = start_obj
        self.end_obj = end_obj

        # Get global graph and cluster context to ensure the node is part of the graph or cluster
        self._graph = get_graph()
        if self._graph is None:
            raise EnvironmentError("The object is not part of a Graph")
        self._state = get_state()

        # Set edge attributes based on the theme using copy to ensure the objects are independent
        self.edge_attrs = self._graph.theme.edge_attrs.copy()

        if not isinstance(self.start_obj, list):
            self.start_obj = [self.start_obj]
        
        if not isinstance(self.end_obj, list):
            self.end_obj = [self.end_obj]

        start_obj_list = self.start_obj
        end_obj_list = self.end_obj

        # Handle all cases
        for current_start_obj in start_obj_list:
            for current_end_obj in end_obj_list:
                start_node = get_node_obj(current_start_obj)
                end_node = get_node_obj(current_end_obj)

                # Cluster to Cluster connections
                if isinstance(current_start_obj, Cluster) and isinstance(current_end_obj, Cluster):
                    self.edge_attrs.update({"ltail": current_start_obj.id, "lhead": current_end_obj.id})
                    self_reference = current_start_obj == current_end_obj
                # Cluster to Node connections
                elif isinstance(current_start_obj, Cluster) and isinstance(current_end_obj, Node):
                    self.edge_attrs.update({"ltail": current_start_obj.id, "lhead": ""})
                    self_reference = start_node == current_end_obj
                # Node to Cluster connections
                elif isinstance(current_start_obj, Node) and isinstance(current_end_obj, Cluster):
                    self.edge_attrs.update({"ltail": "", "lhead": current_end_obj.id})
                    self_reference = current_start_obj == end_node
                # Node to Node connections
                else:
                    self.edge_attrs.update({"ltail": "", "lhead": ""})
                    self_reference = start_node == end_node

                # Update the type of edge based on if the object is an anchor
                if isinstance(current_end_obj, Node) and current_end_obj.hide_node:
                    self.edge_attrs.update({"dir":"none"})

                # Override any attributes directly passed from the object
                self.edge_attrs.update(attrs)

                # Create the connection between Nodes
                if not self_reference:
                    self._graph.edge(start_node, end_node, **self.edge_attrs)


class Flow():
    """
    Another method of connecting nodes by allowing users to define a flow as a list.
    """
    def __init__(self, objs: list[Union[Cluster, Node]], **attrs: Any) -> None:

        self.id = "flow_" + str(id(self))

        self.objs = objs
        self.obj_count = len(self.objs)

        # Get global graph and cluster context to ensure the node is part of the graph or cluster
        self._graph = get_graph()
        if self._graph is None:
            raise EnvironmentError("The object is not part of a Graph")

        # Set edge attributes based on attributes directly passed from the object
        self.edge_attrs = attrs

        # Make sure there is more than one node
        if self.obj_count > 1:

            # For every node in the list
            for i in range(self.obj_count):

                # Set the start and end node
                if i < self.obj_count - 1:
                    self.start_obj = self.objs[i]
                    self.end_obj = self.objs[i + 1]

                    Edge(self.start_obj, self.end_obj, **self.edge_attrs)
        else:
            raise Exception('More than one object must be passed in the list to use Flow')


Canvas = Graph
Connection = Edge
Container = Cluster
