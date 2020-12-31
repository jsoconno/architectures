# consider calling this architectures.core
# and add an architectures.themes

# themes could replace settings and allow for things like
# default, dark mode, big icon, etc.

# want to be able to control all settings easily from a class
# also, currently settings are not updating as implemented

from architectures import Graph, Cluster, Edge, Setting
from architectures.azure.ai import BatchAI
from architectures.azure.compute import VirtualMachine

settings = Setting()

with Graph("my architecture"):
    with Cluster("azure"):
        with Cluster("subscription"):
            with Cluster("resource group"):
                with Cluster("virtual network"):
                    with Cluster("subnet") as sn:
                        one = [BatchAI('batch ai'),
                            BatchAI('batch ai')]

        with Cluster("subscription 2") as sub2:
            with Cluster("resource group 2"):
                with Cluster("virtual network 2"):
                    with Cluster("subnet 2") as sn2:
                        two = VirtualMachine('vm')


    Edge(one, two, lhead=sn2.name)

    print(one)

print(one)

# touch ~/.bash_profile; open ~/.bash_profile
# export PYTHONPATH="/users/use/code"