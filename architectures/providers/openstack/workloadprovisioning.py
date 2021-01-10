# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Openstack

class _Workloadprovisioning(_Openstack):
	_service_type = "workloadprovisioning"
	_icon_dir = "icons/openstack/workloadprovisioning"

class Magnum(_Workloadprovisioning):
	_icon = "magnum.png"
	_default_label = "Magnum"

class Trove(_Workloadprovisioning):
	_icon = "trove.png"
	_default_label = "Trove"

class Sahara(_Workloadprovisioning):
	_icon = "sahara.png"
	_default_label = "Sahara"

