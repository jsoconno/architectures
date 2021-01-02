# consider calling this architectures.core
# and add an architectures.themes

# themes could replace settings and allow for things like
# default, dark mode, big icon, etc.

# want to be able to control all settings easily from a class
# also, currently settings are not updating as implemented

from architectures.core import Graph, Cluster, Node, Edge
from architectures.themes import Default, Clean
from architectures.providers.azure.compute import VirtualMachine
from architectures.providers.azure.devops import Devops
from architectures.providers.azure.network import ApplicationGateway, Firewall, LoadBalancers

theme = Clean()

with Graph("my architecture", theme=theme):
    with Cluster("Azure"):
        with Cluster("Subscription"):
            with Cluster("Resource Group"):
                with Cluster("Virtual Network"):

                    with Cluster("Gateway Subnet") as gateway_subnet:
                        app_gateway = ApplicationGateway("Application Gateway")

                    with Cluster("Firewall Subnet") as firewall_subnet:
                        firewall = Firewall("Azure Firewall")

                    with Cluster("Web Tier Subnet") as web_tier_subnet:
                        web_load_balancer = LoadBalancers("Load Balancer")
                        web_vms = [
                            VirtualMachine("VM"),
                            VirtualMachine("VM")
                        ]

                    with Cluster("Business Tier Subnet") as business_tier_subnet:
                        business_load_balancer = LoadBalancers("Load Balancer")
                        business_vms = [
                            VirtualMachine("VM"),
                            VirtualMachine("VM")
                        ]

                    with Cluster("Data Tier Subnet") as data_tier_subnet:
                        data_load_balancer = LoadBalancers("Load Balancer")
                        data_vms = [
                            VirtualMachine("VM"),
                            VirtualMachine("VM")
                        ]

    Edge(app_gateway, firewall)
    Edge(firewall, web_load_balancer)
    Edge(web_load_balancer, web_vms)
    Edge(web_vms[0], business_load_balancer, ltail=web_tier_subnet.name)
    Edge(business_load_balancer, business_vms)
    Edge(business_vms[0], data_load_balancer, ltail=business_tier_subnet.name)
    Edge(data_load_balancer, data_vms)


# touch ~/.bash_profile; open ~/.bash_profile
# export PYTHONPATH="/users/use/code"