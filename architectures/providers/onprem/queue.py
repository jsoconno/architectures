# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Onprem

class _Queue(_Onprem):
	_service_type = "queue"
	_icon_dir = "icons/onprem/queue"

class Activemq(_Queue):
	_icon = "activemq.png"
	_default_label = "Activemq"

class Celery(_Queue):
	_icon = "celery.png"
	_default_label = "Celery"

class Kafka(_Queue):
	_icon = "kafka.png"
	_default_label = "Kafka"

class Nats(_Queue):
	_icon = "nats.png"
	_default_label = "Nats"

class Rabbitmq(_Queue):
	_icon = "rabbitmq.png"
	_default_label = "Rabbitmq"

class Zeromq(_Queue):
	_icon = "zeromq.png"
	_default_label = "Zeromq"

