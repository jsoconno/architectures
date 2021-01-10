# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Saas

class _Logging(_Saas):
	_service_type = "logging"
	_icon_dir = "icons/saas/logging"

class Datadog(_Logging):
	_icon = "datadog.png"
	_default_label = "Datadog"

class Papertrail(_Logging):
	_icon = "papertrail.png"
	_default_label = "Papertrail"

