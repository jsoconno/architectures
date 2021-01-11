# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _K8S

class _Others(_K8S):
	_service_type = "others"
	_icon_dir = "icons/k8s/others"

class Psp(_Others):
	_icon = "psp.png"
	_default_label = "Psp"

class Crd(_Others):
	_icon = "crd.png"
	_default_label = "Crd"

