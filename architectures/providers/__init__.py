'''
This file will define a class called Azure that is used by other .py files in this directory
'''

from architectures.core import Node

class _Aws(Node):
    _provider = "aws"
    _icon_dir = "icons/aws"

class _Azure(Node):
    _provider = "azure"
    _icon_dir = "icons/azure"

class _Gcp(Node):
    _provider = "gcp"
    _icon_dir = "icons/gcp"

class _General(Node):
    _provider = "general"
    _icon_dir = "icons/general"

class _Kubernetes(Node):
    _provider = "kubernetes"
    _icon_dir = "icons/kubernetes"
