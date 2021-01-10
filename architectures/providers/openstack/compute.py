# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Openstack

class _Compute(_Openstack):
	_service_type = "compute"
	_icon_dir = "icons/openstack/compute"

class Zun(_Compute):
	_icon = "zun.png"
	_default_label = "Zun"

class Qinling(_Compute):
	_icon = "qinling.png"
	_default_label = "Qinling"

class Nova(_Compute):
	_icon = "nova.png"
	_default_label = "Nova"

