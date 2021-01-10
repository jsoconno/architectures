# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Outscale

class _Storage(_Outscale):
	_service_type = "storage"
	_icon_dir = "icons/outscale/storage"

class SimpleStorageService(_Storage):
	_icon = "simple-storage-service.png"
	_default_label = "Simple Storage Service"

class Storage(_Storage):
	_icon = "storage.png"
	_default_label = "Storage"

