# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Onprem

class _Aggregator(_Onprem):
	_service_type = "aggregator"
	_icon_dir = "icons/onprem/aggregator"

class Fluentd(_Aggregator):
	_icon = "fluentd.png"
	_default_label = "Fluentd"

class Vector(_Aggregator):
	_icon = "vector.png"
	_default_label = "Vector"

