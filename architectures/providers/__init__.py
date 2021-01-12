'''
This file will define a class called Azure that is used by other .py files in this directory
'''

from architectures.core import Node

class _Azure(Node):
    _provider = "azure"
    _icon_dir = "icons/azure"

    fontcolor = "#ffffff"

class _Aws(Node):
    _provider = "aws"
    _icon_dir = "icons/aws"