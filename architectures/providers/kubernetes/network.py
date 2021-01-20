# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Kubernetes

class _Network(_Kubernetes):
    _service_type = "network"
    _icon_dir = "icons/kubernetes/network"

class Netpol(_Network):
    _icon = "netpol.png"
    _default_label = "Netpol"

class Ep(_Network):
    _icon = "ep.png"
    _default_label = "Ep"

class Ing(_Network):
    _icon = "ing.png"
    _default_label = "Ing"

class Svc(_Network):
    _icon = "svc.png"
    _default_label = "Svc"