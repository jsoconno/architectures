The next important set of imports to know about are `themes`.  Themes are what give your graph the styling you want.  You can use what is available as is, pass in attribute overrides, or create entirely new themes to fit your needs.
```
from architectures.themes import Default, LightMode, DarkMode
```
If you are creating a diagram that uses provider services (such as AWS, GCP, or Azure), you will also need to import the services you want to use for those `providers`.

Here is an example that import an Azure Virtual Machine:
```
from architectures.providers.azure.compute import VirtualMachine
```
Importing this class will allow you to draw an Azure Virtual Machine on the graph.