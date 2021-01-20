# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Kubernetes

class _Podconfig(_Kubernetes):
    _service_type = "podconfig"
    _icon_dir = "icons/kubernetes/podconfig"

class Cm(_Podconfig):
    _icon = "cm.png"
    _default_label = "Cm"

class Secret(_Podconfig):
    _icon = "secret.png"
    _default_label = "Secret"