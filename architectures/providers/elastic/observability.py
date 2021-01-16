# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Elastic

class _Observability(_Elastic):
	_service_type = "observability"
	_icon_dir = "icons/elastic/observability"

class Apm(_Observability):
	_icon = "apm.png"
	_default_label = "Apm"

class Logs(_Observability):
	_icon = "logs.png"
	_default_label = "Logs"

class Metrics(_Observability):
	_icon = "metrics.png"
	_default_label = "Metrics"

class Observability(_Observability):
	_icon = "observability.png"
	_default_label = "Observability"

class Uptime(_Observability):
	_icon = "uptime.png"
	_default_label = "Uptime"

