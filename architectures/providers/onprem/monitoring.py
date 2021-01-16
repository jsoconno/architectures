# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Onprem

class _Monitoring(_Onprem):
	_service_type = "monitoring"
	_icon_dir = "icons/onprem/monitoring"

class Cortex(_Monitoring):
	_icon = "cortex.png"
	_default_label = "Cortex"

class Datadog(_Monitoring):
	_icon = "datadog.png"
	_default_label = "Datadog"

class Grafana(_Monitoring):
	_icon = "grafana.png"
	_default_label = "Grafana"

class PrometheusOperator(_Monitoring):
	_icon = "prometheus-operator.png"
	_default_label = "Prometheus Operator"

class Prometheus(_Monitoring):
	_icon = "prometheus.png"
	_default_label = "Prometheus"

class Sentry(_Monitoring):
	_icon = "sentry.png"
	_default_label = "Sentry"

class Splunk(_Monitoring):
	_icon = "splunk.png"
	_default_label = "Splunk"

class Thanos(_Monitoring):
	_icon = "thanos.png"
	_default_label = "Thanos"

class Zabbix(_Monitoring):
	_icon = "zabbix.png"
	_default_label = "Zabbix"

