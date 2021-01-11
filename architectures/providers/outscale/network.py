# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Outscale

class _Network(_Outscale):
	_service_type = "network"
	_icon_dir = "icons/outscale/network"

class SiteToSiteVpng(_Network):
	_icon = "site-to-site-vpng.png"
	_default_label = "Site To Site Vpng"

class LoadBalancer(_Network):
	_icon = "load-balancer.png"
	_default_label = "Load Balancer"

class Net(_Network):
	_icon = "net.png"
	_default_label = "Net"

class NatService(_Network):
	_icon = "nat-service.png"
	_default_label = "Nat Service"

class InternetService(_Network):
	_icon = "internet-service.png"
	_default_label = "Internet Service"

class ClientVpn(_Network):
	_icon = "client-vpn.png"
	_default_label = "Client Vpn"

