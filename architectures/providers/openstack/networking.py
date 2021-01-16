# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Openstack

class _Networking(_Openstack):
	_service_type = "networking"
	_icon_dir = "icons/openstack/networking"

class Designate(_Networking):
	_icon = "designate.png"
	_default_label = "Designate"

class Neutron(_Networking):
	_icon = "neutron.png"
	_default_label = "Neutron"

class Octavia(_Networking):
	_icon = "octavia.png"
	_default_label = "Octavia"

