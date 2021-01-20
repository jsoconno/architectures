# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Kubernetes

class _Storage(_Kubernetes):
    _service_type = "storage"
    _icon_dir = "icons/kubernetes/storage"

class Vol(_Storage):
    _icon = "vol.png"
    _default_label = "Vol"

class Sc(_Storage):
    _icon = "sc.png"
    _default_label = "Sc"

class Pvc(_Storage):
    _icon = "pvc.png"
    _default_label = "Pvc"

class Pv(_Storage):
    _icon = "pv.png"
    _default_label = "Pv"