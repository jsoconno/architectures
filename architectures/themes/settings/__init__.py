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
        compound = True,
        concentrate = False,
        fontcolor = "black",
        fontname = "times-roman",
        fontpath = "system-dependent",
        fontsize = 14,
        forcelabels = True,
        gradientangle = 0,
        imagepath = "",
        label = "",
        labeljust = "c",
        labelloc = "b",
        landscape = False,
        layout = "dot",
        margin = 0,
        mclimit = 1,
        newrank = False,
        nodesep = 0.25,
        nojustify = False,
        # "nslimit = "",
        # "nslimit1 = "",
        ordering = "",
        orientation = 0,
        outputorder = "breadthfirst",
        pack = False,
        # "packmode = "node",
        pad = 0.0555,
        pagedir = "bl",
        quantum = 0.0,
        rankdir = "TB",
        ranksep = 0.5,
        ratio = "auto",
        remincross = True,
        rotate = 0,
        searchsize = 30,
        showboxes = 0,
        size = 100.0,
        sortv = 0,
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

        # Add any additional keyword arguments
        self.__dict__.update(kwargs)

        # Ensure that all values for attributes are strings
        for k, v in self.__dict__.items():
            if not isinstance(v, str):
                self.__dict__[k] = str(v).lower().lower()


class ClusterSettings(_Settings):
    def __init__(
        self,
        bgcolor = "transparent",
        color = "black",
        colorscheme = "",
        fillcolor = "black",
        fontcolor = "black",
        fontname = "times-roman",
        fontsize = 14,
        gradientangle = 0,
        label = "",
        labeljust = "c",
        labelloc = "t",
        layer = "",
        margin = 8,
        nojustify = False,
        pencolor = "black",
        penwidth = 1,
        peripheries = 1,
        sortv = 0,
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

        # Add any additional keyword arguments
        self.__dict__.update(kwargs)

        # Ensure that all values for attributes are strings
        for k, v in self.__dict__.items():
            if not isinstance(v, str):
                self.__dict__[k] = str(v).lower()


class NodeSettings(_Settings):
    def __init__(
        self,
        color = "black",
        colorscheme = "",
        comment = "",
        distortion = 0,
        fillcolor = "lightgrey",
        fixedsize = False,
        fontcolor = "black",
        fontname = "times-roman",
        fontsize = 14,
        gradientangle = 0,
        group = "",
        height = 0.5,
        # image = "",
        imagepos = "tc",
        imagescale = False,
        # label = "",
        labelloc = "c",
        layer = "",
        margin = "0.11,0.055",
        nojustify = False,
        ordering = "",
        orientation = 0,
        penwidth = 1,
        peripheries = 1,
        pos = "",
        regular = False,
        shape = "ellipse",
        shapefile = "",
        showboxes = 0,
        sides = 4,
        skew = 0,
        sortv = 0,
        style = "",
        width = 0.75,
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

        # Add any additional keyword arguments
        self.__dict__.update(kwargs)

        # Ensure that all values for attributes are strings
        for k, v in self.__dict__.items():
            if not isinstance(v, str):
                self.__dict__[k] = str(v).lower()


class EdgeSettings(_Settings):
    def __init__(
        self,
        arrowhead = "normal",
        arrowsize = 1,
        arrowtail = "normal",
        color = "black",
        colorscheme = "",
        comment = "",
        constraint = True,
        decorate = False,
        dir = "forward",
        fillcolor = "black",
        fontcolor = "black",
        fontname = "times-roman",
        fontsize = 14,
        headclip = True,
        headlabel = "",
        headport = "center",
        label = "",
        labelangle = -25,
        labeldistance = 1,
        labelfloat = False,
        labelfontcolor = "black",
        labelfontname = "times-roman",
        labelfontsize = 14,
        layer = "",
        lhead = "",
        ltail = "",
        minlen = 1,
        nojustify = False,
        penwidth = 1,
        pos = "",
        samehead = "",
        sametail = "",
        showboxes = 0,
        style = "",
        tailclip = True,
        taillabel = "",
        tailport = "center",
        weight = 1,
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

        # Add any additional keyword arguments
        self.__dict__.update(kwargs)

        # Ensure that all values for attributes are strings
        for k, v in self.__dict__.items():
            if not isinstance(v, str):
                self.__dict__[k] = str(v).lower()