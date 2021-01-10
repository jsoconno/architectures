# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Openstack

class _Monitoring(_Openstack):
	_service_type = "monitoring"
	_icon_dir = "icons/openstack/monitoring"

class Telemetry(_Monitoring):
	_icon = "telemetry.png"
	_default_label = "Telemetry"

class Monasca(_Monitoring):
	_icon = "monasca.png"
	_default_label = "Monasca"

