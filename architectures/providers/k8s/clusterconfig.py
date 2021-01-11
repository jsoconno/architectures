# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _K8S

class _Clusterconfig(_K8S):
	_service_type = "clusterconfig"
	_icon_dir = "icons/k8s/clusterconfig"

class Hpa(_Clusterconfig):
	_icon = "hpa.png"
	_default_label = "Hpa"

class Limits(_Clusterconfig):
	_icon = "limits.png"
	_default_label = "Limits"

class Quota(_Clusterconfig):
	_icon = "quota.png"
	_default_label = "Quota"

