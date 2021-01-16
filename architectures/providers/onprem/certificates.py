# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Onprem

class _Certificates(_Onprem):
	_service_type = "certificates"
	_icon_dir = "icons/onprem/certificates"

class CertManager(_Certificates):
	_icon = "cert-manager.png"
	_default_label = "Cert Manager"

class LetsEncrypt(_Certificates):
	_icon = "lets-encrypt.png"
	_default_label = "Lets Encrypt"

