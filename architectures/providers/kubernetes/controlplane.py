# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Kubernetes

class _Controlplane(_Kubernetes):
    _service_type = "controlplane"
    _icon_dir = "icons/kubernetes/controlplane"

class Sched(_Controlplane):
    _icon = "sched.png"
    _default_label = "Sched"

class Kubelet(_Controlplane):
    _icon = "kubelet.png"
    _default_label = "Kubelet"

class CM(_Controlplane):
    _icon = "c-m.png"
    _default_label = "C M"

class CCM(_Controlplane):
    _icon = "c-c-m.png"
    _default_label = "C C M"

class Api(_Controlplane):
    _icon = "api.png"
    _default_label = "Api"

class KProxy(_Controlplane):
    _icon = "k-proxy.png"
    _default_label = "K Proxy"