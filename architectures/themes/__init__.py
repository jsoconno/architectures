default_graph_attrs = {
    "bgcolor": "white",
    "center": "false",
    "charset": "utf-8",
    "clusterrank": "local",
    "colorscheme": "",
    "comment": "",
    "compound": "true",
    "concentrate": "false",
    "fontcolor": "black",
    "fontname": "times-roman",
    "fontpath": "system-dependent",
    "fontsize": "14",
    "forcelabels": "true",
    "gradientangle": "",
    "imagepath": "",
    "label": "",
    "labeljust": "c",
    "labelloc": "b",
    "landscape": "false",
    "layout": "dot",
    "margin": "8",
    "mclimit": "1",
    "newrank": "false",
    "nodesep": "0.25",
    "nojustify": "false",
    "nslimit": "",
    "nslimit1": "",
    "ordering": "",
    "orientation": "0",
    "outputorder": "breadthfirst",
    "pack": "false",
    # "packmode": "node",
    "pad": "0.0555",
    "pagedir": "bl",
    "quantum": "0.0",
    "rankdir": "TB",
    "ranksep": "0.5",
    "ratio": "auto",
    "remincross": "true",
    "rotate": "0",
    "searchsize": "30",
    "showboxes": "0",
    "size": "",
    "sortv": "0",
    "splines": "line",
    "style": "",
    "viewport": "",
}

default_cluster_attrs = {
    "bgcolor": "transparent",
    "color": "black",
    "colorscheme": "",
    "fillcolor": "black",
    "fontcolor": "black",
    "fontname": "times-roman",
    "fontsize": "14",
    "gradientangle": "",
    "label": "",
    "labeljust": "c",
    "labelloc": "t",
    "layer": "",
    "margin": "8",
    "nojustify": "false",
    "pencolor": "black",
    "penwidth": "1",
    "peripheries": "1",
    "sortv": "0",
    "style": "",
}

default_node_attrs = {
    "color": "black",
    "colorscheme": "",
    "comment": "",
    "distortion": "0",
    "fillcolor": "lightgrey",
    "fixedsize": "false",
    "fontcolor": "black",
    "fontname": "times-roman",
    "fontsize": "14",
    "gradientangle": "",
    "group": "",
    "height": "0.5",
    # "image": "",
    "imagepos": "mc",
    "imagescale": "false",
    # "label": "",
    "labelloc": "c",
    "layer": "",
    "margin": "0.11,0.055",
    "nojustify": "false",
    "ordering": "",
    "orientation": "0",
    "penwidth": "1",
    "peripheries": "1",
    "pos": "",
    "regular": "false",
    "shape": "ellipse",
    "shapefile": "",
    "showboxes": "0",
    "sides": "4",
    "skew": "0",
    "sortv": "0",
    "style": "",
    "width": "0.75",
    # "xlabel": "",
}

default_edge_attrs = {
    "arrowhead": "normal",
    "arrowsize": "1",
    "arrowtail": "normal",
    "color": "black",
    "colorscheme": "",
    "comment": "",
    "constraint": "true",
    "decorate": "false",
    "dir": "forward",
    "fillcolor": "black",
    "fontcolor": "black",
    "fontname": "times-roman",
    "fontsize": "14",
    "headclip": "true",
    "headlabel": "",
    "headport": "center",
    "label": "",
    "labelangle": "-25",
    "labeldistance": "1",
    "labelfloat": "false",
    "labelfontcolor": "black",
    "labelfontname": "times-roman",
    "labelfontsize": "14",
    "layer": "",
    "lhead": "",
    "ltail": "",
    "minlen": "1",
    "nojustify": "false",
    "penwidth": "1",
    "pos": "",
    "samehead": "",
    "sametail": "",
    "showboxes": "0",
    "style": "",
    "tailclip": "true",
    "taillabel": "",
    "tailport": "center",
    "weight": "1",
    "xlabel": "",
}

def get_color_pallet(hue):
    """
    Pre-defined hues for LightMode
    """
    if hue == "white":
        return ["#FDFEFE", "#F7F9F9", "#F4F6F7", "#ECF0F1"]
    elif hue == "red":
        return ["#FAEAEA", "#F6D6D5", "#F1C1C0", "#ECADAB"]
    elif hue == "orange":
        return ["#FFF0E6", "#FFE0CC", "#FFD1B3", "#FFC299"]
    elif hue == "yellow":
        return ["#FFF9E6", "#FFF3CC", "#FFEDB3", "#FFE799"]
    elif hue == "green":
        return ["#EBF7F1", "#D7F0E2", "#C3E8D4", "#AFE1C5"]
    elif hue == "blue":
        return ["#EBF4FA" "#D7E9F5", "#C3DEEF", "#AFD3EA"]
    elif hue == "purple":
        return ["#EEEAF2", "#DCD6E5", "#CBC1D8", "#BAACCB"]
    else:
        ["#FFFFFF"]
class _Theme():

    def __init__(self):
        pass

class Default(_Theme):

    def __init__(self, graph_attr_overrides={}, cluster_attr_overrides={}, node_attr_overrides={}, edge_attr_overrides={}, color_overrides=[]):
    
        self.graph_attrs = default_graph_attrs
        self.cluster_attrs = default_cluster_attrs
        self.edge_attrs = default_edge_attrs
        self.node_attrs = default_node_attrs
        self.colors = []

        if graph_attr_overrides is not None:
            self.graph_attrs.update(graph_attr_overrides)

        if cluster_attr_overrides is not None:
            self.cluster_attrs.update(cluster_attr_overrides)

        if node_attr_overrides is not None:
            self.node_attrs.update(node_attr_overrides)

        if edge_attr_overrides is not None:
            self.edge_attrs.update(edge_attr_overrides)

        if color_overrides:
            self.colors = color_overrides


class LightMode(_Theme):

    def __init__(self, graph_attr_overrides={}, cluster_attr_overrides={}, node_attr_overrides={}, edge_attr_overrides={}, color_overrides=[], hue="white"):

        self.graph_attrs = {
            "bgcolor": "white",
            "compound": "true", 
            "pad": "1.0",
            "splines": "ortho",
            "nodesep": "1.0",
            "ranksep": "1.0",
            "fontname": "Calibri",
            "fontsize": "24",
            "fontcolor": "#2D3436",
            "style": "rounded",
            "rankdir": "LR",
            "labeljust": "l",
            "labelloc": 't',
        }

        self.cluster_attrs = {
            "shape": "box",
            "style": "rounded",
            "labeljust": "l",
            "pencolor": "#AEB6BE",
            "fontname": "Calibri",
            "fontsize": "12",
            "margin": "30"
        }

        self.node_attrs = {
            "shape": "invis",
            "style": "rounded,filled",
            "fixedsize": "true",
            "width": "1.0",
            "height": "1.8",
            "labelloc": "b",
            "imagescale": "true",
            "fontname": "Calibri",
            "fontsize": "13",
            "fontcolor": "#2D3436",
            "color": "invis"
        }

        self.edge_attrs = {
            "penwidth": "2",
            "margin": "1",
            "minlen": "2.0",
            "fontname": "Calibri"
        }

        self.colors = get_color_pallet(hue)

        if graph_attr_overrides is not None:
            self.graph_attrs.update(graph_attr_overrides)

        if cluster_attr_overrides is not None:
            self.cluster_attrs.update(cluster_attr_overrides)

        if node_attr_overrides is not None:
            self.node_attrs.update(node_attr_overrides)

        if edge_attr_overrides is not None:
            self.edge_attrs.update(edge_attr_overrides)

        if color_overrides:
            self.colors = color_overrides

class DarkMode(_Theme):

    def __init__(self, graph_attr_overrides={}, cluster_attr_overrides={}, node_attr_overrides={}, edge_attr_overrides={}, color_overrides=[]):

        self.graph_attrs = {
            "bgcolor": "#17202A",
            "compound": "true", 
            "pad": "1.0",
            "splines": "ortho",
            "nodesep": "1.0",
            "ranksep": "1.0",
            "fontname": "Sans-Serif",
            "fontsize": "24",
            "fontcolor": "#EEEEEE",
            "style": "rounded",
            "rankdir": "LR",
            "labeljust": "l",
            "labelloc": 't',
        }

        self.cluster_attrs = {
            "shape": "box",
            "style": "rounded,dotted",
            "labeljust": "l",
            "pencolor": "#AEB6BE",
            "fontname": "Sans-Serif",
            "fontsize": "12",
            "fontcolor": "#EEEEEE",
            "margin": "30"
        }

        self.node_attrs = {
            "shape": "invis",
            "style": "rounded,filled",
            "fixedsize": "true",
            "width": "1.0",
            "height": "1.8",
            "labelloc": "b",
            "imagescale": "true",
            "fontname": "Sans-Serif",
            "fontsize": "13",
            "fontcolor": "#EEEEEE",
            "color": "invis"
        }

        self.edge_attrs = {
            "penwidth": "2",
            "margin": "1",
            "minlen": "2.0",
            "color": "#EEEEEE"
        }

        self.colors = ["#1C2833", "#212F3D", "#273746", "#2C3E50", "#566573"]

        if graph_attr_overrides is not None:
            self.graph_attrs.update(graph_attr_overrides)

        if cluster_attr_overrides is not None:
            self.cluster_attrs.update(cluster_attr_overrides)

        if node_attr_overrides is not None:
            self.node_attrs.update(node_attr_overrides)

        if edge_attr_overrides is not None:
            self.edge_attrs.update(edge_attr_overrides)

        if color_overrides:
            self.colors = color_overrides