# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Onprem

class _Cd(_Onprem):
	_service_type = "cd"
	_icon_dir = "icons/onprem/cd"

class Spinnaker(_Cd):
	_icon = "spinnaker.png"
	_default_label = "Spinnaker"

class TektonCli(_Cd):
	_icon = "tekton-cli.png"
	_default_label = "Tekton Cli"

class Tekton(_Cd):
	_icon = "tekton.png"
	_default_label = "Tekton"

