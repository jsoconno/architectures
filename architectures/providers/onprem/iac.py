# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Onprem

class _Iac(_Onprem):
	_service_type = "iac"
	_icon_dir = "icons/onprem/iac"

class Ansible(_Iac):
	_icon = "ansible.png"
	_default_label = "Ansible"

class Atlantis(_Iac):
	_icon = "atlantis.png"
	_default_label = "Atlantis"

class Awx(_Iac):
	_icon = "awx.png"
	_default_label = "Awx"

class Terraform(_Iac):
	_icon = "terraform.png"
	_default_label = "Terraform"

