# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Outscale

class _Security(_Outscale):
	_service_type = "security"
	_icon_dir = "icons/outscale/security"

class Firewall(_Security):
	_icon = "firewall.png"
	_default_label = "Firewall"

class IdentityAndAccessManagement(_Security):
	_icon = "identity-and-access-management.png"
	_default_label = "Identity And Access Management"

