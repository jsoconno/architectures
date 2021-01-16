# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Elastic

class _Enterprisesearch(_Elastic):
	_service_type = "enterprisesearch"
	_icon_dir = "icons/elastic/enterprisesearch"

class AppSearch(_Enterprisesearch):
	_icon = "app-search.png"
	_default_label = "App Search"

class EnterpriseSearch(_Enterprisesearch):
	_icon = "enterprise-search.png"
	_default_label = "Enterprise Search"

class SiteSearch(_Enterprisesearch):
	_icon = "site-search.png"
	_default_label = "Site Search"

class WorkplaceSearch(_Enterprisesearch):
	_icon = "workplace-search.png"
	_default_label = "Workplace Search"

