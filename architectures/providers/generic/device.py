# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Generic

class _Device(_Generic):
	_service_type = "device"
	_icon_dir = "icons/generic/device"

class Tablet(_Device):
	_icon = "tablet.png"
	_default_label = "Tablet"

class Mobile(_Device):
	_icon = "mobile.png"
	_default_label = "Mobile"

