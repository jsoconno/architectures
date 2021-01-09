# Do not modify this file directly.  It is auto-generated with Python.

from architectures.providers import _Azure

class _Security(_Azure):
	_service_type = "security"
	_icon_dir = "icons/azure/security"

class SecurityCenter(_Security):
	_icon = "security-center.png"
	_default_label = "Security Center"

class Sentinel(_Security):
	_icon = "sentinel.png"
	_default_label = "Sentinel"

class KeyVaults(_Security):
	_icon = "key-vaults.png"
	_default_label = "Key Vaults"

