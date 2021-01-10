# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Onprem

class _Auth(_Onprem):
	_service_type = "auth"
	_icon_dir = "icons/onprem/auth"

class Oauth2Proxy(_Auth):
	_icon = "oauth2-proxy.png"
	_default_label = "Oauth2 Proxy"

class Boundary(_Auth):
	_icon = "boundary.png"
	_default_label = "Boundary"

class BuzzfeedSso(_Auth):
	_icon = "buzzfeed-sso.png"
	_default_label = "Buzzfeed Sso"

