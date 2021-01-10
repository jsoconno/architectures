# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _K8S

class _Chaos(_K8S):
	_service_type = "chaos"
	_icon_dir = "icons/k8s/chaos"

class LitmusChaos(_Chaos):
	_icon = "litmus-chaos.png"
	_default_label = "Litmus Chaos"

class ChaosMesh(_Chaos):
	_icon = "chaos-mesh.png"
	_default_label = "Chaos Mesh"

