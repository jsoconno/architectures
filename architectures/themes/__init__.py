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
        graph_settings=GraphSettings(),
        cluster_settings=ClusterSettings(),
        node_settings=NodeSettings(),
        edge_settings=EdgeSettings(),
        color_settings=None
    ):
        theme_graph_settings = GraphSettings()
        theme_cluster_settings = ClusterSettings()
        theme_node_settings = NodeSettings()
        theme_edge_settings = EdgeSettings()
        self.colors = []

        self.graph_attrs = theme_graph_settings.get_attributes() | graph_settings.get_attributes()
        self.cluster_attrs = theme_cluster_settings.get_attributes() | cluster_settings.get_attributes()
        self.node_attrs = theme_node_settings.get_attributes() | node_settings.get_attributes()
        self.edge_attrs = theme_edge_settings.get_attributes() | edge_settings.get_attributes()

        if color_settings:
            self.colors = color_settings


class LightMode(_Theme):
    """
    A clean, light theme for general diagram creation.
    """

    def __init__(
        self, 
        graph_settings=GraphSettings(),
        cluster_settings=ClusterSettings(),
        node_settings=NodeSettings(),
        edge_settings=EdgeSettings(),
        color_settings=None
    ):

        theme_graph_settings = GraphSettings(
            pad = 1.0,
            splines = "ortho",
            nodesep = 1.0,
            ranksep = 1.0,
            fontname = "calibri",
            fontsize = 24.0,
            fontcolor = "#2D3436",
            style = "rounded",
            rankdir = "LR",
            labeljust = "l",
            labelloc = 't',
        )
        theme_cluster_settings = ClusterSettings(
            style = "rounded",
            labeljust = "l",
            pencolor = "#AEB6BE",
            fontname = "calibri",
            fontsize = 12.0,
            margin = 30.0
        )
        theme_node_settings = NodeSettings(
            shape = "rectangle",
            style = "filled",
            fixedsize = True,
            width = 1.0,
            height = 1.0,
            labelloc = "b",
            imagepos = "tc",
            imagescale = True,
            fontname = "calibri",
            fontsize = 13.0,
            fontcolor = "#2D3436",
            color = "invis",
            fillcolor = "invis"
        )
        theme_edge_settings = EdgeSettings(
            penwidth = 2.0,
            minlen = 2.0,
            fontname = "calibri"
        )
        self.colors = ["#FBFBFB", "#EDEDED", "#E0E0E0", "#D3D3D3"]

        self.graph_attrs = theme_graph_settings.get_attributes() | graph_settings.get_attributes()
        self.cluster_attrs = theme_cluster_settings.get_attributes() | cluster_settings.get_attributes()
        self.node_attrs = theme_node_settings.get_attributes() | node_settings.get_attributes()
        self.edge_attrs = theme_edge_settings.get_attributes() | edge_settings.get_attributes()

        if color_settings:
            self.colors = color_settings

class DarkMode(_Theme):
    """
    A clean, light theme for general diagram creation.
    """

    def __init__(
        self, 
        graph_settings=GraphSettings(),
        cluster_settings=ClusterSettings(),
        node_settings=NodeSettings(),
        edge_settings=EdgeSettings(),
        color_settings=None
    ):

        theme_graph_settings = GraphSettings(
            bgcolor = "#17202A",
            pad = 1.0,
            splines = "ortho",
            nodesep = 1.0,
            ranksep = 1.0,
            fontname = "calibri",
            fontsize = 24.0,
            fontcolor = "#EEEEEE",
            style = "rounded",
            rankdir = "LR",
            labeljust = "l",
            labelloc = 't',
        )
        theme_cluster_settings = ClusterSettings(
            style = "rounded",
            labeljust = "l",
            pencolor = "#AEB6BE",
            fontname = "calibri",
            fontsize = 12.0,
            fontcolor = "#EEEEEE",
            margin = 30.0
        )
        theme_node_settings = NodeSettings(
            shape = "rectangle",
            style = "filled",
            fixedsize = True,
            width = 1.0,
            height = 1.0,
            labelloc = "b",
            imagepos = "tc",
            imagescale = True,
            fontname = "calibri",
            fontsize = 13.0,
            fontcolor = "#EEEEEE",
            color = "invis",
            fillcolor = "invis"
        )
        theme_edge_settings = EdgeSettings(
            penwidth = 2.0,
            minlen = 2.0,
            fontname = "calibri",
            color = "#EEEEEE"
        )
        self.colors = ["#1C2833", "#212F3D", "#273746", "#2C3E50", "#566573"]

        self.graph_attrs = theme_graph_settings.get_attributes() | graph_settings.get_attributes()
        self.cluster_attrs = theme_cluster_settings.get_attributes() | cluster_settings.get_attributes()
        self.node_attrs = theme_node_settings.get_attributes() | node_settings.get_attributes()
        self.edge_attrs = theme_edge_settings.get_attributes() | edge_settings.get_attributes()

        if color_settings:
            self.colors = color_settings