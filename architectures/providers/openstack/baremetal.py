# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Openstack

class _Baremetal(_Openstack):
	_service_type = "baremetal"
	_icon_dir = "icons/openstack/baremetal"

class Cyborg(_Baremetal):
	_icon = "cyborg.png"
	_default_label = "Cyborg"

class Ironic(_Baremetal):
	_icon = "ironic.png"
	_default_label = "Ironic"

