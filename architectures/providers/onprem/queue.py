# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Onprem

class _Queue(_Onprem):
	_service_type = "queue"
	_icon_dir = "icons/onprem/queue"

class Zeromq(_Queue):
	_icon = "zeromq.png"
	_default_label = "Zeromq"

class Celery(_Queue):
	_icon = "celery.png"
	_default_label = "Celery"

class Activemq(_Queue):
	_icon = "activemq.png"
	_default_label = "Activemq"

class Nats(_Queue):
	_icon = "nats.png"
	_default_label = "Nats"

class Kafka(_Queue):
	_icon = "kafka.png"
	_default_label = "Kafka"

class Rabbitmq(_Queue):
	_icon = "rabbitmq.png"
	_default_label = "Rabbitmq"

