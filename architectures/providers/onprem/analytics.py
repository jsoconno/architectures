# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Onprem

class _Analytics(_Onprem):
	_service_type = "analytics"
	_icon_dir = "icons/onprem/analytics"

class Dbt(_Analytics):
	_icon = "dbt.png"
	_default_label = "Dbt"

class Tableau(_Analytics):
	_icon = "tableau.png"
	_default_label = "Tableau"

class Databricks(_Analytics):
	_icon = "databricks.png"
	_default_label = "Databricks"

class Beam(_Analytics):
	_icon = "beam.png"
	_default_label = "Beam"

class Flink(_Analytics):
	_icon = "flink.png"
	_default_label = "Flink"

class Spark(_Analytics):
	_icon = "spark.png"
	_default_label = "Spark"

class Metabase(_Analytics):
	_icon = "metabase.png"
	_default_label = "Metabase"

class Singer(_Analytics):
	_icon = "singer.png"
	_default_label = "Singer"

class Presto(_Analytics):
	_icon = "presto.png"
	_default_label = "Presto"

class Hadoop(_Analytics):
	_icon = "hadoop.png"
	_default_label = "Hadoop"

class Hive(_Analytics):
	_icon = "hive.png"
	_default_label = "Hive"

class Superset(_Analytics):
	_icon = "superset.png"
	_default_label = "Superset"

class Norikra(_Analytics):
	_icon = "norikra.png"
	_default_label = "Norikra"

class Storm(_Analytics):
	_icon = "storm.png"
	_default_label = "Storm"

