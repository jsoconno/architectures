# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Outscale

class _Compute(_Outscale):
	_service_type = "compute"
	_icon_dir = "icons/outscale/compute"

class Compute(_Compute):
	_icon = "compute.png"
	_default_label = "Compute"

class DirectConnect(_Compute):
	_icon = "direct-connect.png"
	_default_label = "Direct Connect"

