# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Openstack

class _Deployment(_Openstack):
	_service_type = "deployment"
	_icon_dir = "icons/openstack/deployment"

class Helm(_Deployment):
	_icon = "helm.png"
	_default_label = "Helm"

class Chef(_Deployment):
	_icon = "chef.png"
	_default_label = "Chef"

class Kolla(_Deployment):
	_icon = "kolla.png"
	_default_label = "Kolla"

class Charms(_Deployment):
	_icon = "charms.png"
	_default_label = "Charms"

class Tripleo(_Deployment):
	_icon = "tripleo.png"
	_default_label = "Tripleo"

class Ansible(_Deployment):
	_icon = "ansible.png"
	_default_label = "Ansible"

