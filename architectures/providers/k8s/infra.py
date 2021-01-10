# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _K8S

class _Infra(_K8S):
	_service_type = "infra"
	_icon_dir = "icons/k8s/infra"

class Etcd(_Infra):
	_icon = "etcd.png"
	_default_label = "Etcd"

class Master(_Infra):
	_icon = "master.png"
	_default_label = "Master"

class Node(_Infra):
	_icon = "node.png"
	_default_label = "Node"

