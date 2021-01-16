# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Alibabacloud

class _Network(_Alibabacloud):
	_service_type = "network"
	_icon_dir = "icons/alibabacloud/network"

class Cdn(_Network):
	_icon = "cdn.png"
	_default_label = "Cdn"

class CloudEnterpriseNetwork(_Network):
	_icon = "cloud-enterprise-network.png"
	_default_label = "Cloud Enterprise Network"

class ElasticIpAddress(_Network):
	_icon = "elastic-ip-address.png"
	_default_label = "Elastic Ip Address"

class ExpressConnect(_Network):
	_icon = "express-connect.png"
	_default_label = "Express Connect"

class NatGateway(_Network):
	_icon = "nat-gateway.png"
	_default_label = "Nat Gateway"

class ServerLoadBalancer(_Network):
	_icon = "server-load-balancer.png"
	_default_label = "Server Load Balancer"

class SmartAccessGateway(_Network):
	_icon = "smart-access-gateway.png"
	_default_label = "Smart Access Gateway"

class VirtualPrivateCloud(_Network):
	_icon = "virtual-private-cloud.png"
	_default_label = "Virtual Private Cloud"

class VpnGateway(_Network):
	_icon = "vpn-gateway.png"
	_default_label = "Vpn Gateway"

