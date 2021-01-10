# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Saas

class _Cdn(_Saas):
	_service_type = "cdn"
	_icon_dir = "icons/saas/cdn"

class Akamai(_Cdn):
	_icon = "akamai.png"
	_default_label = "Akamai"

class Cloudflare(_Cdn):
	_icon = "cloudflare.png"
	_default_label = "Cloudflare"

