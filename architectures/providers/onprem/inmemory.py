# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Onprem

class _Inmemory(_Onprem):
	_service_type = "inmemory"
	_icon_dir = "icons/onprem/inmemory"

class Aerospike(_Inmemory):
	_icon = "aerospike.png"
	_default_label = "Aerospike"

class Hazelcast(_Inmemory):
	_icon = "hazelcast.png"
	_default_label = "Hazelcast"

class Memcached(_Inmemory):
	_icon = "memcached.png"
	_default_label = "Memcached"

class Redis(_Inmemory):
	_icon = "redis.png"
	_default_label = "Redis"

