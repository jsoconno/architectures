# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Onprem

class _Tracing(_Onprem):
	_service_type = "tracing"
	_icon_dir = "icons/onprem/tracing"

class Jaeger(_Tracing):
	_icon = "jaeger.png"
	_default_label = "Jaeger"

