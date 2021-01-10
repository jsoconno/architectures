# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Onprem

class _Proxmox(_Onprem):
	_service_type = "proxmox"
	_icon_dir = "icons/onprem/proxmox"

class Pve(_Proxmox):
	_icon = "pve.png"
	_default_label = "Pve"

