# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _K8S

class _Storage(_K8S):
	_service_type = "storage"
	_icon_dir = "icons/k8s/storage"

class Pv(_Storage):
	_icon = "pv.png"
	_default_label = "Pv"

class Pvc(_Storage):
	_icon = "pvc.png"
	_default_label = "Pvc"

class Sc(_Storage):
	_icon = "sc.png"
	_default_label = "Sc"

class Vol(_Storage):
	_icon = "vol.png"
	_default_label = "Vol"

