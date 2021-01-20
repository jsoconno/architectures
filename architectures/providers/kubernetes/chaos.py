# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Kubernetes

class _Chaos(_Kubernetes):
    _service_type = "chaos"
    _icon_dir = "icons/kubernetes/chaos"

class LitmusChaos(_Chaos):
    _icon = "litmus-chaos.png"
    _default_label = "Litmus Chaos"

class ChaosMesh(_Chaos):
    _icon = "chaos-mesh.png"
    _default_label = "Chaos Mesh"