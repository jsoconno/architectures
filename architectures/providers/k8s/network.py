# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _K8S

class _Network(_K8S):
	_service_type = "network"
	_icon_dir = "icons/k8s/network"

class Ep(_Network):
	_icon = "ep.png"
	_default_label = "Ep"

class Ing(_Network):
	_icon = "ing.png"
	_default_label = "Ing"

class Netpol(_Network):
	_icon = "netpol.png"
	_default_label = "Netpol"

class Svc(_Network):
	_icon = "svc.png"
	_default_label = "Svc"

