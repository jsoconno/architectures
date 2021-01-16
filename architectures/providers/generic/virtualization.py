# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Generic

class _Virtualization(_Generic):
	_service_type = "virtualization"
	_icon_dir = "icons/generic/virtualization"

class Virtualbox(_Virtualization):
	_icon = "virtualbox.png"
	_default_label = "Virtualbox"

class Vmware(_Virtualization):
	_icon = "vmware.png"
	_default_label = "Vmware"

class Xen(_Virtualization):
	_icon = "xen.png"
	_default_label = "Xen"

