# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Openstack

class _Optimization(_Openstack):
	_service_type = "optimization"
	_icon_dir = "icons/openstack/optimization"

class Watcher(_Optimization):
	_icon = "watcher.png"
	_default_label = "Watcher"

class Vitrage(_Optimization):
	_icon = "vitrage.png"
	_default_label = "Vitrage"

class Rally(_Optimization):
	_icon = "rally.png"
	_default_label = "Rally"

class Congress(_Optimization):
	_icon = "congress.png"
	_default_label = "Congress"

