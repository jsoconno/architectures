# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Generic

class _Network(_Generic):
	_service_type = "network"
	_icon_dir = "icons/generic/network"

class Vpn(_Network):
	_icon = "vpn.png"
	_default_label = "Vpn"

class Firewall(_Network):
	_icon = "firewall.png"
	_default_label = "Firewall"

class Switch(_Network):
	_icon = "switch.png"
	_default_label = "Switch"

class Router(_Network):
	_icon = "router.png"
	_default_label = "Router"

class Subnet(_Network):
	_icon = "subnet.png"
	_default_label = "Subnet"

