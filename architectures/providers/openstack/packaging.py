# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Openstack

class _Packaging(_Openstack):
	_service_type = "packaging"
	_icon_dir = "icons/openstack/packaging"

class Loci(_Packaging):
	_icon = "loci.png"
	_default_label = "Loci"

class Puppet(_Packaging):
	_icon = "puppet.png"
	_default_label = "Puppet"

class Rpm(_Packaging):
	_icon = "rpm.png"
	_default_label = "Rpm"

