# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Gcp

class _Database(_Gcp):
    _service_type = "database"
    _icon_dir = "icons/gcp/database"

class Memorystore(_Database):
    _icon = "memorystore.png"
    _default_label = "Memorystore"

class Firestore(_Database):
    _icon = "firestore.png"
    _default_label = "Firestore"

class Datastore(_Database):
    _icon = "datastore.png"
    _default_label = "Datastore"

class Sql(_Database):
    _icon = "sql.png"
    _default_label = "Sql"

class Bigtable(_Database):
    _icon = "bigtable.png"
    _default_label = "Bigtable"

class Spanner(_Database):
    _icon = "spanner.png"
    _default_label = "Spanner"