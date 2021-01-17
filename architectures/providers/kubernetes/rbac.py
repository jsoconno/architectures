# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Kubernetes

class _Rbac(_Kubernetes):
	_service_type = "rbac"
	_icon_dir = "icons/kubernetes/rbac"

class CRole(_Rbac):
	_icon = "c-role.png"
	_default_label = "C Role"

class Crb(_Rbac):
	_icon = "crb.png"
	_default_label = "Crb"

class Group(_Rbac):
	_icon = "group.png"
	_default_label = "Group"

class Rb(_Rbac):
	_icon = "rb.png"
	_default_label = "Rb"

class Role(_Rbac):
	_icon = "role.png"
	_default_label = "Role"

class Sa(_Rbac):
	_icon = "sa.png"
	_default_label = "Sa"

class User(_Rbac):
	_icon = "user.png"
	_default_label = "User"

