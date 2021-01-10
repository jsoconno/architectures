# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Elastic

class _Security(_Elastic):
	_service_type = "security"
	_icon_dir = "icons/elastic/security"

class Siem(_Security):
	_icon = "siem.png"
	_default_label = "Siem"

class Endpoint(_Security):
	_icon = "endpoint.png"
	_default_label = "Endpoint"

class Security(_Security):
	_icon = "security.png"
	_default_label = "Security"

