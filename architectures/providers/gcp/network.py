# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Gcp

class _Network(_Gcp):
    _service_type = "network"
    _icon_dir = "icons/gcp/network"

class Vpn(_Network):
    _icon = "vpn.png"
    _default_label = "Vpn"

class Dns(_Network):
    _icon = "dns.png"
    _default_label = "Dns"

class Nat(_Network):
    _icon = "nat.png"
    _default_label = "Nat"

class ExternalIpAddresses(_Network):
    _icon = "external-ip-addresses.png"
    _default_label = "External Ip Addresses"

class DedicatedInterconnect(_Network):
    _icon = "dedicated-interconnect.png"
    _default_label = "Dedicated Interconnect"

class StandardNetworkTier(_Network):
    _icon = "standard-network-tier.png"
    _default_label = "Standard Network Tier"

class Armor(_Network):
    _icon = "armor.png"
    _default_label = "Armor"

class VirtualPrivateCloud(_Network):
    _icon = "virtual-private-cloud.png"
    _default_label = "Virtual Private Cloud"

class Routes(_Network):
    _icon = "routes.png"
    _default_label = "Routes"

class Router(_Network):
    _icon = "router.png"
    _default_label = "Router"

class PartnerInterconnect(_Network):
    _icon = "partner-interconnect.png"
    _default_label = "Partner Interconnect"

class Cdn(_Network):
    _icon = "cdn.png"
    _default_label = "Cdn"

class FirewallRules(_Network):
    _icon = "firewall-rules.png"
    _default_label = "Firewall Rules"

class LoadBalancing(_Network):
    _icon = "load-balancing.png"
    _default_label = "Load Balancing"

class PremiumNetworkTier(_Network):
    _icon = "premium-network-tier.png"
    _default_label = "Premium Network Tier"

class Network(_Network):
    _icon = "network.png"
    _default_label = "Network"

class TrafficDirector(_Network):
    _icon = "traffic-director.png"
    _default_label = "Traffic Director"