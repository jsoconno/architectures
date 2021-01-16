# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Openstack

class _Applicationlifecycle(_Openstack):
	_service_type = "applicationlifecycle"
	_icon_dir = "icons/openstack/applicationlifecycle"

class Freezer(_Applicationlifecycle):
	_icon = "freezer.png"
	_default_label = "Freezer"

class Masakari(_Applicationlifecycle):
	_icon = "masakari.png"
	_default_label = "Masakari"

class Murano(_Applicationlifecycle):
	_icon = "murano.png"
	_default_label = "Murano"

class Solum(_Applicationlifecycle):
	_icon = "solum.png"
	_default_label = "Solum"

