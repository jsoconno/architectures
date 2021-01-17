# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _General

class _Virtualization(_General):
	_service_type = "virtualization"
	_icon_dir = "icons/general/virtualization"

class Virtualbox(_Virtualization):
	_icon = "virtualbox.png"
	_default_label = "Virtualbox"

class Vmware(_Virtualization):
	_icon = "vmware.png"
	_default_label = "Vmware"

class Xen(_Virtualization):
	_icon = "xen.png"
	_default_label = "Xen"

