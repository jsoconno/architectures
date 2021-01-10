# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Onprem

class _Workflow(_Onprem):
	_service_type = "workflow"
	_icon_dir = "icons/onprem/workflow"

class Kubeflow(_Workflow):
	_icon = "kubeflow.png"
	_default_label = "Kubeflow"

class Airflow(_Workflow):
	_icon = "airflow.png"
	_default_label = "Airflow"

class Nifi(_Workflow):
	_icon = "nifi.png"
	_default_label = "Nifi"

class Digdag(_Workflow):
	_icon = "digdag.png"
	_default_label = "Digdag"

