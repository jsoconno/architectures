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

theme = Clean()

with Graph("my architecture", output_file_format="png", theme=theme):
    with Cluster("azure"):
        with Cluster("subscription"):
            with Cluster("resource group"):
                with Cluster("virtual network"):
                    with Cluster("subnet") as sn:
                        VirtualMachine('vm')
                        Devops('test')
                        

        with Cluster("subscription 2") as sub2:
            with Cluster("resource group 2"):
                with Cluster("virtual network 2"):
                    with Cluster("subnet 2") as sn2:
                        VirtualMachine('vm2')


# touch ~/.bash_profile; open ~/.bash_profile
# export PYTHONPATH="/users/use/code"