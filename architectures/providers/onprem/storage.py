# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Onprem

class _Storage(_Onprem):
	_service_type = "storage"
	_icon_dir = "icons/onprem/storage"

class Ceph(_Storage):
	_icon = "ceph.png"
	_default_label = "Ceph"

class Glusterfs(_Storage):
	_icon = "glusterfs.png"
	_default_label = "Glusterfs"

class CephOsd(_Storage):
	_icon = "ceph-osd.png"
	_default_label = "Ceph Osd"

