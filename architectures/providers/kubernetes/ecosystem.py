# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Kubernetes

class _Ecosystem(_Kubernetes):
    _service_type = "ecosystem"
    _icon_dir = "icons/kubernetes/ecosystem"

class Kustomize(_Ecosystem):
    _icon = "kustomize.png"
    _default_label = "Kustomize"

class Helm(_Ecosystem):
    _icon = "helm.png"
    _default_label = "Helm"

class Krew(_Ecosystem):
    _icon = "krew.png"
    _default_label = "Krew"

class ExternalDns(_Ecosystem):
    _icon = "external-dns.png"
    _default_label = "External Dns"