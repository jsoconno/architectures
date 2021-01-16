# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Onprem

class _Logging(_Onprem):
	_service_type = "logging"
	_icon_dir = "icons/onprem/logging"

class Fluentbit(_Logging):
	_icon = "fluentbit.png"
	_default_label = "Fluentbit"

class Graylog(_Logging):
	_icon = "graylog.png"
	_default_label = "Graylog"

class Loki(_Logging):
	_icon = "loki.png"
	_default_label = "Loki"

class Rsyslog(_Logging):
	_icon = "rsyslog.png"
	_default_label = "Rsyslog"

class SyslogNg(_Logging):
	_icon = "syslog-ng.png"
	_default_label = "Syslog Ng"

