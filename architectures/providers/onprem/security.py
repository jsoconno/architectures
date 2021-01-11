# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Onprem

class _Security(_Onprem):
	_service_type = "security"
	_icon_dir = "icons/onprem/security"

class Vault(_Security):
	_icon = "vault.png"
	_default_label = "Vault"

class Trivy(_Security):
	_icon = "trivy.png"
	_default_label = "Trivy"

class Bitwarden(_Security):
	_icon = "bitwarden.png"
	_default_label = "Bitwarden"

