color_schemes = ["x11","svg","accent3","accent4","accent5","accent6","accent7","accent8","blues3","blues4","blues5","blues6","blues7","blues8","blues9","brbg10","brbg11","brbg3","brbg4","brbg5","brbg6","brbg7","brbg8","brbg9","bugn3","bugn4","bugn5","bugn6","bugn7","bugn8","bugn9","bupu3","bupu4","bupu5","bupu6","bupu7","bupu8","bupu9","dark23","dark24","dark25","dark26","dark27","dark28","gnbu3","gnbu4","gnbu5","gnbu6","gnbu7","gnbu8","gnbu9","greens3","greens4","greens5","greens6","greens7","greens8","greens9","greys3","greys4","greys5","greys6","greys7","greys8","greys9","oranges3","oranges4","oranges5","oranges6","oranges7","oranges8","oranges9","orrd3","orrd4","orrd5","orrd6","orrd7","orrd8","orrd9","paired10","paired11","paired12","paired3","paired4","paired5","paired6","paired7","paired8","paired9","pastel13","pastel14","pastel15","pastel16","pastel17","pastel18","pastel19","pastel23","pastel24","pastel25","pastel26","pastel27","pastel28","piyg10","piyg11","piyg3","piyg4","piyg5","piyg6","piyg7","piyg8","piyg9","prgn10","prgn11","prgn3","prgn4","prgn5","prgn6","prgn7","prgn8","prgn9","pubu3","pubu4","pubu5","pubu6","pubu7","pubu8","pubu9","pubugn3","pubugn4","pubugn5","pubugn6","pubugn7","pubugn8","pubugn9","puor10","puor11","puor3","puor4","puor5","puor6","puor7","puor8","puor9","purd3","purd4","purd5","purd6","purd7","purd8","purd9","purples3","purples4","purples5","purples6","purples7","purples8","purples9","rdbu10","rdbu11","rdbu3","rdbu4","rdbu5","rdbu6","rdbu7","rdbu8","rdbu9","rdgy10","rdgy11","rdgy3","rdgy4","rdgy5","rdgy6","rdgy7","rdgy8","rdgy9","rdpu3","rdpu4","rdpu5","rdpu6","rdpu7","rdpu8","rdpu9","rdylbu10","rdylbu11","rdylbu3","rdylbu4","rdylbu5","rdylbu6","rdylbu7","rdylbu8","rdylbu9","rdylgn10","rdylgn11","rdylgn3","rdylgn4","rdylgn5","rdylgn6","rdylgn7","rdylgn8","rdylgn9","reds3","reds4","reds5","reds6","reds7","reds8","reds9","set13","set14","set15","set16","set17","set18","set19","set23","set24","set25","set26","set27","set28","set310","set311","set312","set33","set34","set35","set36","set37","set38","set39","spectral10","spectral11","spectral3","spectral4","spectral5","spectral6","spectral7","spectral8","spectral9","ylgn3","ylgn4","ylgn5","ylgn6","ylgn7","ylgn8","ylgn9","ylgnbu3","ylgnbu4","ylgnbu5","ylgnbu6","ylgnbu7","ylgnbu8","ylgnbu9","ylorbr3","ylorbr4","ylorbr5","ylorbr6","ylorbr7","ylorbr8","ylorbr9","ylorrd3","ylorrd4","ylorrd5","ylorrd6","ylorrd7","ylorrd8","ylorrd9"]
x11_colors = [
    
]
class _Settings():

    # String Checks
    _string_field_checks = {
        "bgcolor": None,
        "dir": ["forward", "back", "both", "none"],
        "charset": ["utf-8", "iso-8859-1"],
        "colorscheme": None,
        "clusterrank": ["local", "global", "none"],
        "comment": None,
        "fontcolor": None,
        "fontname": None,
        "fontpath": None,
        "imagepath": None,
        "label": None,
        "labeljust": ["c", "r", "l"],
        "labelloc": ["t", "c", "b"],
        "layout": ["circo", "dot", "fdp", "neato", "patchwork", "twopi"],
        "ordering": ["in", "out"],
        "outputorder": ["breadthfirst", "nodesfirst", "edgesfirst"],
        "pagedir": ["bl", "br", "tl", "tr", "rb", "rt", "lb", "lt"],
        "rankdir": ["tb", "lr", "bt", "rl"],
        "ratio": ["fill", "compress", "expand", "auto"],
        "splines": ["true", "false", "none", "line", "polyline", "ortho", "curved", "spline"],
        "style": ["dashed", "dotted", "solid", "invis", "bold", "tapered", "filled", "striped", "wedged", "diagonals", "rounded", "radial"],
        "viewport": None,
    }

    # Boolean Checks
    # _boolean_field_checks = ["compound", "concentrate", "forcelabels", "landscape", "newrank", "nojustify", "pack", "remincross", ]

    # Float Checks
    _float_field_checks = {
        "fontsize": {"min": 1.0, "max": None},
        "margin": {"min": 0.0, "max": None},
        "mclimit": {"min": 1.0, "max": None},
        "nodesep": {"min": 0.02, "max": None},
        "orientation": {"min":0.0, "max": 360.0},
        "pad": {"min": 0.0, "max": None},
        "quantum": {"min": 0.0, "max": None},
        "ranksep": {"min": 0.02, "max": None},
        "size": {"min": 0.0, "max": None},
    }

    # Integer Checks
    _integer_field_checks = {
        "gradientangle": {"min": 0, "max": None},
        "rotate": {"min": 0, "max": 360},
        "searchsize": {"min": 0, "max": None},
        "showboxes": {"min": 0, "max": 2},
        "sortv": {"min": 0, "max": None},
    }


    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, item):
        return self.__dict__[item]

    def __repr__(self):
        return str(self.__dict__)

    def __iter__(self):
        return iter(self.__dict__.items())

    def check_string_settings(self, setting: str, valid_settings: list) -> bool:
        return setting in valid_settings


class GraphSettings(_Settings):
    
    def __init__(
        self,
        bgcolor = "white",
        center = False,
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
        margin = 0.0,
        mclimit = 1.0,
        newrank = False,
        nodesep = 0.25,
        nojustify = False,
        # "nslimit = "",
        # "nslimit1 = "",
        ordering = "",
        orientation = 0.0,
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

        # Check dir settings
        for field, checks in self._field_checks.items():
            value = dict(self)[field]
            if not isinstance(value, str):
                raise TypeError(f"The {field} attribute expects a string.")
            if not self.check_string_settings(value, checks):
                raise ValueError(f"The {field} attribute is set to a value of {value} but expects {', '.join(checks)}.")

        # Ensure that all values for attributes are strings
        for k, v in self.__dict__.items():
            if not isinstance(v, str):
                self.__dict__[k] = str(v).lower()