# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Saas

class _Alerting(_Saas):
	_service_type = "alerting"
	_icon_dir = "icons/saas/alerting"

class Opsgenie(_Alerting):
	_icon = "opsgenie.png"
	_default_label = "Opsgenie"

class Pushover(_Alerting):
	_icon = "pushover.png"
	_default_label = "Pushover"

