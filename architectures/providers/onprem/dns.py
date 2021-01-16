# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Onprem

class _Dns(_Onprem):
	_service_type = "dns"
	_icon_dir = "icons/onprem/dns"

class Coredns(_Dns):
	_icon = "coredns.png"
	_default_label = "Coredns"

class Powerdns(_Dns):
	_icon = "powerdns.png"
	_default_label = "Powerdns"

