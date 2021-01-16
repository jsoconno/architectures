# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Onprem

class _Compute(_Onprem):
	_service_type = "compute"
	_icon_dir = "icons/onprem/compute"

class Nomad(_Compute):
	_icon = "nomad.png"
	_default_label = "Nomad"

class Server(_Compute):
	_icon = "server.png"
	_default_label = "Server"

