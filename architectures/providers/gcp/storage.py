# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Gcp

class _Storage(_Gcp):
    _service_type = "storage"
    _icon_dir = "icons/gcp/storage"

class PersistentDisk(_Storage):
    _icon = "persistent-disk.png"
    _default_label = "Persistent Disk"

class Filestore(_Storage):
    _icon = "filestore.png"
    _default_label = "Filestore"

class Storage(_Storage):
    _icon = "storage.png"
    _default_label = "Storage"