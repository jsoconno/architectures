from architectures.core import Cluster

class ManagementGroup(Cluster):
    _default_label = "Management Group"

class Subscription(Cluster):
    _default_label = "Subscription"

class ResourceGroup(Cluster):
    _default_label = "Resource Group"

class VirtualNetwork(Cluster):
    _default_label = "Virtual Network"

class Subnet(Cluster):
    _default_label = "Subnet"