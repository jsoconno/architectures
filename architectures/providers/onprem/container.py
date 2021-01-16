# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Onprem

class _Container(_Onprem):
	_service_type = "container"
	_icon_dir = "icons/onprem/container"

class Containerd(_Container):
	_icon = "containerd.png"
	_default_label = "Containerd"

class Crio(_Container):
	_icon = "crio.png"
	_default_label = "Crio"

class Docker(_Container):
	_icon = "docker.png"
	_default_label = "Docker"

class Firecracker(_Container):
	_icon = "firecracker.png"
	_default_label = "Firecracker"

class Gvisor(_Container):
	_icon = "gvisor.png"
	_default_label = "Gvisor"

class Lxc(_Container):
	_icon = "lxc.png"
	_default_label = "Lxc"

class Rkt(_Container):
	_icon = "rkt.png"
	_default_label = "Rkt"

