# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Openstack

class _Storage(_Openstack):
	_service_type = "storage"
	_icon_dir = "icons/openstack/storage"

class Cinder(_Storage):
	_icon = "cinder.png"
	_default_label = "Cinder"

class Manila(_Storage):
	_icon = "manila.png"
	_default_label = "Manila"

class Swift(_Storage):
	_icon = "swift.png"
	_default_label = "Swift"

