# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Openstack

class _Orchestration(_Openstack):
	_service_type = "orchestration"
	_icon_dir = "icons/openstack/orchestration"

class Mistral(_Orchestration):
	_icon = "mistral.png"
	_default_label = "Mistral"

class Blazar(_Orchestration):
	_icon = "blazar.png"
	_default_label = "Blazar"

class Zaqar(_Orchestration):
	_icon = "zaqar.png"
	_default_label = "Zaqar"

class Heat(_Orchestration):
	_icon = "heat.png"
	_default_label = "Heat"

class Senlin(_Orchestration):
	_icon = "senlin.png"
	_default_label = "Senlin"

