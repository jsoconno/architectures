class _Settings():

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, item):
        return self.__dict__[item]

    def __repr__(self):
        return str(self.__dict__)

    def __iter__(self):
        return iter(self.__dict__.items())
class GraphSettings(_Settings):
    
    def __init__(
        self,
        bgcolor = "white",
        center = "false",
        charset = "utf-8",
        clusterrank = "local",
        colorscheme = "",
        comment = "",
        compound = "true",
        concentrate = "false",
        fontcolor = "black",
        fontname = "times-roman",
        fontpath = "system-dependent",
        fontsize = "14",
        forcelabels = "true",
        gradientangle = "",
        imagepath = "",
        label = "",
        labeljust = "c",
        labelloc = "b",
        landscape = "false",
        layout = "dot",
        margin = "0",
        mclimit = "1",
        newrank = "false",
        nodesep = "0.25",
        nojustify = "false",
        # "nslimit = "",
        # "nslimit1 = "",
        ordering = "",
        orientation = "0",
        outputorder = "breadthfirst",
        pack = "false",
        # "packmode = "node",
        pad = "0.0555",
        pagedir = "bl",
        quantum = "0.0",
        rankdir = "TB",
        ranksep = "0.5",
        ratio = "auto",
        remincross = "true",
        rotate = "0",
        searchsize = "30",
        showboxes = "0",
        size = "",
        sortv = "0",
        splines = "line",
        style = "",
        viewport = "",
        **kwargs
    ):
        self.bgcolor = bgcolor
        self.center = center
        self.charset = charset
        self.clusterrank = clusterrank
        self.colorscheme = colorscheme
        self.comment = comment
        self.compound = compound
        self.concentrate = concentrate
        self.fontcolor = fontcolor
        self.fontname = fontname
        self.fontpath = fontpath
        self.fontsize = fontsize
        self.forcelabels = forcelabels
        self.gradientangle = gradientangle
        self.imagepath = imagepath
        self.label = label
        self.labeljust = labeljust
        self.labelloc = labelloc
        self.landscape = landscape
        self.layout = layout
        self.margin = margin
        self.mclimit = mclimit
        self.newrank = newrank
        self.nodesep = nodesep
        self.nojustify = nojustify
        # "nslimit = ""
        # "nslimit1 = ""
        self.ordering = ordering
        self.orientation = orientation
        self.outputorder = outputorder
        self.pack = pack
        # "packmode = "node"
        self.pad = pad
        self.pagedir = pagedir
        self.quantum = quantum
        self.rankdir = rankdir
        self.ranksep = ranksep
        self.ratio = ratio
        self.remincross = remincross
        self.rotate = rotate
        self.searchsize = searchsize
        self.showboxes = showboxes
        self.size = size
        self.sortv = sortv
        self.splines = splines
        self.style = style
        self.viewport = viewport

        self.__dict__.update(kwargs)


class ClusterSettings(_Settings):
    def __init__(
        self,
        bgcolor = "transparent",
        color = "black",
        colorscheme = "",
        fillcolor = "black",
        fontcolor = "black",
        fontname = "times-roman",
        fontsize = "14",
        gradientangle = "",
        label = "",
        labeljust = "c",
        labelloc = "t",
        layer = "",
        margin = "8",
        nojustify = "false",
        pencolor = "black",
        penwidth = "1",
        peripheries = "1",
        sortv = "0",
        style = "",
        **kwargs
    ):
        self.bgcolor = bgcolor
        self.color = color
        self.colorscheme = colorscheme
        self.fillcolor = fillcolor
        self.fontcolor = fontcolor
        self.fontname = fontname
        self.fontsize = fontsize
        self.gradientangle = gradientangle
        self.label = label
        self.labeljust = labeljust
        self.labelloc = labelloc
        self.layer = layer
        self.margin = margin
        self.nojustify = nojustify
        self.pencolor = pencolor
        self.penwidth = penwidth
        self.peripheries = peripheries
        self.sortv = sortv
        self.style = style

        self.__dict__.update(kwargs)


class NodeSettings(_Settings):
    def __init__(
        self,
        color = "black",
        colorscheme = "",
        comment = "",
        distortion = "0",
        fillcolor = "lightgrey",
        fixedsize = "false",
        fontcolor = "black",
        fontname = "times-roman",
        fontsize = "14",
        gradientangle = "",
        group = "",
        height = "0.5",
        # image = "",
        imagepos = "tc",
        imagescale = "false",
        # label = "",
        labelloc = "c",
        layer = "",
        margin = "0.11,0.055",
        nojustify = "false",
        ordering = "",
        orientation = "0",
        penwidth = "1",
        peripheries = "1",
        pos = "",
        regular = "false",
        shape = "ellipse",
        shapefile = "",
        showboxes = "0",
        sides = "4",
        skew = "0",
        sortv = "0",
        style = "",
        width = "0.75",
        # xlabel = "",
        **kwargs
    ):
        self.color = color
        self.colorscheme = colorscheme
        self.comment = comment
        self.distortion = distortion
        self.fillcolor = fillcolor
        self.fixedsize = fixedsize
        self.fontcolor = fontcolor
        self.fontname = fontname
        self.fontsize = fontsize
        self.gradientangle = gradientangle
        self.group = group
        self.height = height
        # self.image = image
        self.imagepos = imagepos
        self.imagescale = imagescale
        # self.label = label
        self.labelloc = labelloc
        self.layer = layer
        self.margin = margin
        self.nojustify = nojustify
        self.ordering = ordering
        self.orientation = orientation
        self.penwidth = penwidth
        self.peripheries = peripheries
        self.pos = pos
        self.regular = regular
        self.shape = shape
        self.shapefile = shapefile
        self.showboxes = showboxes
        self.sides = sides
        self.skew = skew
        self.sortv = sortv
        self.style = style
        self.width = width
        # self.xlabel = xlabel

        self.__dict__.update(kwargs)


class EdgeSettings(_Settings):
    def __init__(
        self,
        arrowhead = "normal",
        arrowsize = "1",
        arrowtail = "normal",
        color = "black",
        colorscheme = "",
        comment = "",
        constraint = "true",
        decorate = "false",
        dir = "forward",
        fillcolor = "black",
        fontcolor = "black",
        fontname = "times-roman",
        fontsize = "14",
        headclip = "true",
        headlabel = "",
        headport = "center",
        label = "",
        labelangle = "-25",
        labeldistance = "1",
        labelfloat = "false",
        labelfontcolor = "black",
        labelfontname = "times-roman",
        labelfontsize = "14",
        layer = "",
        lhead = "",
        ltail = "",
        minlen = "1",
        nojustify = "false",
        penwidth = "1",
        pos = "",
        samehead = "",
        sametail = "",
        showboxes = "0",
        style = "",
        tailclip = "true",
        taillabel = "",
        tailport = "center",
        weight = "1",
        xlabel = "",
        **kwargs
    ):
        self.arrowhead = arrowhead
        self.arrowsize =arrowsize
        self.arrowtail = arrowtail
        self.color = color
        self.colorscheme = colorscheme
        self.comment = comment
        self.constraint = constraint
        self.decorate = decorate
        self.dir = dir
        self.fillcolor = fillcolor
        self.fontcolor = fontcolor
        self.fontname = fontname
        self.fontsize = fontsize
        self.headclip = headclip
        self.headlabel = headlabel
        self.headport = headport
        self.label = label
        self.labelangle = labelangle
        self.labeldistance = labeldistance
        self.labelfloat = labelfloat
        self.labelfontcolor = labelfontcolor
        self.labelfontname = labelfontname
        self.labelfontsize = labelfontsize
        self.layer = layer
        self.lhead = lhead
        self.ltail = ltail
        self.minlen = minlen
        self.nojustify = nojustify
        self.penwidth = penwidth
        self.pos = pos
        self.samehead = samehead
        self.sametail = sametail
        self.showboxes = showboxes
        self.style = style
        self.tailclip = tailclip
        self.taillabel = taillabel
        self.tailport = tailport
        self.weight = weight
        self.xlabel = xlabel

        self.__dict__.update(kwargs)


class Default():

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


class LightMode():

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
            compound = "true", 
            pad = "1.0",
            splines = "ortho",
            nodesep = "1.0",
            ranksep = "1.0",
            fontname = "Calibri",
            fontsize = "24",
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
            fontname = "Calibri",
            fontsize = "12",
            margin = "30"
        ))
        self.node_attrs = dict(NodeSettings(
            shape = "invis",
            style = "rounded,filled",
            fixedsize = "true",
            width = "1.0",
            height = "1.0",
            labelloc = "b",
            imagescale = "true",
            fontname = "Calibri",
            fontsize = "13",
            fontcolor = "#2D3436",
            color = "invis",
            fillcolor = "invis"
        ))
        self.edge_attrs = dict(EdgeSettings(
            penwidth = "2",
            minlen = "2.0",
            fontname = "Calibri"
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

    def get_delta_dict(self, first_dict, second_dict):
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

class DarkMode():

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
            compound = "true", 
            pad = "1.0",
            splines = "ortho",
            nodesep = "1.0",
            ranksep = "1.0",
            fontname = "Sans-Serif",
            fontsize = "24",
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
            fontname = "Sans-Serif",
            fontsize = "12",
            fontcolor = "#EEEEEE",
            margin = "30"
        ))
        self.node_attrs = dict(NodeSettings(
            shape = "invis",
            style = "rounded,filled",
            fixedsize = "true",
            width = "1.0",
            height = "1.0",
            labelloc = "b",
            imagescale = "true",
            fontname = "Sans-Serif",
            fontsize = "13",
            fontcolor = "#EEEEEE",
            color = "invis",
            fillcolor = "invis"
        ))
        self.edge_attrs = dict(EdgeSettings(
            penwidth = "2",
            minlen = "2.0",
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

    def get_delta_dict(self, first_dict, second_dict):
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