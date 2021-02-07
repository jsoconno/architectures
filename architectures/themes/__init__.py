from architectures.themes.settings import GraphSettings, ClusterSettings, NodeSettings, EdgeSettings, _Settings

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
        theme_graph_settings = GraphSettings().get_attributes()
        theme_cluster_settings = ClusterSettings().get_attributes()
        theme_node_settings = NodeSettings().get_attributes()
        theme_edge_settings = EdgeSettings().get_attributes()
        self.colors = []

        if isinstance(graph_settings, _Settings):
            graph_settings = graph_settings.get_attributes()

        if isinstance(cluster_settings, _Settings):
            cluster_settings = cluster_settings.get_attributes()

        if isinstance(node_settings, _Settings):
            node_settings = node_settings.get_attributes()

        if isinstance(edge_settings, _Settings):
            edge_settings = edge_settings.get_attributes()

        self.graph_attrs = theme_graph_settings | graph_settings
        self.cluster_attrs = theme_cluster_settings | cluster_settings
        self.node_attrs = theme_node_settings | node_settings
        self.edge_attrs = theme_edge_settings | edge_settings
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
            bgcolor = "#FFFFFF",
            compound = True,
            fontcolor = "#2D3436",
            fontname = "calibri",
            fontsize = 24.0,
            labeljust = "l",
            labelloc = 't',
            nodesep = 1.0,
            pad = 1.0,
            rankdir = "LR",
            ranksep = 1.0,
            splines = "ortho",
            style = "rounded",
        ).get_attributes()
        theme_cluster_settings = ClusterSettings(
            fontname = "calibri",
            fontsize = 12.0,
            labeljust = "l",
            margin = 30.0,
            pencolor = "#AEB6BE",
            style = "rounded",
        ).get_attributes()
        theme_node_settings = NodeSettings(
            color = "invis",
            fillcolor = "invis",
            fixedsize = True,
            fontcolor = "#2D3436",
            fontname = "calibri",
            fontsize = 13.0,
            height = 1.0,
            imagepos = "tc",
            imagescale = True,
            labelloc = "b",
            shape = "rectangle",
            style = "filled",
            width = 1.0,
        ).get_attributes()
        theme_edge_settings = EdgeSettings(
            fontname = "calibri",
            minlen = 2.0,
            penwidth = 2.0,
        ).get_attributes()
        self.colors = ["#FBFBFB", "#EDEDED", "#E0E0E0", "#D3D3D3"]

        if isinstance(graph_settings, _Settings):
            graph_settings = graph_settings.get_attributes()

        if isinstance(cluster_settings, _Settings):
            cluster_settings = cluster_settings.get_attributes()

        if isinstance(node_settings, _Settings):
            node_settings = node_settings.get_attributes()

        if isinstance(edge_settings, _Settings):
            edge_settings = edge_settings.get_attributes()

        self.graph_attrs = theme_graph_settings | graph_settings
        self.cluster_attrs = theme_cluster_settings | cluster_settings
        self.node_attrs = theme_node_settings | node_settings
        self.edge_attrs = theme_edge_settings | edge_settings
        if color_settings:
            self.colors = color_settings

class DarkMode(_Theme):
    """
    Lightmode, but cooler.
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
            compound = True,
            fontcolor = "#EEEEEE",
            fontname = "calibri",
            fontsize = 24.0,
            labeljust = "l",
            labelloc = 't',
            nodesep = 1.0,
            pad = 1.0,
            splines = "ortho",
            style = "rounded",
            rankdir = "LR",
            ranksep = 1.0,
        ).get_attributes()
        theme_cluster_settings = ClusterSettings(
            fontcolor = "#EEEEEE",
            fontname = "calibri",
            fontsize = 12.0,
            labeljust = "l",
            margin = 30.0,
            pencolor = "#AEB6BE",
            style = "rounded",
        ).get_attributes()
        theme_node_settings = NodeSettings(
            color = "invis",
            fillcolor = "invis",
            fixedsize = True,
            fontcolor = "#EEEEEE",
            fontname = "calibri",
            fontsize = 13.0,
            height = 1.0,
            imagepos = "tc",
            imagescale = True,
            labelloc = "b",
            shape = "rectangle",
            style = "filled",
            width = 1.0,
        ).get_attributes()
        theme_edge_settings = EdgeSettings(
            color = "#EEEEEE",
            fontname = "calibri",
            minlen = 2.0,
            penwidth = 2.0,
        ).get_attributes()
        self.colors = ["#1C2833", "#212F3D", "#273746", "#2C3E50", "#566573"]

        if isinstance(graph_settings, _Settings):
            graph_settings = graph_settings.get_attributes()

        if isinstance(cluster_settings, _Settings):
            cluster_settings = cluster_settings.get_attributes()

        if isinstance(node_settings, _Settings):
            node_settings = node_settings.get_attributes()

        if isinstance(edge_settings, _Settings):
            edge_settings = edge_settings.get_attributes()

        self.graph_attrs = theme_graph_settings | graph_settings
        self.cluster_attrs = theme_cluster_settings | cluster_settings
        self.node_attrs = theme_node_settings | node_settings
        self.edge_attrs = theme_edge_settings | edge_settings

        if color_settings:
            self.colors = color_settings