# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Elastic

class _Elasticsearch(_Elastic):
	_service_type = "elasticsearch"
	_icon_dir = "icons/elastic/elasticsearch"

class Alerting(_Elasticsearch):
	_icon = "alerting.png"
	_default_label = "Alerting"

class Beats(_Elasticsearch):
	_icon = "beats.png"
	_default_label = "Beats"

class Elasticsearch(_Elasticsearch):
	_icon = "elasticsearch.png"
	_default_label = "Elasticsearch"

class Kibana(_Elasticsearch):
	_icon = "kibana.png"
	_default_label = "Kibana"

class Logstash(_Elasticsearch):
	_icon = "logstash.png"
	_default_label = "Logstash"

class MachineLearning(_Elasticsearch):
	_icon = "machine-learning.png"
	_default_label = "Machine Learning"

class Maps(_Elasticsearch):
	_icon = "maps.png"
	_default_label = "Maps"

class Monitoring(_Elasticsearch):
	_icon = "monitoring.png"
	_default_label = "Monitoring"

class SecuritySettings(_Elasticsearch):
	_icon = "security-settings.png"
	_default_label = "Security Settings"

class Sql(_Elasticsearch):
	_icon = "sql.png"
	_default_label = "Sql"

