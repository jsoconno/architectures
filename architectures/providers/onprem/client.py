# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Onprem

class _Client(_Onprem):
	_service_type = "client"
	_icon_dir = "icons/onprem/client"

class User(_Client):
	_icon = "user.png"
	_default_label = "User"

class Users(_Client):
	_icon = "users.png"
	_default_label = "Users"

class Client(_Client):
	_icon = "client.png"
	_default_label = "Client"

