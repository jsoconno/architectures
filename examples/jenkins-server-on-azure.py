from architectures.core import Graph, Cluster, Group, Node, Edge, Flow
from architectures.themes import Default, LightMode

from architectures.providers.azure.general import Computer
from architectures.providers.azure.compute import VirtualMachineWindows
from architectures.providers.azure.storage import ManagedDiskStandardHdd, StorageAccountBlob
from architectures.providers.azure.security import KeyVault
from architectures.providers.azure.networking import NetworkSecurityGroupClassic, VirtualNetwork, VirtualSubnet
from architectures.providers.azure.management import AzureMonitor
from architectures.providers.azure.deployment import AzureRepo
from architectures.providers.azure.identity import AzureActiveDirectory

with Graph("Jenkins Server on Azure", theme=LightMode()):
    with Cluster("Virtual Network") as virtual_network_cluster:
        with Cluster("Subnet") as subnet_cluster:
            NetworkSecurityGroupClassic("NSG", width=".7")
            with Cluster("Scaled Agents") as scaled_agents_cluster:
                vm1 = VirtualMachineWindows("Build VM")
                vm2 = VirtualMachineWindows("Build VM")
                vm3 = VirtualMachineWindows("Build VM")
                agent_pool = [vm1, vm2, vm3]
            with Group():
                jenkins_server = VirtualMachineWindows("Jenkins Server")
    computer = Computer()
    active_directory = AzureActiveDirectory()
    source_control = AzureRepo()
    managed_discs = ManagedDiskStandardHdd()
    monitor = AzureMonitor()
    key_vault = KeyVault()
    blob_storage = StorageAccountBlob()
    

    Flow([computer, jenkins_server, [active_directory, managed_discs, scaled_agents_cluster, monitor]])
    Edge(vm3, [key_vault, blob_storage], ltail=scaled_agents_cluster.name)
    Edge(source_control, jenkins_server)
    Flow([vm1, vm2, vm3], style="invis")


