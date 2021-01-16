# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Openstack

class _Sharedservices(_Openstack):
	_service_type = "sharedservices"
	_icon_dir = "icons/openstack/sharedservices"

class Barbican(_Sharedservices):
	_icon = "barbican.png"
	_default_label = "Barbican"

class Glance(_Sharedservices):
	_icon = "glance.png"
	_default_label = "Glance"

class Karbor(_Sharedservices):
	_icon = "karbor.png"
	_default_label = "Karbor"

class Keystone(_Sharedservices):
	_icon = "keystone.png"
	_default_label = "Keystone"

class Searchlight(_Sharedservices):
	_icon = "searchlight.png"
	_default_label = "Searchlight"

