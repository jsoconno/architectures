from architectures.themes.settings import GraphSettings, ClusterSettings, NodeSettings, EdgeSettings

class _Theme():

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, item):
        return self.__dict__[item]

    def __repr__(self):
        return str(self.__dict__)

    def __iter__(self):
        return iter(self.__dict__.items())

    def get_delta_dict(self, first_dict, second_dict):
        """
        Compare two dictionaries and return a new dictionary
        that contains same keys with different values or new keys.
        """
        # create a merged dict
        merged_dict = {**first_dict, **second_dict}
        # create a new dict
        new_dict = {}
        for k, v in merged_dict.items():
            if k in first_dict:
                if first_dict[k] != v:
                    new_dict[k] = v
            else:
                new_dict[k] = v

        return new_dict

class Default(_Theme):
    """
    The Graphviz default theme.
    """

    def __init__(
        self, 
        graph_settings=None,
        cluster_settings=None,
        node_settings=None,
        edge_settings=None,
        color_settings=None
    ):
        self.graph_attrs = dict(GraphSettings())
        self.cluster_attrs = dict(ClusterSettings())
        self.node_attrs = dict(NodeSettings())
        self.edge_attrs = dict(EdgeSettings())
        self.colors = []

        if graph_settings is not None:
            self.graph_attrs.update(dict(graph_settings))

        if cluster_settings is not None:
            self.cluster_attrs.update(dict(cluster_settings))

        if node_settings is not None:
            self.node_attrs.update(dict(node_settings))

        if edge_settings is not None:
            self.edge_attrs.update(dict(edge_settings))

        if color_settings:
            self.colors = color_settings


class LightMode(_Theme):
    """
    A clean, light theme for general diagram creation.
    """

    def __init__(
        self, 
        graph_settings=None,
        cluster_settings=None,
        node_settings=None,
        edge_settings=None,
        color_settings=[]
    ):

        self.graph_attrs = dict(GraphSettings(
            bgcolor = "white",
            compound = True, 
            pad = 1.0,
            splines = "ortho",
            nodesep = 1.0,
            ranksep = 1.0,
            fontname = "calibri",
            fontsize = 24,
            fontcolor = "#2D3436",
            style = "rounded",
            rankdir = "LR",
            labeljust = "l",
            labelloc = 't',
        ))
        self.cluster_attrs = dict(ClusterSettings(
            style = "rounded",
            labeljust = "l",
            pencolor = "#AEB6BE",
            fontname = "calibri",
            fontsize = 12,
            margin = 30
        ))
        self.node_attrs = dict(NodeSettings(
            shape = "invis",
            style = "rounded,filled",
            fixedsize = True,
            width = 1.0,
            height = 1.0,
            labelloc = "b",
            imagescale = "true",
            fontname = "calibri",
            fontsize = 13,
            fontcolor = "#2D3436",
            color = "invis",
            fillcolor = "invis"
        ))
        self.edge_attrs = dict(EdgeSettings(
            penwidth = 2,
            minlen = 2.0,
            fontname = "calibri"
        ))
        self.colors = ["#FBFBFB", "#EDEDED", "#E0E0E0", "#D3D3D3"]

        _default_settings = Default()

        if graph_settings:
            custom_attrs = self.get_delta_dict(_default_settings.graph_attrs, dict(graph_settings))
            self.graph_attrs.update(custom_attrs)

        if cluster_settings:
            custom_attrs = self.get_delta_dict(_default_settings.cluster_attrs, dict(cluster_settings))
            self.cluster_attrs.update(custom_attrs)

        if node_settings:
            custom_attrs = self.get_delta_dict(_default_settings.node_attrs, dict(node_settings))
            self.node_attrs.update(custom_attrs)

        if edge_settings:
            custom_attrs = self.get_delta_dict(_default_settings.edge_attrs, dict(edge_settings))
            self.edge_attrs.update(custom_attrs)

        if color_settings:
            self.colors = color_settings

class DarkMode(_Theme):
    """
    A dark mode version of lightmode
    """

    def __init__(
        self, 
        graph_settings=None,
        cluster_settings=None,
        node_settings=None,
        edge_settings=None,
        color_settings=None
    ):

        self.graph_attrs = dict(GraphSettings(
            bgcolor = "#17202A",
            compound = True, 
            pad = 1.0,
            splines = "ortho",
            nodesep = 1.0,
            ranksep = 1.0,
            fontname = "calibri",
            fontsize = 24,
            fontcolor = "#EEEEEE",
            style = "rounded",
            rankdir = "LR",
            labeljust = "l",
            labelloc = 't',
        ))
        self.cluster_attrs = dict(ClusterSettings(
            style = "rounded,dotted",
            labeljust = "l",
            pencolor = "#AEB6BE",
            fontname = "calibri",
            fontsize = 12,
            fontcolor = "#EEEEEE",
            margin = 30
        ))
        self.node_attrs = dict(NodeSettings(
            shape = "invis",
            style = "rounded,filled",
            fixedsize = "true",
            width = 1.0,
            height = 1.0,
            labelloc = "b",
            imagescale = True,
            fontname = "calibri",
            fontsize = 13,
            fontcolor = "#EEEEEE",
            color = "invis",
            fillcolor = "invis"
        ))
        self.edge_attrs = dict(EdgeSettings(
            penwidth = 2,
            minlen = 2.0,
            color = "#EEEEEE"
        ))
        self.colors = ["#1C2833", "#212F3D", "#273746", "#2C3E50", "#566573"]

        _default_settings = Default()

        if graph_settings:
            custom_attrs = self.get_delta_dict(_default_settings.graph_attrs, dict(graph_settings))
            self.graph_attrs.update(custom_attrs)

        if cluster_settings:
            custom_attrs = self.get_delta_dict(_default_settings.cluster_attrs, dict(cluster_settings))
            self.cluster_attrs.update(custom_attrs)

        if node_settings:
            custom_attrs = self.get_delta_dict(_default_settings.node_attrs, dict(node_settings))
            self.node_attrs.update(custom_attrs)

        if edge_settings:
            custom_attrs = self.get_delta_dict(_default_settings.edge_attrs, dict(edge_settings))
            self.edge_attrs.update(custom_attrs)

        if color_settings:
            self.colors = color_settings